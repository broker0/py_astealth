from abc import ABC, abstractmethod
from typing import Any, BinaryIO, get_type_hints
import struct
import typing
import inspect


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
            from py_astealth.stealth_types import U32   # local import prevent circular module import

            if not value:   # empty list
                U32.pack_simple_value(stream, 0)  # array length is 0 elements
                return

            # type of the first element of the list
            inner_type = typing.get_args(type_obj)[0]

            # write array length
            U32.pack_simple_value(stream, len(value))

            # we pack each element
            for item in value:
                RPCType.pack_value(stream, item, inner_type)
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
            from py_astealth.stealth_types import U32
            # read the number of array elements
            count = U32.unpack_simple_value(stream)

            # we read the required number of elements and return the list
            inner_type = typing.get_args(type_obj)[0]
            return [RPCType.unpack_value(stream, inner_type) for _ in range(count)]

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
        if len(data) < size: raise ValueError(f"Stream ended while reading {cls}")

        # unpack the received data according to the format
        unpacked_value, = struct.unpack(f'{cls._format}', data)
        # TODO float types
        # In fact, cls.mapping is not used, since struct.unpack converts the binary data
        # to an integer or bool type according to the format
        return unpacked_value


class StructType(RPCType):
    # '_fields' is a list of structure fields to be serialized.
    # The first element of the tuple is the field name, the second element is the field type.
    _fields: list[tuple[str, Any]] = []

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        # We go through the fields from the list and serialize each value with the required type.
        for field_name, field_type in cls._fields:
            field_value = getattr(value, field_name)
            RPCType.pack_value(stream, field_value, field_type)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        # We create a list of values by deserializing the value of each field.
        unpacked_args = []
        for _, field_type in cls._fields:
            unpacked_args.append(RPCType.unpack_value(stream, field_type))

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
                fields_list.append((field_name, hints[field_name]))

        # attach list of fields to the class itself
        cls._fields = fields_list
        return cls
