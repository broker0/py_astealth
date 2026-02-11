from datetime import datetime, timedelta
from typing import Any, BinaryIO

from py_astealth.core.base_types import PrimitiveType, RPCType
from py_astealth.stealth_events import StealthEvent
from py_astealth.stealth_enums import EventType


__all__ = ['Buffer', 'Bool', 'U8', 'I8', 'U16', 'I16', 'U32', 'I32', 'U64', 'I64', 'F32', 'F64',
           'DateTime', 'String', 'EventType', 'StealthEvent', 'TypedTuple']


class Buffer(RPCType):
    _mapping = bytes

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        stream.write(value)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        return stream.read()


class Bool(PrimitiveType):
    _format = '<?'
    _mapping = bool


class U8(PrimitiveType):
    _format = '<B'
    _mapping = int


class I8(PrimitiveType):
    _format = '<b'
    _mapping = int


class U16(PrimitiveType):
    _format = '<H'
    _mapping = int


class I16(PrimitiveType):
    _format = '<h'
    _mapping = int


class U32(PrimitiveType):
    _format = '<I'
    _mapping = int


class I32(PrimitiveType):
    _format = '<i'
    _mapping = int


class U64(PrimitiveType):
    _format = '<Q'
    _mapping = int


class I64(PrimitiveType):
    _format = '<q'
    _mapping = int


class F32(PrimitiveType):
    _format = "<f"
    _mapping = float


class F64(PrimitiveType):
    _format = "<d"
    _mapping = float


class DateTime(F64):
    _format = "<d"
    _mapping = datetime
    DELPHI_EPOCH = datetime(1899, 12, 30)
    DAY = timedelta(days=1)

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        days = (value - cls.DELPHI_EPOCH) / cls.DAY
        super().pack_simple_value(stream, days)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        days = super().unpack_simple_value(stream)
        return cls.DELPHI_EPOCH + timedelta(days=days)


class String(RPCType):
    _mapping = str
    STEALTH_CODEC = 'UTF_16LE'

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        encoded_str = value.encode(cls.STEALTH_CODEC)
        # The length is written as 4 bytes.
        U32.pack_simple_value(stream, len(encoded_str))
        # Write encoded to UTF-16_LE string bytes
        stream.write(encoded_str)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        # read the string length as a U32 value
        size = U32.unpack_simple_value(stream)
        data = stream.read(size)
        if len(data) < size:
            raise ValueError(f"Stream ended while reading {cls}")

        # cls.mapping is not used here either, so decode returns a string
        decoded_value = data.decode(cls.STEALTH_CODEC)
        return decoded_value

class TypedTuple(RPCType):
    _mapping = tuple
    TYPE_MAP = (String, U32, I32, U16, I16, U8, I8, Bool)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> list[Any]:
        count = U8.unpack_simple_value(stream)
        args = []

        for _ in range(count):
            arg_type_idx = U8.unpack_simple_value(stream)
            if 0 <= arg_type_idx < len(TypedTuple.TYPE_MAP):
                arg_type = TypedTuple.TYPE_MAP[arg_type_idx]
                args.append(arg_type.unpack_simple_value(stream))
            else:
                raise ValueError(f"Unknown event argument type index: {arg_type_idx}")

        return args
