import asyncio
import io
import os
import socket
import time
import struct
import sys
from dataclasses import dataclass
from enum import IntEnum
from typing import Any

from py_astealth.core.api_specification import MethodSpec
from py_astealth.core.base_types import RPCType
from py_astealth.core.rpc_client import AsyncRPCClient
from py_astealth.stealth_types import *
from py_astealth.stealth_api import StealthApi


DEFAULT_STEALTH_HOST = '127.0.0.1'
DEFAULT_STEALTH_PORT = 47602
SOCK_TIMEOUT = 10.0
GET_PORT_ATTEMPT_COUNT = 3


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


class EventType(IntEnum):
    EvItemInfo = 0
    EvItemDeleted = 1
    EvSpeech = 2
    EvDrawGamePlayer = 3
    EvMoveRejection = 4
    EvDrawContainer = 5
    EvAddItemToContainer = 6
    EvAddMultipleItemsInCont = 7
    EvRejectMoveItem = 8
    EvUpdateChar = 9
    EvDrawObject = 10
    EvMenu = 11
    EvMapMessage = 12
    EvAllowRefuseAttack = 13
    EvClilocSpeech = 14
    EvClilocSpeechAffix = 15
    EvUnicodeSpeech = 16
    EvBuffDebuffSystem = 17
    EvClientSendResync = 18
    EvCharAnimation = 19
    EvIcqDisconnect = 20
    EvIcqConnect = 21
    EvIcqIncomingText = 22
    EvIcqError = 23
    EvIncomingGump = 24
    EvTimer1 = 25
    EvTimer2 = 26
    EvWindowsMessage = 27
    EvSound = 28
    EvDeath = 29
    EvQuestArrow = 30
    EvPartyInvite = 31
    EvMapPin = 32
    EvGumpTextEntry = 33
    EvGraphicalEffect = 34
    EvIrcIncomingText = 35
    EvMessengerEvent = 36
    EvSetGlobalVar = 37
    EvUpdateObjStats = 38
    EvGlobalChat = 39
    EvWarDamage = 40
    EvContextMenu = 41


@dataclass
class StealthEvent:
    id: EventType
    arguments: list


class StealthRPCEncoder:
    """
    Serialize and deserialize arguments, results and callbacks
    """

    # encoding of event argument data types 0..7
    EVENT_TYPES = (String, U32, I32, U16, I16, U8, I8, Bool)

    @staticmethod
    def encode_arguments(method_spec: MethodSpec, *args) -> bytes:
        """
        encode arguments list to bytes
        """
        if len(args) != len(method_spec.args):
            raise TypeError(f"{method_spec.name}() takes {len(method_spec.args)} arguments but {len(args)} were given")

        with io.BytesIO() as stream:
            arg_types = [arg.type for arg in method_spec.args]
            for arg_value, arg_type in zip(args, arg_types):
                RPCType.pack_value(stream, arg_value, arg_type)

            return stream.getvalue()

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
    def encode_packet(method_spec: MethodSpec, call_id: int, *args) -> bytes:
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

    @staticmethod
    def decode_event(stream: io.BytesIO) -> (EventType, list):
        """
        decode server events (callbacks) id and arguments
        """
        event_id, arg_count = U8.unpack_simple_value(stream), U8.unpack_simple_value(stream)

        # read all event arguments from the stream
        event_payload = []
        for _ in range(arg_count):
            arg_type = U8.unpack_simple_value(stream)
            event_payload.append(StealthRPCEncoder.EVENT_TYPES[arg_type].unpack_simple_value(stream))

        return EventType(event_id), event_payload


class AsyncStealthClient(AsyncRPCClient):
    """
        implementation of a specific Stealth client protocol
    """

    # possible types of packets from the server
    class PacketType(IntEnum):
        FUNCTION_RESULT = 1
        STOP_SCRIPT = 2
        CLIENT_VERSION = 3
        TOGGLE_PAUSE = 4
        EVENT = 6
        REQ_SCRIPT_PATH = 9

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self._transport = None
        self._protocol = None
        self._connected = asyncio.Event()

        self.call_id = 0
        self._pending_replies: dict[int, asyncio.Future] = {}
        self.events: asyncio.Queue[StealthEvent] = asyncio.Queue()

    async def connect(self):
        """establishing a connection with the Stealth-client and sending a packet with the version of our protocol"""
        loop = asyncio.get_running_loop()
        try:
            self._transport, self._protocol = await loop.create_connection(
                lambda: AsyncStealthRPCProtocol(self), self.host, self.port
            )
            await self._connected.wait()  # waiting for connection to be established
            # TODO make normal package formation with the version instead of this hardcode
            encoded = b'\x05\x00\x00\x00\x01\x02\x07\x00\x00'
            self.send_packet(encoded)
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

        # for methods with a return value, we assign a new call_id
        ret_type = method_spec.result.type
        expect_reply = ret_type is not type(None)
        call_id = self._get_call_id() if expect_reply else 0

        packet = StealthRPCEncoder.encode_packet(method_spec, call_id, *args)

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

            packet_type = AsyncStealthClient.PacketType(U16.unpack_simple_value(stream))

            if packet_type == AsyncStealthClient.PacketType.FUNCTION_RESULT:
                call_id = U16.unpack_simple_value(stream)
                if call_id in self._pending_replies:
                    future = self._pending_replies.pop(call_id)

                    # all that remains in the stream is the payload of the result
                    result_payload = stream.read()
                    future.set_result(result_payload)
                else:
                    print(f"[Warning] Result received for unknown reply_id: {call_id}")

            elif packet_type == AsyncStealthClient.PacketType.EVENT:
                event_id, event_payload = StealthRPCEncoder.decode_event(stream)
                event = StealthEvent(id=event_id, arguments=event_payload)
                self.events.put_nowait(event)

            elif packet_type == AsyncStealthClient.PacketType.STOP_SCRIPT:
                print(f"[Info] Received  {packet_type.name}, close connection, stopping client")
                self.close()

            elif packet_type == AsyncStealthClient.PacketType.REQ_SCRIPT_PATH:
                lp = os.path.realpath(sys.argv[0])
                packet = StealthRPCEncoder.encode_packet(StealthApi.ScriptPath.method_spec, 0, lp)
                self.send_packet(packet)

            else:
                print(f"[Info] Received packet of unknown or unhandled type: {packet_type.name}")

        except (struct.error, ValueError, KeyError) as e:
            # KeyError - if an unknown PacketType arrives
            # struct.error, ValueError - if the packet is "broken" (unexpected end)
            print(f"[Error] Error parsing packet: {e}. Payload (hex): {payload.hex(' ')}")

    @staticmethod
    def get_stealth_port(host: str = DEFAULT_STEALTH_HOST, port: int = DEFAULT_STEALTH_PORT) -> [str, int]:
        return get_stealth_port(host, port)


def get_stealth_port(host: str = DEFAULT_STEALTH_HOST, port: int = DEFAULT_STEALTH_PORT) -> [str, int]:
    """
    Synchronously retrieves the script port from the Stealth client.
    """
    # Check command line arguments first (standard behavior)
    if len(sys.argv) >= 3 and sys.argv[2].isdigit():
        return host, int(sys.argv[2])

    for i in range(GET_PORT_ATTEMPT_COUNT):
        sock = None
        try:
            sock = socket.create_connection((host, port), timeout=SOCK_TIMEOUT)

            # Packet structure:
            # Type: 2 bytes (unsigned short) = 4
            # Value: 4 bytes (unsigned int) = 0xDEADBEEF
            packet = struct.pack('<HI', 4, 0xDEADBEEF)
            sock.sendall(packet)

            # Read length first (2 bytes)
            header_data = b''
            while len(header_data) < 2:
                chunk = sock.recv(2 - len(header_data))
                if not chunk:
                    raise ConnectionError("Connection closed while reading length")
                header_data += chunk
            
            length = struct.unpack('<H', header_data)[0]
            
            # Read payload
            payload_data = b''
            while len(payload_data) < length:
                chunk = sock.recv(length - len(payload_data))
                if not chunk:
                    raise ConnectionError("Connection closed while reading payload")
                payload_data += chunk

            if len(payload_data) >= 2:
                # The port is at offset 2 (after 2 bytes of something? logic copied from async version)
                # Wait, the async version did:
                # data = await reader.read(4096)
                # length = struct.unpack_from('<H', data)[0]
                # if len(data) >= 2 + length: ... script_port = struct.unpack_from('<H', data, 2)[0]
                
                # The async logic was slightly loose reading 4096 bytes at once.
                # Let's stick to the protocol: 2 bytes length, then `length` bytes payload.
                # The previous code did: `script_port = struct.unpack_from('<H', data, 2)[0]`
                # But `data` included the length bytes if read in one go?
                # No, `reader.read(4096)` returns whatever is available.
                # If it returned length(2) + payload, then offset 2 is start of payload.
                # So script_port is at the BEGINNING of the payload.
                
                script_port = struct.unpack_from('<H', payload_data, 0)[0]
                return host, script_port

        except (OSError, struct.error, ConnectionError):
            # If we can't connect to the main Stealth port, we can't get the script port
            if i == GET_PORT_ATTEMPT_COUNT - 1:
                if sock:
                    sock.close()
                raise RuntimeError(f"Stealth not found at {host}:{port}")
            
            if sock:
                sock.close()
            
            time.sleep(0.1)
            continue
        finally:
            if sock:
                sock.close()

    raise RuntimeError("Failed to retrieve script port from Stealth")
