from typing import Any, BinaryIO
from py_astealth.core.base_types import PrimitiveType, RPCType

__all__ = ['U8', 'I8', 'U16', 'I16', 'U32', 'I32', 'U64', 'I64', 'String', 'Bool']


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

# TODO float types, date type


class String(RPCType):
    _mapping = str
    STEALTH_CODEC = 'UTF_16LE'

    @classmethod
    def pack_simple_value(cls, stream: BinaryIO, value: Any):
        encoded_str = value.encode(String.STEALTH_CODEC)
        # The length is written as 4 bytes.
        U32.pack_simple_value(stream, len(encoded_str))
        # Write encoded to UTF-16_LE string bytes
        stream.write(encoded_str)

    @classmethod
    def unpack_simple_value(cls, stream: BinaryIO) -> Any:
        # read the string length as a U32 value
        size = U32.unpack_simple_value(stream)
        data = stream.read(size)
        if len(data) < size: raise ValueError(f"Stream ended while reading {cls}")

        # cls.mapping is not used here either, so decode returns a string
        decoded_value = data.decode(String.STEALTH_CODEC)
        return decoded_value



