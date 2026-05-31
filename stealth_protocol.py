import asyncio
import io
import struct
import logging

from typing import Any

from py_astealth.core.api_specification import MethodSpec
from py_astealth.core.base_types import RPCType
from py_astealth.core.rpc_client import AsyncRPCClient
from py_astealth.stealth_types import *
from py_astealth.utilites.logger import protocol_logger


_U32_HEADER = struct.Struct('<I')


class AsyncStealthRPCProtocol(asyncio.Protocol):
    """
        The class implements reading a data stream and splitting it into individual packets.
    """

    def __init__(self, client: AsyncRPCClient):
        self.client = client
        self.transport = None
        self._buffer = bytearray()
        self._tx_bytes = 0
        self._rx_bytes = 0

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport
        # notify the client about the connection
        self.client.connection_made(transport)

    def data_received(self, data: bytes):
        self._rx_bytes += len(data)

        if protocol_logger.isEnabledFor(logging.DEBUG):
            protocol_logger.debug(f"data_received: {data.hex()}")

        buf = self._buffer
        buf.extend(data)

        # works as long as the buffer length is greater than 4 bytes
        while len(buf) >= 4:
            # peek the length of the packet without slicing or re-parsing the format
            packet_len = _U32_HEADER.unpack_from(buf, 0)[0]
            total = 4 + packet_len

            if len(buf) < total:
                break   # there is not enough data yet for a complete packet

            # take a detached copy of the payload (its own bytearray), then trim
            # the buffer in place — no allocation of a fresh tail copy
            packet_payload = buf[4:total]
            if protocol_logger.isEnabledFor(logging.INFO):
                protocol_logger.info(f"data_received: len {buf[:4].hex()} payload {packet_payload.hex()}")

            del buf[:total]

            self.client.handle_packet(packet_payload)

    def send_packet(self, payload: bytes):
        if not self.transport:
            raise ConnectionError("Client not connected")

        self._tx_bytes += len(payload)
        packet_len = struct.pack('<I', len(payload))    # the packet is preceded by u32 length

        if protocol_logger.isEnabledFor(logging.INFO):
            protocol_logger.info(f"send_packet: len {packet_len.hex()} payload {payload.hex()}")

        self.transport.write(packet_len + payload)

    def connection_lost(self, exc):
        self.client.connection_lost(exc)

    def close(self):
        if self.transport:
            self.transport.close()


class StealthRPCEncoder:
    """
    Serialize and deserialize arguments, results and callbacks
    """

    @staticmethod
    def encode_arguments(method_spec: MethodSpec, *args) -> bytes:
        """
        encode arguments list to bytes
        """
        if len(args) != len(method_spec.args):
            raise TypeError(f"{method_spec.name}() takes {len(method_spec.args)} arguments but {len(args)} were given")

        return StealthRPCEncoder.encode_tuple(*zip(args, (arg.type for arg in method_spec.args)))

    @staticmethod
    def decode_arguments(method_spec: MethodSpec, stream: io.BytesIO) -> tuple:
        """
        decode arguments from bytes to python types
        """
        return tuple(RPCType.unpack_value(stream, arg.type) for arg in method_spec.args)
        # args = []
        # for arg in method_spec.args:
        #     args.append(RPCType.unpack_value(stream, arg.type))
        # return args

    @staticmethod
    def encode_tuple(*items) -> bytes:
        """
        Encodes a sequence of (value, type) pairs into bytes.
        Example: encode_tuple((10, U16), (0, U16))
        """
        with io.BytesIO() as stream:
            for value, type_cls in items:
                RPCType.pack_value(stream, value, type_cls)

            return stream.getvalue()

    @staticmethod
    def decode_tuple(item_types, payload: bytes) -> tuple:
        """
        Decodes a bytes to a sequence of types
        Example: decode_tuple(byte_buffer, U16, U16)
        """
        with io.BytesIO(payload) as stream:
            return tuple(RPCType.unpack_value(stream, item_type) for item_type in item_types)

    @staticmethod
    def encode_method(method_spec: MethodSpec, call_id: int, *args) -> bytes:
        """
        encode full packet with header and arguments
        """
        header = StealthRPCEncoder.encode_tuple((method_spec.id, U16), (call_id, U16))
        args_payload = StealthRPCEncoder.encode_arguments(method_spec, *args)
        return header + args_payload

    @staticmethod
    def decode_result(method_spec: MethodSpec, payload: bytes) -> Any:
        """
        decode single (result) value from bytes to python types
        """
        if not payload:
            return None

        with io.BytesIO(payload) as stream:
            ret_type = method_spec.result.type
            return RPCType.unpack_value(stream, ret_type)
