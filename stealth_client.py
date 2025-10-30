import asyncio
import io
import struct
from dataclasses import dataclass
from enum import IntEnum
from typing import Any

from py_astealth.core.rpc_client import AsyncRPCClient
from py_astealth.stealth_types import *


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


@dataclass
class StealthEvent:
    id: int
    arguments: list


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

    # encoding of event argument data types 0..7
    EVENT_TYPES = (String, U32, I32, U16, I16, U8, I8, Bool)

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

    async def call_method(self, method_id: int, args_payload: bytes, ret) -> Any:
        # call_method receives the id of the method being called, the packed arguments,
        # and the type of the return value of the method.

        # If the method returns a value (not None), then we generate a new call_id;
        # if it returns nothing, then call_id=0
        expect_reply = ret is not None
        call_id = self._get_call_id() if expect_reply else 0

        # a function call packet starts with two u16 values - method_id and call_id
        # and then come the packed arguments
        header = struct.pack("<2H", method_id, call_id)
        packet = header + args_payload

        # If the function returns a result, then we create a future for the response and add it to _pending_replies
        future = None
        if expect_reply:
            future = asyncio.get_running_loop().create_future()
            self._pending_replies[call_id] = future

        # TODO It probably makes sense to limit the wait with a timeout
        # TODO You can create an adaptive timeout based on method_id - for example,
        #  GetPathArray3D can work for tens of seconds, while most methods should provide an "instant" response

        # We send the package and, if necessary, wait for the result.
        self.send_packet(packet)
        return await future if expect_reply else None

    def send_packet(self, payload: bytes):
        if not self._transport:
            raise ConnectionError("Client not connected")
        # the packet is preceded by u32 length
        packet_len = struct.pack('<I', len(payload))
        self._transport.write(packet_len + payload)

    def connection_made(self, transport: asyncio.Transport):
        self._transport = transport
        self._connected.set()

    def connection_lost(self, exc):
        print("Connection lost")
        self._transport = None
        self._connected.clear()
        for future in self._pending_replies.values():
            if not future.done():
                future.set_exception(ConnectionAbortedError("Connection lost"))

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
                event_id, arg_count = EventType(U8.unpack_simple_value(stream)), U8.unpack_simple_value(stream)

                # read all event arguments from the stream
                event_payload = []
                for _ in range(arg_count):
                    arg_type = U8.unpack_simple_value(stream)
                    event_payload.append(AsyncStealthClient.EVENT_TYPES[arg_type].unpack_simple_value(stream))

                event = StealthEvent(id=event_id, arguments=event_payload)
                self.events.put_nowait(event)

            else:
                print(f"[Info] Received packet of unknown or unhandled type: {packet_type.name}")

        except (struct.error, ValueError, KeyError) as e:
            # KeyError - if an unknown PacketType arrives
            # struct.error, ValueError - if the packet is "broken" (unexpected end)
            print(f"[Error] Error parsing packet: {e}. Payload (hex): {payload.hex(' ')}")
