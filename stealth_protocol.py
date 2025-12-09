import asyncio
import io
import struct
from typing import Any

from py_astealth.core.api_specification import MethodSpec
from py_astealth.core.base_types import RPCType
from py_astealth.core.rpc_client import AsyncRPCClient
from py_astealth.stealth_types import *
from py_astealth.utilites.config import DEBUG_PROTOCOL


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

        if DEBUG_PROTOCOL > 1:
            print("data_received:", data.hex())

        self._buffer.extend(data)

        # works as long as the buffer length is greater than 4 bytes
        while len(self._buffer) >= 4:
            # peek the length of the packet
            packet_len, = struct.unpack('<I', self._buffer[:4])

            if len(self._buffer) < 4 + packet_len:
                break   # there is not enough data yet for a complete packet

            # skip the length, get the payload from the packet, remove the data from the buffer
            # and give the client the data
            packet_payload = self._buffer[4:4 + packet_len]
            self._buffer = self._buffer[4 + packet_len:]

            if DEBUG_PROTOCOL > 0:
                print("data_received.packet:", packet_len, packet_payload.hex())

            self.client.handle_packet(packet_payload)

    def send_packet(self, payload: bytes):
        if not self.transport:
            raise ConnectionError("Client not connected")

        self._tx_bytes += len(payload)
        packet_len = struct.pack('<I', len(payload))    # the packet is preceded by u32 length

        if DEBUG_PROTOCOL > 0:
            print("send_packet: ", packet_len.hex(), payload.hex())

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

        stream = io.BytesIO(payload)
        ret_type = method_spec.result.type
        return RPCType.unpack_value(stream, ret_type)
