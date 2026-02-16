import asyncio
import os
import struct
import sys
import threading
import logging

from typing import Optional
from concurrent.futures import Future

from py_astealth.stealth_api import StealthApi
from py_astealth.stealth_types import U16
from py_astealth.stealth_protocol import StealthRPCEncoder

from py_astealth.utilites.config import DEFAULT_STEALTH_HOST, DEFAULT_STEALTH_PORT
from py_astealth.utilites.config import GET_PORT_ATTEMPT_COUNT, SOCK_TIMEOUT
from py_astealth.utilites.config import STRICT_PROTOCOL
from py_astealth.utilites.logger import session_logger


class StealthSession:
    """
    Manages the identity and connection parameters for a Stealth script session.
    Stores the script group, profile, and negotiated script port.
    Thread-safe for concurrent negotiation across multiple event loops.
    """
    def __init__(self,
                 host: str = DEFAULT_STEALTH_HOST,
                 port: int = DEFAULT_STEALTH_PORT,
                 script_group: int = 0,
                 profile: str = "",
                 script_name: str = None):
        self.host = host
        self.port = port  # stealth port provider
        self.script_group = script_group
        self.profile = profile
        
        if script_name is None:
            self.script_name = os.path.realpath(sys.argv[0])
        else:
            self.script_name = script_name

        self.script_port: Optional[int] = None
        self.negotiated = False
        
        # Concurrency control
        self._negotiation_future: Optional[Future] = None
        self._negotiation_lock = threading.Lock()

    async def negotiate_port(self, force: bool = False) -> tuple[int, int]:
        """
        Connects to the main Stealth port to request a dedicated script port.
        Thread-safe and Loop-safe (prevents deadlocks by avoiding blocking locks across awaits).
        """
        if self.negotiated and not force:
            return self.script_port, self.script_group

        future_to_wait = None
        
        with self._negotiation_lock:
            if self.negotiated and not force:
                return self.script_port, self.script_group
            
            # check if already process negotiation
            if self._negotiation_future is None:
                self._negotiation_future = Future()
            else:
                future_to_wait = self._negotiation_future

        if future_to_wait:
            await asyncio.wrap_future(future_to_wait)
            return self.script_port, self.script_group

        try:
            await self._perform_negotiate_port()
            
            # signal success
            self._negotiation_future.set_result(True)
            return self.script_port, self.script_group
            
        except Exception as e:
            self._negotiation_future.set_exception(e)
            raise e
        finally:
            with self._negotiation_lock:
                if self._negotiation_future and self._negotiation_future.done():
                    self._negotiation_future = None

    async def _perform_negotiate_port(self):
        """
        Internal method performing the actual socket IO.
        """
        # Check command line arguments first (standard behavior) - legacy support
        if len(sys.argv) >= 3 and sys.argv[2].isdigit() and self.script_port is None:
            self.script_port = int(sys.argv[2])
            self.negotiated = True

            session_logger.debug("negotiate_port: %s passed as cmdline argument", self.port)
            return

        for i in range(GET_PORT_ATTEMPT_COUNT):
            reader = None
            writer = None
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection(self.host, self.port),
                    timeout=SOCK_TIMEOUT
                )

                session_logger.info("negotiate_port: calling _RequestPort(%s, \"%s\")", self.script_group, self.profile)

                my_call_id = 1
                packet = StealthRPCEncoder.encode_method(StealthApi._RequestPort.method_spec, my_call_id, self.script_group, self.profile)
                header = struct.pack('<I', len(packet))

                if session_logger.isEnabledFor(logging.DEBUG):
                    session_logger.debug(f"negotiate_port: packet header {header.hex()}, payload {packet.hex()}")

                writer.write(header + packet)
                await writer.drain()

                # Read length first (4 bytes)
                header_data = await reader.readexactly(4)
                length = struct.unpack('<I', header_data)[0]

                session_logger.debug("negotiate_port: length of reply %s", length)

                # Read payload
                payload = await reader.readexactly(length)

                if session_logger.isEnabledFor(logging.DEBUG):
                    session_logger.debug(f"negotiate_port: reply payload {payload.hex()}")

                method_id, call_id = StealthRPCEncoder.decode_tuple((U16, U16), payload)

                if STRICT_PROTOCOL:
                    assert method_id == StealthApi._FunctionResultCallback.method_spec.id
                    assert call_id == my_call_id

                result = payload[4:]
                new_script_port, new_script_group = StealthRPCEncoder.decode_result(StealthApi._RequestPort.method_spec, result)

                self.script_port = new_script_port
                self.script_group = new_script_group
                self.negotiated = True

                session_logger.info("negotiate_port: receiving reply with port %s and group %s", self.script_port, self.script_group)

                return

            except (OSError, struct.error, asyncio.TimeoutError, asyncio.IncompleteReadError):
                if i == GET_PORT_ATTEMPT_COUNT - 1:
                    if writer:
                        writer.close()
                        await writer.wait_closed()
                    raise RuntimeError(f"Stealth PortProviding service not available on {self.host}:{self.port}")

                if writer:
                    writer.close()
                    await writer.wait_closed()

                await asyncio.sleep(0.1)
                continue

            finally:
                if writer:
                    writer.close()
                    try:
                        await writer.wait_closed()
                    except Exception:
                        pass
        
        raise RuntimeError("Failed to retrieve script port from Stealth")
