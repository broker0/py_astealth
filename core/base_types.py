from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, BinaryIO, get_type_hints
import struct
import typing
import inspect


def _get_primitive_format(type_obj: Any) -> str | None:
    """
    Returns the struct format character if type_obj is a safe primitive type.
    Returns None otherwise.
    Safe primitives are those that inherit from PrimitiveType and have a simple _format.
    We exclude DateTime because it overrides pack/unpack logic.
    """
    if inspect.isclass(type_obj) and issubclass(type_obj, PrimitiveType):
        # Check if it's one of the safe primitives
        # We can check if it overrides pack_simple_value/unpack_simple_value
        # If it does (like DateTime), we shouldn't use raw struct packing
        if type_obj.__dict__.get('pack_simple_value') or type_obj.__dict__.get('unpack_simple_value'):
            return None
        
        fmt = getattr(type_obj, '_format', None)
        if fmt and fmt.startswith('<') and len(fmt) == 2:
            return fmt[1] # Return just the format char (e.g. 'I', 'H', 'd')
    return None


class RPCType(ABC):
    # '_mapping' is what python-type this stealth-type expects as a value
    _mapping = None

    @abstractmethod
    def pack_simple_value(self, stream: BinaryIO, value: Any):
        """Writes the binary representation of 'value' to 'stream'."""
        raise NotImplementedError

    @abstractmethod
    def unpack_simple_value(self, stream: BinaryIO) -> Any:
        """Reads data from the stream 'stream' and returns a Python object."""
        raise NotImplementedError

    @staticmethod
    def pack_value(stream: BinaryIO, value: Any, type_obj: Any):
        """Packing a value into binary form as type type_obj"""
        if type_obj is type(None):
            return  # None type has no serialization

        # # if this is a list we write the list as an array of elements
        origin = typing.get_origin(type_obj)
        if origin is list:
            if not value:   # empty list
                stream.write(struct.pack('<I', 0))  # array length is 0 elements
                return

            # type of the first element of the list
            inner_type = typing.get_args(type_obj)[0]

            # write array length
            stream.write(struct.pack('<I', len(value)))

            # Optimization: if inner_type is a safe primitive, pack all at once
            prim_fmt = _get_primitive_format(inner_type)
            if prim_fmt:
                # Construct format string: < + count * fmt
                # e.g. <1000I
                full_fmt = f'<{len(value)}{prim_fmt}'
                stream.write(struct.pack(full_fmt, *value))
                return

            # we pack each element
            for item in value:
                RPCType.pack_value(stream, item, inner_type)
            return

        # if this is a tuple we write the tuple elements sequentially
        if origin is tuple:
            inner_types = typing.get_args(type_obj)
            for item, item_type in zip(value, inner_types):
                RPCType.pack_value(stream, item, item_type)
            return

        # If the type is inherited from StealthType, then we call its pack method
        if inspect.isclass(type_obj) and issubclass(type_obj, RPCType):
            type_obj.pack_simple_value(stream, value)
        else:
            raise TypeError(f"Serialization of this value type is not implemented: {type_obj}")

    @staticmethod
    def unpack_value(stream: BinaryIO, type_obj: Any) -> Any:
        """Unpacking a binary value"""

        if type_obj is type(None):
            return None

        # Processing the list
        origin = typing.get_origin(type_obj)
        if origin is list:
            # read the number of array elements
            data = stream.read(4)
            if len(data) < 4:
                raise ValueError("Stream ended while reading list length")
            count, = struct.unpack('<I', data)

            # we read the required number of elements and return the list
            inner_type = typing.get_args(type_obj)[0]

            # Optimization: if inner_type is a safe primitive, unpack all at once
            prim_fmt = _get_primitive_format(inner_type)
            if prim_fmt:
                full_fmt = f'<{count}{prim_fmt}'
                size = struct.calcsize(full_fmt)
                data = stream.read(size)
                if len(data) < size:
                    raise ValueError(f"Stream ended while reading list of {inner_type}")
                return list(struct.unpack(full_fmt, data))

            return [RPCType.unpack_value(stream, inner_type) for _ in range(count)]

        # Processing the tuple
        if origin is tuple:
            inner_types = typing.get_args(type_obj)
            return tuple(RPCType.unpack_value(stream, t) for t in inner_types)

        # If the type is inherited from StealthType, then we call its unpack method
        if inspect.isclass(type_obj) and issubclass(type_obj, RPCType):
            return type_obj.unpack_simple_value(stream)
        else:
            raise TypeError(f"Deserialization of this value type is not implemented: {type_obj}")


class PrimitiveType(RPCType):
    # '_format' defines the packing and unpacking format of the given type using struct.pack/unpack
    _format = None

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        stream.write(struct.pack(cls._format, value))

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        # We calculate the size of this type in bytes and read from the stream
        size = struct.calcsize(f'{cls._format}')
        data = stream.read(size)
        if len(data) < size:
            raise ValueError(f"Stream ended while reading {cls}")

        # unpack the received data according to the format
        unpacked_value, = struct.unpack(f'{cls._format}', data)

        # In fact, cls.mapping is not used, since struct.unpack converts the binary data
        # to an integer or bool type according to the format
        return unpacked_value


@dataclass
class ParameterSpec:
    name: str
    type: Any


class StructType(RPCType):
    # '_fields' is a list of structure fields to be serialized.
    _fields: list[ParameterSpec] = []

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        # Optimization: use pre-calculated format
        if getattr(cls, '_struct_format', None):
            values = [getattr(value, field.name) for field in cls._fields]
            stream.write(struct.pack(cls._struct_format, *values))
            return

        # We go through the fields from the list and serialize each value with the required type.
        for field in cls._fields:
            field_value = getattr(value, field.name)
            RPCType.pack_value(stream, field_value, field.type)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        # Optimization: use pre-calculated format
        if getattr(cls, '_struct_format', None):
            size = struct.calcsize(cls._struct_format)
            data = stream.read(size)
            if len(data) < size:
                raise ValueError(f"Stream ended while reading struct {cls}")
            unpacked_args = struct.unpack(cls._struct_format, data)
            return cls(*unpacked_args)

        # We create a list of values by deserializing the value of each field.
        unpacked_args = []
        for field in cls._fields:
            unpacked_args.append(RPCType.unpack_value(stream, field.type))

        # TODO maybe add validation of constructor arguments and types of unboxed values or is this too complicated?
        # We pass this list as arguments to the class constructor and return the created object.
        return cls(*unpacked_args)

    @staticmethod
    def register(cls: type) -> type:
        """
        A decorator for creating structured types that can be serialized using StructType.
        """
        # inspect the __init__ parameters of the class
        hints = get_type_hints(cls)
        params = inspect.signature(cls).parameters

        # Only fields that have the type annotation will be written to fields_list
        fields_list = []
        for field_name in params:
            if field_name in hints:
                fields_list.append(ParameterSpec(field_name, hints[field_name]))

        # attach list of fields to the class itself
        cls._fields = fields_list

        # Optimization: pre-calculate struct format if all fields are primitives
        field_formats = []
        for field in fields_list:
            fmt = _get_primitive_format(field.type)
            if not fmt:
                field_formats = None
                break
            field_formats.append(fmt)
        
        if field_formats:
            cls._struct_format = '<' + ''.join(field_formats)
        else:
            cls._struct_format = None

        return cls
