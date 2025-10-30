import asyncio
from abc import ABC, abstractmethod


class AsyncRPCClient(ABC):
    """
        The client's base class defines the methods that the client must implement.
    """

    @abstractmethod
    def connection_made(self, transport: asyncio.Transport):
        pass

    @abstractmethod
    def handle_packet(self, payload: bytes):
        pass

    @abstractmethod
    def send_packet(self, payload: bytes):
        pass

    @abstractmethod
    def connection_lost(self, exc):
        pass

    @abstractmethod
    def call_method(self, method_id: int, args_payload: bytes, ret):
        pass
