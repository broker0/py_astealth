import asyncio
import io
import os
import struct
import sys
from typing import Any

from py_astealth.core.api_specification import MethodSpec
from py_astealth.core.base_types import RPCType
from py_astealth.core.rpc_client import AsyncRPCClient
from py_astealth.stealth_types import *
from py_astealth.stealth_api import StealthApi
from py_astealth.config import VERSION, DEFAULT_STEALTH_HOST
from py_astealth.utilites.connection import async_get_stealth_port


class AsyncStealthRPCProtocol(asyncio.Protocol):
    """
        The class implements reading a data stream and splitting it into individual packets.
    """

    def __init__(self, client: AsyncRPCClient):
        self.client = client
        self.transport = None
        self._buffer = bytearray()

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport
        # notify the client about the connection
        self.client.connection_made(transport)

    def data_received(self, data: bytes):
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

            self.client.handle_packet(packet_payload)

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
    def decode_arguments(method_spec: MethodSpec, stream: io.BytesIO) -> list[Any]:
        """
        decode arguments from bytes to python types
        """
        args = []
        for arg in method_spec.args:
            args.append(RPCType.unpack_value(stream, arg.type))
        return args

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


class AsyncStealthClient(AsyncRPCClient):
    """
        implementation of a specific Stealth client protocol
    """

    def __init__(self, host: str = None, port: int = None):
        self.host = host
        self.port = port
        self._transport = None
        self._protocol = None
        self._connected = asyncio.Event()

        self._sending_allowed = asyncio.Event()
        self._sending_allowed.set()
        self.call_id = 0
        self._pending_replies: dict[int, asyncio.Future] = {}
        self.events: asyncio.Queue[StealthEvent] = asyncio.Queue()

        self._packet_handlers = {
            StealthApi._FunctionResultCallback.method_spec.id: self._handle_FunctionResultCallback,
            StealthApi._EventCallback.method_spec.id: self._handle_EventCallback,
            StealthApi._ScriptTogglePauseCallback.method_spec.id: self._handle_ScriptTogglePauseCallback,
            StealthApi._StopScriptCallback.method_spec.id: self._handle_StopScriptCallback,
            StealthApi._ScriptPathCallback.method_spec.id: self._handle_ScriptPathCallback,
        }

    async def connect(self, profile: str = None):
        """establishing a connection with the Stealth-client and sending a packet with the version of our protocol"""
        if self.host is None:
            self.host = DEFAULT_STEALTH_HOST

        if self.port is None:
            self.port = await async_get_stealth_port(self.host)

        loop = asyncio.get_running_loop()
        try:
            self._transport, self._protocol = await loop.create_connection(
                lambda: AsyncStealthRPCProtocol(self), self.host, self.port
            )
            await self._connected.wait()  # waiting for connection to be established

            # packet = StealthRPCEncoder.encode_method(StealthApi.LangVersion.method_spec, 0, 1, *VERSION)
            # self.send_packet(packet)
            await self.call_method(StealthApi._LangVersion.method_spec, 1, *VERSION)

            if profile is not None:
                await self.call_method(StealthApi._SelectProfile.method_spec, profile)

        except ConnectionRefusedError:
            print(f"Unable to connect to {self.host}:{self.port}. Connection refused.")
            raise

    def close(self):
        if self._transport:
            self._transport.close()

    def _get_call_id(self):
        self.call_id = (self.call_id + 1) & 0xFFFF
        return self.call_id

    async def call_method(self, method_spec: MethodSpec, *args) -> Any:
        # call_method receives the method_spec and arguments
        await self._sending_allowed.wait()

        # for methods with a return value, we assign a new call_id
        ret_type = method_spec.result.type
        expect_reply = ret_type is not type(None)
        call_id = self._get_call_id() if expect_reply else 0

        packet = StealthRPCEncoder.encode_method(method_spec, call_id, *args)

        future = None
        if expect_reply:
            future = asyncio.get_running_loop().create_future()
            self._pending_replies[call_id] = future

        # TODO It probably makes sense to limit the wait with a timeout
        # TODO You can create an adaptive timeout based on method_id - for example,
        #  GetPathArray3D can work for tens of seconds, while most methods should provide an "instant" response

        self.send_packet(packet)
        result_payload = await future if expect_reply else None

        return StealthRPCEncoder.decode_result(method_spec, result_payload)

    def connection_made(self, transport: asyncio.Transport):
        self._transport = transport
        self._connected.set()

    def connection_lost(self, exc):
        self._transport = None
        self._connected.clear()

        for future in self._pending_replies.values():
            if not future.done():
                future.set_exception(ConnectionAbortedError("Connection lost"))

    def send_packet(self, payload: bytes):
        if not self._transport:
            raise ConnectionError("Client not connected")

        # the packet is preceded by u32 length
        packet_len = struct.pack('<I', len(payload))
        self._transport.write(packet_len + payload)

    def handle_packet(self, payload: bytes):
        """unpacking incoming server packets"""
        try:
            stream = io.BytesIO(payload)
            method_id = U16.unpack_simple_value(stream)
            
            # Handle known server methods
            handler = self._packet_handlers.get(method_id)
            if handler:
                method_spec = StealthApi.get_method(method_id)
                args = StealthRPCEncoder.decode_arguments(method_spec, stream)
                handler(*args)
            else:
                print(f"[Info] Received packet of unknown or unhandled type: ID {method_id}")

        except (struct.error, ValueError, KeyError) as e:
            # struct.error, ValueError - if the packet is "broken" (unexpected end)
            print(f"[Error] Error parsing packet: {e}. Payload (hex): {payload.hex(' ')}")
            # TODO strict mode
            # raise ConnectionError("[Error] Error parsing packet: {e}. Payload (hex): {payload.hex(' ')}")

    def _handle_FunctionResultCallback(self, call_id: int, result_payload: bytes):
        if call_id in self._pending_replies:
            future = self._pending_replies.pop(call_id)
            future.set_result(result_payload)
        else:
            print(f"[Warning] Result received for unknown reply_id: {call_id}")

    def _handle_EventCallback(self, event_id: int, arguments: list):
        event = StealthEvent(id=EventType(event_id), arguments=arguments)
        self.events.put_nowait(event)

    def _handle_StopScriptCallback(self):
        print(f"[Info] Received StopScript, close connection, stopping client")
        self.close()

    def _handle_ScriptTogglePauseCallback(self):
        if self._sending_allowed.is_set():
            print(f"[Info] Received ScriptTogglePauseRequest, PAUSED")
            self._sending_allowed.clear()
        else:
            print(f"[Info] Received ScriptTogglePauseRequest, resume")
            self._sending_allowed.set()

    def _handle_ScriptPathCallback(self):
        script_name = os.path.realpath(sys.argv[0])
        packet = StealthRPCEncoder.encode_method(StealthApi._ScriptPath.method_spec, 0, script_name)
        self.send_packet(packet)
