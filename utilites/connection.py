import sys
import time
import asyncio
import socket
import struct

from py_astealth.config import DEFAULT_STEALTH_HOST, DEFAULT_STEALTH_PORT, SOCK_TIMEOUT, GET_PORT_ATTEMPT_COUNT


def get_stealth_port(host: str = DEFAULT_STEALTH_HOST, port: int = DEFAULT_STEALTH_PORT) -> int:
    """
    Synchronously retrieves the script port from the Stealth client.
    """
    # Check command line arguments first (standard behavior)
    if len(sys.argv) >= 3 and sys.argv[2].isdigit():
        return int(sys.argv[2])

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
                script_port = struct.unpack_from('<H', payload_data, 0)[0]
                return script_port

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


async def async_get_stealth_port(host: str = DEFAULT_STEALTH_HOST, port: int = DEFAULT_STEALTH_PORT) -> int:
    """
    Asynchronously retrieves the script port from the Stealth client.
    """
    # Check command line arguments first (standard behavior)
    if len(sys.argv) >= 3 and sys.argv[2].isdigit():
        return int(sys.argv[2])

    for i in range(GET_PORT_ATTEMPT_COUNT):
        reader = None
        writer = None
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(host, port), 
                timeout=SOCK_TIMEOUT
            )

            # Packet structure:
            # Type: 2 bytes (unsigned short) = 4
            # Value: 4 bytes (unsigned int) = 0xDEADBEEF
            packet = struct.pack('<HI', 4, 0xDEADBEEF)
            writer.write(packet)
            await writer.drain()

            # Read length first (2 bytes)
            header_data = await reader.readexactly(2)
            length = struct.unpack('<H', header_data)[0]
            
            # Read payload
            payload_data = await reader.readexactly(length)

            if len(payload_data) >= 2:
                script_port = struct.unpack_from('<H', payload_data, 0)[0]
                return script_port

        except (OSError, struct.error, asyncio.TimeoutError, asyncio.IncompleteReadError):
            # If we can't connect to the main Stealth port, we can't get the script port
            if i == GET_PORT_ATTEMPT_COUNT - 1:
                if writer:
                    writer.close()
                    await writer.wait_closed()
                raise RuntimeError(f"Stealth not found at {host}:{port}")
            
            if writer:
                writer.close()
                await writer.wait_closed()
            
            await asyncio.sleep(0.1)
            continue

        finally:
            if writer:
                writer.close()
                # await writer.wait_closed() # wait_closed can hang if connection is already closed/error
                try:
                    await writer.wait_closed()
                except Exception:
                    pass

    raise RuntimeError("Failed to retrieve script port from Stealth")
