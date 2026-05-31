"""
Per-method packet encoder and result decoder builders.

For each `MethodSpec` we compile two closures once (at decorator time):

- `encode_packet(call_id, *args) -> bytes` — produces the full wire packet
- `decode_result(payload) -> Any` (or `None` sentinel if the method returns None)

This eliminates the per-call `typing.get_origin` / `isinstance` / `issubclass`
reflection that would otherwise run inside `RPCType.pack_value` /
`RPCType.unpack_value` on every RPC call. The all-primitive cases (the bulk of
the API) collapse to a single `struct.Struct.pack` / `.unpack` with no
intermediate buffer; the slow paths use `bytearray` (encode side) and
`unpack_from` with offset tracking (decode side for String / list[String] / etc.)
rather than `io.BytesIO`.

The remaining `BytesIO`-based path (in `_make_reader` + `decode_general`) only
fires for nested-variable returns like a slow struct or `list[SlowStruct]`,
which are rare in the API.
"""
import struct
import typing
from datetime import timedelta
from io import BytesIO
from typing import Any, Callable, Optional

from py_astealth.core.base_types import (
    MethodSpec,
    ParameterSpec,
    PrimitiveType,
    RPCType,
    StructType,
)
from py_astealth.stealth_types import Buffer, DateTime, String


_U32 = struct.Struct('<I')
_HEADER = struct.Struct('<HH')
_STRING_CODEC = String.STEALTH_CODEC
_DELPHI_EPOCH = DateTime.DELPHI_EPOCH
_DAY = DateTime.DAY
_DATETIME_STRUCT = struct.Struct(DateTime._format)


def _can_fast_pack_primitive(t: Any) -> bool:
    return (
        isinstance(t, type)
        and issubclass(t, PrimitiveType)
        and bool(t._format)
        and t.pack_simple_value.__func__ is PrimitiveType.pack_simple_value.__func__
    )


def _can_fast_unpack_primitive(t: Any) -> bool:
    return (
        isinstance(t, type)
        and issubclass(t, PrimitiveType)
        and bool(t._format)
        and t.unpack_simple_value.__func__ is PrimitiveType.unpack_simple_value.__func__
    )


def _can_fast_pack_struct(t: Any) -> bool:
    return (
        isinstance(t, type)
        and issubclass(t, StructType)
        and bool(t._struct_format)
        and t.pack_simple_value.__func__ is StructType.pack_simple_value.__func__
    )


def _can_fast_unpack_struct(t: Any) -> bool:
    return (
        isinstance(t, type)
        and issubclass(t, StructType)
        and bool(t._struct_format)
        and t.unpack_simple_value.__func__ is StructType.unpack_simple_value.__func__
    )


def build_packet_encoder(method_id: int, arg_specs: list[ParameterSpec]) -> Callable[..., bytes]:
    """Return a closure that encodes a complete packet for one method.

    Fast path (all args are plain primitives): one `struct.Struct.pack` covering
    `[method_id, call_id, *args]`. No buffer allocation beyond the resulting bytes.

    Slow path (mixed args): per-arg writers compiled once into a list, invoked
    in order against a `bytearray` that is converted to `bytes` once at the end.
    """
    arg_types = [arg.type for arg in arg_specs]
    mid = method_id

    if all(_can_fast_pack_primitive(t) for t in arg_types):
        fmts = ''.join(t._format.lstrip('<') for t in arg_types)
        packet_struct = struct.Struct('<HH' + fmts)

        def encode_primitive(call_id, *args):
            return packet_struct.pack(mid, call_id, *args)

        return encode_primitive

    writers = [_make_writer(t) for t in arg_types]

    def encode_mixed(call_id, *args):
        buf = bytearray()
        buf += _HEADER.pack(mid, call_id)
        for w, v in zip(writers, args):
            w(buf, v)
        return bytes(buf)

    return encode_mixed


def build_result_decoder(return_type: Any) -> Optional[Callable[[bytes], Any]]:
    """Return a closure that decodes a result payload, or `None` if the method
    returns `None` (the caller skips the wait-for-reply branch).
    """
    if return_type is type(None) or return_type is None:
        return None

    if _can_fast_unpack_primitive(return_type):
        st = struct.Struct(return_type._format)

        def decode_primitive(payload):
            return st.unpack(payload)[0]

        return decode_primitive

    if _can_fast_unpack_struct(return_type):
        st = struct.Struct(return_type._struct_format)
        cls = return_type

        def decode_struct(payload):
            return cls(*st.unpack(payload))

        return decode_struct

    if return_type is String:
        codec = _STRING_CODEC

        def decode_string(payload):
            size = _U32.unpack_from(payload, 0)[0]
            return payload[4:4 + size].decode(codec, errors='surrogateescape')

        return decode_string

    if return_type is DateTime:
        epoch = _DELPHI_EPOCH
        dt_st = _DATETIME_STRUCT

        def decode_datetime(payload):
            return epoch + timedelta(days=dt_st.unpack(payload)[0])

        return decode_datetime

    origin = typing.get_origin(return_type)

    if origin is list:
        inner = typing.get_args(return_type)[0]

        if _can_fast_unpack_struct(inner):
            item_st = struct.Struct(inner._struct_format)
            item_size = item_st.size
            cls = inner

            def decode_list_struct(payload):
                count = _U32.unpack_from(payload, 0)[0]
                if count == 0:
                    return []
                end = 4 + count * item_size
                return [cls(*a) for a in item_st.iter_unpack(memoryview(payload)[4:end])]

            return decode_list_struct

        if _can_fast_unpack_primitive(inner):
            item_st = struct.Struct(inner._format)
            item_size = item_st.size

            def decode_list_prim(payload):
                count = _U32.unpack_from(payload, 0)[0]
                if count == 0:
                    return []
                end = 4 + count * item_size
                return [a[0] for a in item_st.iter_unpack(memoryview(payload)[4:end])]

            return decode_list_prim

        if inner is String:
            codec = _STRING_CODEC

            def decode_list_string(payload):
                count = _U32.unpack_from(payload, 0)[0]
                if count == 0:
                    return []
                offset = 4
                result = []
                for _ in range(count):
                    size = _U32.unpack_from(payload, offset)[0]
                    offset += 4
                    result.append(payload[offset:offset + size].decode(codec, errors='surrogateescape'))
                    offset += size
                return result

            return decode_list_string

    if origin is tuple:
        inner_types = typing.get_args(return_type)
        if all(_can_fast_unpack_primitive(t) for t in inner_types):
            fmt = '<' + ''.join(t._format.lstrip('<') for t in inner_types)
            tup_struct = struct.Struct(fmt)

            def decode_tuple_prim(payload):
                return tup_struct.unpack(payload)

            return decode_tuple_prim

    # General slow fallback — rare nested-variable returns only.
    reader = _make_reader(return_type)

    def decode_general(payload):
        if not payload:
            return None
        with BytesIO(payload) as stream:
            return reader(stream)

    return decode_general


def build_args_decoder(arg_specs: list[ParameterSpec]) -> Callable[[Any, int], tuple]:
    """Return a closure that decodes an inbound packet's argument list.

    Used by `AsyncStealthClient.handle_packet` for server-initiated packets
    (most importantly `_FunctionResultCallback` — called once per reply). The
    closure takes `(payload, offset)` where `offset` is the position after the
    2-byte method id and returns the arg tuple.

    Fast paths:
      * empty args              → constant `()` (no work)
      * all-primitive args      → single `Struct.unpack_from(payload, offset)`
      * primitives + trailing Buffer (covers `_FunctionResultCallback(U16, Buffer)`)
                                → one `Struct.unpack_from` + one slice
    Slow path: `BytesIO(payload).seek(offset)` + cached per-arg readers.
    """
    arg_types = [arg.type for arg in arg_specs]

    if not arg_types:
        return _empty_args_decoder

    if all(_can_fast_unpack_primitive(t) for t in arg_types):
        fmts = ''.join(t._format.lstrip('<') for t in arg_types)
        st = struct.Struct('<' + fmts)

        def decode_all_prim(payload, offset):
            return st.unpack_from(payload, offset)

        return decode_all_prim

    if (len(arg_types) >= 2
            and arg_types[-1] is Buffer
            and all(_can_fast_unpack_primitive(t) for t in arg_types[:-1])):
        prim_fmts = ''.join(t._format.lstrip('<') for t in arg_types[:-1])
        prim_struct = struct.Struct('<' + prim_fmts)
        prim_size = prim_struct.size

        def decode_prims_plus_buffer(payload, offset):
            prim_vals = prim_struct.unpack_from(payload, offset)
            tail = bytes(payload[offset + prim_size:])
            return prim_vals + (tail,)

        return decode_prims_plus_buffer

    readers = [_make_reader(t) for t in arg_types]

    def decode_general_args(payload, offset):
        with BytesIO(payload) as stream:
            stream.seek(offset)
            return tuple(r(stream) for r in readers)

    return decode_general_args


def _empty_args_decoder(payload, offset):
    return ()


def _make_writer(type_obj: Any) -> Callable[[bytearray, Any], None]:
    """Compile a `(buf: bytearray, value) -> None` closure for one value's type.

    Writers append directly to the caller's bytearray via `buf += ...` — no
    intermediate `BytesIO` allocation in the slow path.
    """
    if type_obj is type(None):
        return _noop_writer

    origin = typing.get_origin(type_obj)
    if origin is list:
        inner_writer = _make_writer(typing.get_args(type_obj)[0])

        def write_list(buf, value):
            buf += _U32.pack(len(value))
            for item in value:
                inner_writer(buf, item)

        return write_list

    if origin is tuple:
        inner_writers = [_make_writer(t) for t in typing.get_args(type_obj)]

        def write_tuple(buf, value):
            for w, v in zip(inner_writers, value):
                w(buf, v)

        return write_tuple

    if _can_fast_pack_primitive(type_obj):
        st = struct.Struct(type_obj._format)

        def write_prim(buf, value):
            buf += st.pack(value)

        return write_prim

    if _can_fast_pack_struct(type_obj):
        st = struct.Struct(type_obj._struct_format)
        field_names = tuple(f.name for f in type_obj._fields)

        def write_struct_fast(buf, value):
            buf += st.pack(*(getattr(value, n) for n in field_names))

        return write_struct_fast

    if isinstance(type_obj, type) and issubclass(type_obj, StructType):
        field_writers = [(f.name, _make_writer(f.type)) for f in type_obj._fields]

        def write_struct(buf, value):
            for name, w in field_writers:
                w(buf, getattr(value, name))

        return write_struct

    if type_obj is String:
        codec = _STRING_CODEC

        def write_string(buf, value):
            encoded = value.encode(codec)
            buf += _U32.pack(len(encoded))
            buf += encoded

        return write_string

    if type_obj is Buffer:
        def write_buffer(buf, value):
            buf += value

        return write_buffer

    if type_obj is DateTime:
        epoch = _DELPHI_EPOCH
        day = _DAY
        st = _DATETIME_STRUCT

        def write_datetime(buf, value):
            buf += st.pack((value - epoch) / day)

        return write_datetime

    # Fallback for any other `RPCType` subclass (e.g. `TypedTuple`, which is
    # decode-only — its `pack_simple_value` is the abstract `RPCType` one and
    # raises). We still attach a closure so the decorator succeeds; if a caller
    # ever actually invokes it for an unimplemented type, the abstract method
    # raises NotImplementedError. Same effective behavior as the slow path, but
    # using bytearray.
    if isinstance(type_obj, type) and issubclass(type_obj, RPCType):
        pack = type_obj.pack_simple_value

        def write_via_stream(buf, value):
            with BytesIO() as tmp:
                pack(tmp, value)
                buf += tmp.getvalue()

        return write_via_stream

    raise TypeError(f"Cannot build writer for type {type_obj}")


def _make_reader(type_obj: Any) -> Callable[[Any], Any]:
    """Compile a `(stream) -> value` closure for one value's type.

    Stream-based — used only by the general slow-fallback decoder for nested
    variable shapes that don't have a top-level fast path in
    `build_result_decoder`.
    """
    if type_obj is type(None):
        return _noop_reader

    origin = typing.get_origin(type_obj)
    if origin is list:
        inner = typing.get_args(type_obj)[0]

        if _can_fast_unpack_struct(inner):
            item_st = struct.Struct(inner._struct_format)
            item_size = item_st.size
            cls = inner

            def read_list_struct(stream):
                count = _U32.unpack(stream.read(4))[0]
                if count == 0:
                    return []
                data = stream.read(count * item_size)
                return [cls(*a) for a in item_st.iter_unpack(data)]

            return read_list_struct

        if _can_fast_unpack_primitive(inner):
            item_st = struct.Struct(inner._format)
            item_size = item_st.size

            def read_list_prim(stream):
                count = _U32.unpack(stream.read(4))[0]
                if count == 0:
                    return []
                data = stream.read(count * item_size)
                return [a[0] for a in item_st.iter_unpack(data)]

            return read_list_prim

        inner_reader = _make_reader(inner)

        def read_list(stream):
            count = _U32.unpack(stream.read(4))[0]
            return [inner_reader(stream) for _ in range(count)]

        return read_list

    if origin is tuple:
        inner_readers = [_make_reader(t) for t in typing.get_args(type_obj)]

        def read_tuple(stream):
            return tuple(r(stream) for r in inner_readers)

        return read_tuple

    if isinstance(type_obj, type) and issubclass(type_obj, RPCType):
        return type_obj.unpack_simple_value

    raise TypeError(f"Cannot build reader for type {type_obj}")


def _noop_writer(buf, value):
    pass


def _noop_reader(stream):
    return None
