import asyncio
import io
import struct
import logging

from typing import Any

from py_astealth.core.api_specification import MethodSpec
from py_astealth.core.rpc_client import AsyncRPCClient

from py_astealth.stealth_types import *
from py_astealth.stealth_api import StealthApi
from py_astealth.stealth_protocol import AsyncStealthRPCProtocol, StealthRPCEncoder
from py_astealth.stealth_session import StealthSession
from py_astealth.stealth_events import EventFactory

from py_astealth.utilites.config import VERSION
from py_astealth.utilites.config import STRICT_PROTOCOL
from py_astealth.utilites.logger import client_logger


class AsyncStealthClient(AsyncRPCClient):
    """
        implementation of a specific Stealth client protocol
    """

    def __init__(self, session: StealthSession = None):
        self.events: asyncio.Queue[StealthEvent] = asyncio.Queue()

        self._session = StealthSession() if session is None else session

        self._transport = None
        self._protocol = None
        self._connected = asyncio.Event()

        self._sending_allowed = asyncio.Event()
        self._sending_allowed.set()
        self._call_id = 0
        self._pending_replies: dict[int, asyncio.Future] = {}

        self._calls = 0

        self._packet_handlers = {
            StealthApi._FunctionResultCallback.method_spec.id: self._handle_FunctionResultCallback,
            StealthApi._EventCallback.method_spec.id: self._handle_EventCallback,
            StealthApi._ScriptTogglePauseCallback.method_spec.id: self._handle_ScriptTogglePauseCallback,
            StealthApi._StopScriptCallback.method_spec.id: self._handle_StopScriptCallback,
            StealthApi._ErrorReportCallback.method_spec.id: self._handle_ErrorReportCallback,
            StealthApi._ScriptPathCallback.method_spec.id: self._handle_ScriptPathCallback,
        }

    async def connect(self) -> int:
        """establishing a connection with the Stealth-client and sending a packet with the version of our protocol"""
        
        # Negotiate port/group if needed
        await self._session.negotiate_port()

        loop = asyncio.get_running_loop()
        try:
            self._transport, self._protocol = await loop.create_connection(
                lambda: AsyncStealthRPCProtocol(self), self._session.host, self._session.script_port
            )
            await self._connected.wait()  # waiting for connection to be established

            # packet = StealthRPCEncoder.encode_method(StealthApi.LangVersion.method_spec, 0, 1, *VERSION)
            # self.send_packet(packet)
            await self.call_method(StealthApi._LangVersion.method_spec, 1, *VERSION)

            # if self.session.profile:
            #     await self.call_method(StealthApi._SelectProfile.method_spec, self.session.profile)

        except ConnectionRefusedError:
            client_logger.error(f"Unable to connect to {self._session.host}:{self._session.script_port}. Connection refused.")
            raise

        return self._session.script_group

    def close(self):
        if self._transport:
            self._transport.close()

    def _get_call_id(self):
        self._call_id = self._call_id % 0xFFFF + 1
        return self._call_id

    async def call_method(self, method_spec: MethodSpec, *args) -> Any:
        # wait if paused
        await self._sending_allowed.wait()

        # for methods with a return value, we assign a new call_id
        ret_type = method_spec.result.type
        expect_reply = ret_type is not type(None)
        call_id = self._get_call_id() if expect_reply else 0

        if client_logger.isEnabledFor(logging.INFO):
            client_logger.info(f"called({call_id}) {method_spec.name} with {args} -> {ret_type.__name__}")

        packet = StealthRPCEncoder.encode_method(method_spec, call_id, *args)

        future = None
        if expect_reply:
            future = asyncio.get_running_loop().create_future()
            self._pending_replies[call_id] = future

        # TODO It probably makes sense to limit the wait with a timeout
        # TODO You can create an adaptive timeout based on method_id - for example,
        #  GetPathArray3D can work for tens of seconds, while most methods should provide an "instant" response

        self._calls += 1
        self.send_packet(packet)
        result_payload = await future if expect_reply else None
        result = StealthRPCEncoder.decode_result(method_spec, result_payload)

        if client_logger.isEnabledFor(logging.INFO):
            if ret_type is not type(None):
                client_logger.info(f"decoded result({call_id}) for {method_spec.name} {result_payload.hex()} => {ret_type.__name__}({result})")
            else:
                client_logger.info(f"{method_spec.name} has no result({call_id})")

        return result

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

        self._protocol.send_packet(payload)

    def handle_packet(self, payload: bytes):
        """unpacking incoming server packets"""

        if client_logger.isEnabledFor(logging.DEBUG):
            client_logger.debug(f"handle_packet: {payload.hex()}")

        try:
            stream = io.BytesIO(payload)
            method_id = U16.unpack_simple_value(stream)

            # Handle known server methods
            handler = self._packet_handlers.get(method_id)
            if handler:
                method_spec = StealthApi.get_method(method_id)
                args = StealthRPCEncoder.decode_arguments(method_spec, stream)
                if client_logger.isEnabledFor(logging.DEBUG):
                    client_logger.debug(f"received {method_spec.name} with {args}")
                handler(*args)
            else:
                client_logger.error(f"Received packet of unknown or unhandled type: ID {method_id}, data: {payload.hex()}")

        except (struct.error, ValueError, KeyError) as e:
            # struct.error, ValueError - if the packet is "broken" (unexpected end)
            error_msg = f"[Error] Error parsing packet: {e}. Payload (hex): {payload.hex(' ')}"
            if STRICT_PROTOCOL:
                raise ConnectionError(error_msg)

            client_logger.error(error_msg)

    def _handle_FunctionResultCallback(self, call_id: int, result_payload: bytes):
        if call_id in self._pending_replies:
            future = self._pending_replies.pop(call_id)
            try:
                future.set_result(result_payload)
            except asyncio.exceptions.InvalidStateError:
                if client_logger.isEnabledFor(logging.DEBUG):
                    client_logger.debug(f"FunctionResultCallback({call_id}) cannot set future result {result_payload.hex()}")
        else:
            client_logger.warning(f"FunctionResultCallback({call_id}) received for unknown call_id")

    def _handle_EventCallback(self, event_id: int, arguments: list):
        event = EventFactory.create(event_id, arguments)
        self.events.put_nowait(event)

    def _handle_StopScriptCallback(self):
        client_logger.debug("StopScript, close connection, stopping client")
        self.close()

    def _handle_ErrorReportCallback(self, error: str):
        client_logger.error("ErrorReportCallback: Stealth report error %s", error)
        self.close()

    def _handle_ScriptTogglePauseCallback(self):
        if self._sending_allowed.is_set():
            client_logger.debug("ScriptTogglePauseCallback, set pause")

            self._sending_allowed.clear()
        else:
            client_logger.debug("ScriptTogglePauseCallback, resume")

            self._sending_allowed.set()

    def _handle_ScriptPathCallback(self):
        script_name = self._session.script_name
        client_logger.debug("ScriptPathCallback -> %s", script_name)

        # packet = StealthRPCEncoder.encode_method(StealthApi._ScriptPath.method_spec, 0, script_name)
        # self.send_packet(packet)

        loop = asyncio.get_running_loop()
        loop.create_task(self.call_method(StealthApi._ScriptPath.method_spec, script_name))
