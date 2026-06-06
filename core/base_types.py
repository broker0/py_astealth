from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, BinaryIO, Callable, Optional, get_type_hints
import struct
import typing
import inspect


_U32 = struct.Struct('<I')

# Caches of compiled (stream, value)->None writers and (stream)->value readers,
# keyed by the serialized type. Populated lazily by compile_writer/compile_reader.
_writer_cache: dict = {}
_reader_cache: dict = {}


def get_fixed_struct(type_obj: Any) -> Optional[struct.Struct]:
    """
    Return a pre-compiled struct.Struct if 'type_obj' serializes to a fixed-size,
    plain (no overridden pack/unpack) layout — a plain primitive or an all-primitive
    structure. Otherwise None.

    This is the single source of truth for "can this be packed/unpacked in one
    struct call" used by lists, structures and method plans.
    """
    if not inspect.isclass(type_obj):
        return None

    # plain primitive (Bool, U8..F64). DateTime is explicitly NOT plain.
    if issubclass(type_obj, PrimitiveType) and getattr(type_obj, '_is_plain', False) and type_obj._format:
        # cache compiled struct on the class
        st = getattr(type_obj, '_struct', None)
        if st is None:
            st = struct.Struct(type_obj._format)
            type_obj._struct = st
        return st

    # all-primitive structure
    if issubclass(type_obj, StructType):
        return getattr(type_obj, '_struct', None)

    return None


def compile_writer(type_obj: Any) -> Callable[[BinaryIO, Any], None]:
    """
    Compile a (stream, value)->None serializer for 'type_obj', once, recursively.

    This is the single source of truth for serialization "plans": lists, tuples,
    structures and method arguments/results all reuse the closures produced here.
    Leaf RPCType values (String / Buffer / DateTime / etc.) delegate to their own
    pack_simple_value, so custom encodings stay in one place.
    """
    cached = _writer_cache.get(type_obj)
    if cached is not None:
        return cached

    origin = typing.get_origin(type_obj)

    if type_obj is type(None):
        writer = _noop_writer

    elif origin is list:
        inner = typing.get_args(type_obj)[0]
        item_struct = get_fixed_struct(inner)
        if item_struct is not None and inspect.isclass(inner) and issubclass(inner, StructType):
            names = inner._struct_names

            def writer(stream, value, _st=item_struct, _names=names):
                stream.write(_U32.pack(len(value)))
                for item in value:
                    stream.write(_st.pack(*[getattr(item, n) for n in _names]))

        elif item_struct is not None:      # plain-primitive element
            def writer(stream, value, _st=item_struct):
                stream.write(_U32.pack(len(value)))
                for item in value:
                    stream.write(_st.pack(item))

        else:                              # variable-size element
            inner_writer = compile_writer(inner)

            def writer(stream, value, _iw=inner_writer):
                stream.write(_U32.pack(len(value)))
                for item in value:
                    _iw(stream, item)

    elif origin is tuple:
        inner_writers = [compile_writer(t) for t in typing.get_args(type_obj)]

        def writer(stream, value, _ws=inner_writers):
            for fw, v in zip(_ws, value):
                fw(stream, v)

    elif inspect.isclass(type_obj) and issubclass(type_obj, StructType):
        # reuse the struct's own compiled writer if available (registered structs),
        # else compile a segmented one now.
        writer = type_obj._writer if type_obj._writer is not None else _compile_struct_writer(type_obj)

    elif inspect.isclass(type_obj) and issubclass(type_obj, RPCType):
        # leaf type (String / Buffer / DateTime / TypedTuple / primitive): use its own pack
        writer = type_obj.pack_simple_value

    else:
        raise TypeError(f"Cannot compile writer for type {type_obj}")

    _writer_cache[type_obj] = writer
    return writer


def compile_reader(type_obj: Any) -> Callable[[BinaryIO], Any]:
    """
    Compile a (stream)->value deserializer for 'type_obj', once, recursively.
    Mirror of compile_writer; the single source of truth for deserialization.
    """
    cached = _reader_cache.get(type_obj)
    if cached is not None:
        return cached

    origin = typing.get_origin(type_obj)

    if type_obj is type(None):
        reader = _noop_reader

    elif origin is list:
        inner = typing.get_args(type_obj)[0]
        item_struct = get_fixed_struct(inner)
        if item_struct is not None and inspect.isclass(inner) and issubclass(inner, StructType):
            item_size = item_struct.size

            def reader(stream, _st=item_struct, _sz=item_size, _cls=inner):
                count = _U32.unpack(stream.read(4))[0]
                if count == 0:
                    return []
                data = stream.read(count * _sz)
                if len(data) < count * _sz:
                    raise ValueError(f"Stream ended while reading list of {_cls}")
                return [_cls(*a) for a in _st.iter_unpack(data)]

        elif item_struct is not None:      # plain-primitive element
            item_size = item_struct.size

            def reader(stream, _st=item_struct, _sz=item_size):
                count = _U32.unpack(stream.read(4))[0]
                if count == 0:
                    return []
                data = stream.read(count * _sz)
                if len(data) < count * _sz:
                    raise ValueError("Stream ended while reading list")
                return [a[0] for a in _st.iter_unpack(data)]

        else:                              # variable-size element
            inner_reader = compile_reader(inner)

            def reader(stream, _ir=inner_reader):
                count = _U32.unpack(stream.read(4))[0]
                return [_ir(stream) for _ in range(count)]

    elif origin is tuple:
        inner_readers = [compile_reader(t) for t in typing.get_args(type_obj)]

        def reader(stream, _rs=inner_readers):
            return tuple(r(stream) for r in _rs)

    elif inspect.isclass(type_obj) and issubclass(type_obj, StructType):
        reader = type_obj._reader if type_obj._reader is not None else _compile_struct_reader(type_obj)

    elif inspect.isclass(type_obj) and issubclass(type_obj, RPCType):
        reader = type_obj.unpack_simple_value

    else:
        raise TypeError(f"Cannot compile reader for type {type_obj}")

    _reader_cache[type_obj] = reader
    return reader


def _segment_fields(fields: list) -> list:
    """
    Split a struct's fields into segments: contiguous runs of plain primitives are
    merged into a single ('struct', struct.Struct, names) segment; every other field
    becomes a ('field', type, name) segment. Used to build struct writers/readers
    that pack/unpack primitive runs in one struct call and recurse on the rest.
    """
    segments = []
    run_fmt = []
    run_names = []

    def flush():
        if run_fmt:
            segments.append(('struct', struct.Struct('<' + ''.join(run_fmt)), tuple(run_names)))
            run_fmt.clear()
            run_names.clear()

    for f in fields:
        fmt = StructType._plain_format(f.type)
        if fmt is not None:
            run_fmt.append(fmt)
            run_names.append(f.name)
        else:
            flush()
            segments.append(('field', f.type, f.name))
    flush()
    return segments


def _compile_struct_writer(cls: type) -> Callable[[BinaryIO, Any], None]:
    # pre-compile field writers for non-primitive segments
    segs = []
    for seg in _segment_fields(cls._fields):
        if seg[0] == 'struct':
            segs.append((True, seg[1], seg[2]))                   # (is_block, Struct, names)
        else:
            segs.append((False, compile_writer(seg[1]), seg[2]))  # (is_block, writer, name)

    def writer(stream, value, _segs=segs):
        for is_block, obj, target in _segs:
            if is_block:
                stream.write(obj.pack(*[getattr(value, n) for n in target]))
            else:
                obj(stream, getattr(value, target))   # target is a single field name
    return writer


def _compile_struct_reader(cls: type) -> Callable[[BinaryIO], Any]:
    segs = []
    for seg in _segment_fields(cls._fields):
        if seg[0] == 'struct':
            segs.append((True, seg[1], seg[1].size))            # (is_struct_seg, Struct, size)
        else:
            segs.append((False, compile_reader(seg[1]), None))   # (False, reader, None)

    def reader(stream, _segs=segs, _cls=cls):
        args = []
        for is_block, obj, size in _segs:
            if is_block:
                data = stream.read(size)
                if len(data) < size:
                    raise ValueError(f"Stream ended while reading {_cls}")
                args.extend(obj.unpack(data))
            else:
                args.append(obj(stream))
        return _cls(*args)
    return reader


def _noop_writer(stream, value):
    pass


def _noop_reader(stream):
    return None



class RPCType(ABC):
    # '_mapping' is what python-type this stealth-type expects as a value
    _mapping = None
    # '_reads_to_end' marks a type that consumes the rest of the payload (e.g. Buffer).
    # Used by inbound argument plans to detect a trailing raw buffer.
    _reads_to_end = False

    @classmethod
    @abstractmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        """Writes the binary representation of 'value' to 'stream'."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        """Reads data from the stream 'stream' and returns a Python object."""
        raise NotImplementedError

    @staticmethod
    def pack_value(stream: BinaryIO, value: Any, type_obj: Any):
        """
        Packing a value into binary form as type 'type_obj'.

        Thin wrapper over compile_writer: all list/tuple/struct/primitive fast
        paths live in the compiled writer (single source of truth). The compiled
        closure is cached per type, so repeated calls are cheap.
        """
        compile_writer(type_obj)(stream, value)

    @staticmethod
    def unpack_value(stream: BinaryIO, type_obj: Any) -> Any:
        """
        Unpacking a binary value of type 'type_obj'.

        Thin wrapper over compile_reader (mirror of pack_value); the compiled
        reader is the single source of truth for all deserialization fast paths.
        """
        return compile_reader(type_obj)(stream)


class PrimitiveType(RPCType):
    # '_format' defines the packing and unpacking format of the given type using struct.pack/unpack
    _format = None
    # '_is_plain' marks a primitive whose pack/unpack is the default struct-based one
    # (no value transformation). DateTime sets this to False because it converts to/from days.
    _is_plain = True
    # '_struct' caches a compiled struct.Struct for '_format' (populated lazily by get_fixed_struct)
    _struct: struct.Struct = None

    @classmethod
    def _get_struct(cls) -> struct.Struct:
        """Return a cached struct.Struct for cls._format, compiling it once."""
        st = cls.__dict__.get('_struct')
        if st is None:
            st = struct.Struct(cls._format)
            cls._struct = st
        return st

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        stream.write(cls._get_struct().pack(value))

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        st = cls._get_struct()
        data = stream.read(st.size)
        if len(data) < st.size:
            raise ValueError(f"Stream ended while reading {cls}")

        # struct.unpack converts the binary data to int/bool/float per the format;
        # cls._mapping is not needed here.
        unpacked_value, = st.unpack(data)
        return unpacked_value


def split_prim_prefix(types: list) -> tuple[list, int]:
    """
    Return (struct-format parts, count) for the leading contiguous run of plain
    primitive types in 'types'. Shared by the struct, argument-encode and
    argument-decode plans so the "collect leading primitives" logic lives once.
    """
    fmt_parts = []
    for t in types:
        fmt = StructType._plain_format(t)
        if fmt is None:
            break
        fmt_parts.append(fmt)
    return fmt_parts, len(fmt_parts)


@dataclass
class ArgsPlan:
    """
    Plan for encoding a full outbound packet: [method_id(U16), call_id(U16), *args].

    'packet_struct' is set when method_id, call_id and every argument are plain
    primitives -> the whole packet is one struct.Struct.pack call.

    'prefix_struct' covers '<HH' + a leading run of plain-primitive args; the
    remaining 'tail_types' are encoded via reflection. 'prefix_arg_count' is how
    many *arguments* (not counting the 2 header fields) the prefix covers.
    """
    packet_struct: struct.Struct = None
    prefix_struct: struct.Struct = None
    prefix_arg_count: int = 0
    tail_writers: list = field(default_factory=list)    # compiled (stream, value)->None for tail args

    @staticmethod
    def build(arg_types: list) -> "ArgsPlan":
        # collect leading run of plain-primitive args
        prefix_fmt, prefix_count = split_prim_prefix(arg_types)

        if prefix_count == len(arg_types):
            # all args plain -> single packet struct (header + args)
            packet_struct = struct.Struct('<HH' + ''.join(prefix_fmt))
            return ArgsPlan(packet_struct=packet_struct)

        # header + primitive prefix in one struct, compiled writers for the tail
        prefix_struct = struct.Struct('<HH' + ''.join(prefix_fmt))
        return ArgsPlan(
            prefix_struct=prefix_struct,
            prefix_arg_count=prefix_count,
            tail_writers=[compile_writer(t) for t in arg_types[prefix_count:]],
        )


class ResultKind(Enum):
    """Strategy for decoding a method result payload."""
    NONE = auto()       # method returns None, no decoding
    FIXED = auto()      # plain primitive or all-primitive struct: single struct.unpack
    LIST = auto()       # list[T] where T is fixed-size plain: read count + iter_unpack
    GENERAL = auto()    # everything else: compiled stream reader


class ArgsDecodeKind(Enum):
    """Strategy for decoding an inbound packet's argument list."""
    EMPTY = auto()              # no arguments
    ALL_PRIM = auto()           # every arg is a plain primitive: one unpack
    PRIMS_PLUS_BUFFER = auto()  # leading plain primitives + trailing read-to-end Buffer
    GENERAL = auto()            # compiled per-arg stream readers


@dataclass
class ResultPlan:
    """
    Plan for decoding a result payload. See ResultKind for the meaning of 'kind'.
    """
    kind: ResultKind = ResultKind.GENERAL
    item_struct: struct.Struct = None       # for FIXED (the value/struct) or LIST (the element)
    cls: Any = None                         # struct class to construct (fixed struct / list of structs)
    is_struct: bool = False                 # whether item_struct unpacks into a struct ctor
    reader: Any = None                      # compiled (stream)->value for the GENERAL path

    @staticmethod
    def build(return_type: Any) -> "ResultPlan":
        if return_type is type(None) or return_type is None:
            return ResultPlan(kind=ResultKind.NONE)

        fixed = get_fixed_struct(return_type)
        if fixed is not None:
            is_struct = inspect.isclass(return_type) and issubclass(return_type, StructType)
            return ResultPlan(kind=ResultKind.FIXED, item_struct=fixed,
                              cls=return_type if is_struct else None, is_struct=is_struct)

        if typing.get_origin(return_type) is list:
            inner = typing.get_args(return_type)[0]
            item = get_fixed_struct(inner)
            if item is not None:
                is_struct = inspect.isclass(inner) and issubclass(inner, StructType)
                return ResultPlan(kind=ResultKind.LIST, item_struct=item,
                                  cls=inner if is_struct else None, is_struct=is_struct)

        return ResultPlan(kind=ResultKind.GENERAL, reader=compile_reader(return_type))


@dataclass
class ArgsDecodePlan:
    """
    Plan for decoding an inbound packet's argument list, starting at 'offset'
    (the position right after the 2-byte method id). See ArgsDecodeKind for the
    meaning of 'kind'. PRIMS_PLUS_BUFFER covers _FunctionResultCallback(CallId, Result).
    """
    kind: ArgsDecodeKind = ArgsDecodeKind.GENERAL
    prim_struct: struct.Struct = None       # for ALL_PRIM / PRIMS_PLUS_BUFFER
    readers: list = field(default_factory=list)   # compiled (stream)->value for GENERAL

    @staticmethod
    def build(arg_types: list) -> "ArgsDecodePlan":
        if not arg_types:
            return ArgsDecodePlan(kind=ArgsDecodeKind.EMPTY)

        prefix_fmt, prefix_count = split_prim_prefix(arg_types)

        if prefix_count == len(arg_types):
            return ArgsDecodePlan(kind=ArgsDecodeKind.ALL_PRIM,
                                  prim_struct=struct.Struct('<' + ''.join(prefix_fmt)))

        # leading primitives + a single trailing read-to-end Buffer
        last = arg_types[-1]
        if (prefix_count == len(arg_types) - 1
                and inspect.isclass(last)
                and getattr(last, '_reads_to_end', False)):
            prim = struct.Struct('<' + ''.join(prefix_fmt)) if prefix_fmt else None
            return ArgsDecodePlan(kind=ArgsDecodeKind.PRIMS_PLUS_BUFFER, prim_struct=prim)

        return ArgsDecodePlan(kind=ArgsDecodeKind.GENERAL,
                              readers=[compile_reader(t) for t in arg_types])


@dataclass
class ParameterSpec:
    name: str
    type: Any


@dataclass
class MethodSpec:
    id: int
    name: str
    args: list[ParameterSpec]
    result: Any
    timeout: float | None

    # Pre-computed serialization plans (filled in by method_api at decorator time,
    # mirroring how StructType.register pre-computes _struct/_prefix_struct).
    args_plan: ArgsPlan = None            # how to encode outbound arguments (with header)
    result_plan: ResultPlan = None        # how to decode the result payload
    args_decode_plan: ArgsDecodePlan = None   # how to decode inbound argument payloads


class StructType(RPCType):
    _fields: list[ParameterSpec] = []       # '_fields' is a list of structure fields to be serialized.
    _struct_format: str = None              # '_struct_format' is format string if all fields are primitive types.
    _struct: struct.Struct = None           # compiled struct.Struct for '_struct_format' (all-primitive structs).
    _struct_names: tuple = ()               # field names in struct order (used by the list fast path).

    # Compiled serializers (built once in register). They segment the struct into
    # contiguous runs of plain primitives (packed/unpacked in a single struct call)
    # plus per-field closures for the rest — covering all-primitive, prefix and
    # fully-mixed structs uniformly. See compile_writer / compile_reader.
    _writer: Callable = None
    _reader: Callable = None

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        cls._writer(stream, value)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        return cls._reader(stream)

    @staticmethod
    def register(cls: type) -> type:
        """
        A decorator for creating structured types that can be serialized using StructType.
        """
        # inspect the __init__ parameters of the class
        cls = dataclass(cls)
        hints = get_type_hints(cls)
        params = inspect.signature(cls).parameters

        # Only fields that have the type annotation will be written to fields_list
        fields_list = []

        for field_name in params:
            if field_name in hints:
                field_type = hints[field_name]
                fields_list.append(ParameterSpec(field_name, field_type))

        # attach list of fields to the class itself
        cls._fields = fields_list

        # If every field is a plain primitive, expose a single struct.Struct so that
        # get_fixed_struct() can pack/unpack lists of this struct in one iter_unpack.
        field_types = [f.type for f in fields_list]
        all_fmt, prim_count = split_prim_prefix(field_types)
        all_primitive = bool(fields_list) and prim_count == len(fields_list)

        if all_primitive:
            cls._struct = struct.Struct('<' + ''.join(all_fmt))
            cls._struct_format = cls._struct.format
            cls._struct_names = tuple(f.name for f in fields_list)
        else:
            cls._struct = None
            cls._struct_format = None
            cls._struct_names = ()

        # Compile the (segmented) writer/reader used for single values and as the
        # per-element path for lists of non-fixed structs.
        cls._writer = _compile_struct_writer(cls)
        cls._reader = _compile_struct_reader(cls)

        return cls

    @staticmethod
    def _plain_format(field_type: Any) -> Optional[str]:
        """Return the struct format char(s) for a plain primitive field, else None."""
        if not inspect.isclass(field_type):
            return None    # list/tuple/etc. are not classes
        if (issubclass(field_type, PrimitiveType)
                and getattr(field_type, '_is_plain', False)
                and field_type._format):
            fmt = field_type._format
            return fmt[1:] if fmt.startswith('<') else fmt
        return None
