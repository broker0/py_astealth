import asyncio
import io
import struct
import logging

from datetime import timedelta
from typing import Any

from py_astealth.core.api_specification import MethodSpec
from py_astealth.core.base_types import RPCType, ResultKind, ArgsDecodeKind
from py_astealth.core.rpc_client import AsyncRPCClient
from py_astealth.stealth_types import *
from py_astealth.utilites.logger import protocol_logger


_HEADER = struct.Struct('<HH')
_U32 = struct.Struct('<I')


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
            if protocol_logger.isEnabledFor(logging.INFO):
                protocol_logger.info(f"data_received: len {self._buffer[:4].hex()} payload {packet_payload.hex()}")

            self._buffer = self._buffer[4 + packet_len:]

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
        decode arguments from bytes to python types.

        Uses the pre-computed 'args_decode_plan' for the common fast paths
        (all-primitive args, or primitives followed by a trailing Buffer such as
        _FunctionResultCallback), falling back to per-arg reflection.
        """
        plan = method_spec.args_decode_plan

        if plan is not None:
            kind = plan.kind
            if kind is ArgsDecodeKind.EMPTY:
                return ()

            if kind is ArgsDecodeKind.ALL_PRIM:
                st = plan.prim_struct
                data = stream.read(st.size)
                if len(data) < st.size:
                    raise ValueError(f"Stream ended while reading arguments of {method_spec.name}")
                return st.unpack(data)

            if kind is ArgsDecodeKind.PRIMS_PLUS_BUFFER:
                prim = plan.prim_struct
                prim_vals = ()
                if prim is not None:
                    data = stream.read(prim.size)
                    if len(data) < prim.size:
                        raise ValueError(f"Stream ended while reading arguments of {method_spec.name}")
                    prim_vals = prim.unpack(data)
                return prim_vals + (stream.read(),)

            if kind is ArgsDecodeKind.GENERAL:    # compiled per-arg readers
                return tuple(r(stream) for r in plan.readers)

        return tuple(RPCType.unpack_value(stream, arg.type) for arg in method_spec.args)

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
        encode full packet with header and arguments.

        Uses the pre-computed 'args_plan': all-primitive arguments collapse to a
        single struct.Struct.pack covering [method_id, call_id, *args]; a leading
        primitive prefix is packed in one call with the tail encoded via reflection.
        """
        if len(args) != len(method_spec.args):
            raise TypeError(f"{method_spec.name}() takes {len(method_spec.args)} arguments but {len(args)} were given")

        plan = method_spec.args_plan
        if plan is not None:
            if plan.packet_struct is not None:
                return plan.packet_struct.pack(method_spec.id, call_id, *args)

            if plan.prefix_struct is not None:
                n = plan.prefix_arg_count
                buf = bytearray(plan.prefix_struct.pack(method_spec.id, call_id, *args[:n]))
                with io.BytesIO() as stream:
                    for value, w in zip(args[n:], plan.tail_writers):
                        w(stream, value)
                    buf += stream.getvalue()
                return bytes(buf)

        # fallback
        header = StealthRPCEncoder.encode_tuple((method_spec.id, U16), (call_id, U16))
        args_payload = StealthRPCEncoder.encode_arguments(method_spec, *args)
        return header + args_payload

    @staticmethod
    def decode_result(method_spec: MethodSpec, payload: bytes) -> Any:
        """
        decode single (result) value from bytes to python types.

        Uses the pre-computed 'result_plan' for fast paths (plain primitive,
        all-primitive struct, list of fixed-size elements), falling back to a
        stream-based reflection decode for variable shapes (String, DateTime,
        prefix structs, list[String], etc.).
        """
        if not payload:
            return None

        plan = method_spec.result_plan
        if plan is not None:
            kind = plan.kind

            if kind is ResultKind.FIXED:
                st = plan.item_struct
                if len(payload) < st.size:
                    raise ValueError(f"Payload too short for result of {method_spec.name}")
                if plan.is_struct:
                    return plan.cls(*st.unpack_from(payload, 0))
                return st.unpack_from(payload, 0)[0]

            if kind is ResultKind.LIST:
                count = _U32.unpack_from(payload, 0)[0]
                if count == 0:
                    return []
                st = plan.item_struct
                end = 4 + count * st.size
                if len(payload) < end:
                    raise ValueError(f"Payload too short for list result of {method_spec.name}")
                view = memoryview(payload)[4:end]
                if plan.is_struct:
                    cls = plan.cls
                    return [cls(*a) for a in st.iter_unpack(view)]
                return [a[0] for a in st.iter_unpack(view)]

            if kind is ResultKind.GENERAL:     # compiled reader
                with io.BytesIO(payload) as stream:
                    return plan.reader(stream)

        # general fallback
        with io.BytesIO(payload) as stream:
            return RPCType.unpack_value(stream, method_spec.result.type)
