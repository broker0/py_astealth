import asyncio
import io
import os
import struct
import sys

from py_astealth.stealth_api import StealthApi
from py_astealth.stealth_types import U16, U64
from py_astealth.stealth_protocol import StealthRPCEncoder

from py_astealth.utilites.config import DEFAULT_STEALTH_HOST, DEFAULT_STEALTH_PORT
from py_astealth.utilites.config import GET_PORT_ATTEMPT_COUNT, SOCK_TIMEOUT
from py_astealth.utilites.config import STRICT_PROTOCOL


class StealthSession:
    """
    Manages the identity and connection parameters for a Stealth script session.
    Stores the script group, profile, and negotiated script port.
    
    Not thread-safe for concurrent negotiation across multiple event loops.
    Safe for concurrent use within a single event loop if initialized sequentially.
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

        self.script_port: int | None = None
        self.negotiated = False

    async def negotiate_port(self, force: bool = False) -> tuple[int, int]:
        """
        Connects to the main Stealth port to request a dedicated script port.
        Updates self.script_port and self.group_id with values returned by Stealth.
        """
        if self.negotiated and not force:
            return self.script_port, self.script_group

        # Check command line arguments first (standard behavior) - legacy support
        if len(sys.argv) >= 3 and sys.argv[2].isdigit() and self.script_port is None:
            self.script_port = int(sys.argv[2])
            return self.script_port, self.script_group   # TODO What if port in argument and group==0?

        for i in range(GET_PORT_ATTEMPT_COUNT):
            reader = None
            writer = None
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection(self.host, self.port),
                    timeout=SOCK_TIMEOUT
                )

                CALL_ID = 1
                packet = StealthRPCEncoder.encode_method(StealthApi._RequestPort.method_spec, CALL_ID, self.script_group, self.profile)
                header = struct.pack('<I', len(packet))
                writer.write(header + packet)
                await writer.drain()

                # Read length first (4 bytes)
                header_data = await reader.readexactly(4)
                length = struct.unpack('<I', header_data)[0]

                # Read payload
                payload_data = await reader.readexactly(length)

                stream = io.BytesIO(payload_data)
                method_id = U16.unpack_simple_value(stream)
                call_id = U16.unpack_simple_value(stream)

                if STRICT_PROTOCOL:
                    assert method_id == StealthApi._FunctionResultCallback.method_spec.id
                    assert call_id == CALL_ID

                new_script_port = U16.unpack_simple_value(stream)
                new_script_group = U64.unpack_simple_value(stream)
                
                self.script_port = new_script_port
                self.script_group = new_script_group
                self.negotiated = True

                return self.script_port, self.script_group

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
