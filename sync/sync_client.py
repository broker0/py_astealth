from typing import Callable, Optional

from py_astealth.api_client import AsyncStealthApiClient
from py_astealth.core.api_specification import MethodSpec, implement_api
from py_astealth.generated.sync_interface import SyncInterface
from py_astealth.stealth_api import StealthApi
from py_astealth.stealth_session import StealthSession
from py_astealth.stealth_types import StealthEvent
from py_astealth.sync.context import StealthContext, DefaultContextManager


def create_sync_proxy_method(method_spec: MethodSpec) -> Callable:
    """
    sync method implementation factory
    """

    def sync_proxy_impl(self, *args, **kwargs):
        # get an asynchronous method from the '_async_client'
        async_method = getattr(self._async_client, method_spec.name)
        # we create a coroutine method with arguments
        coro = async_method(*args, **kwargs)

        # Delegate execution to the context
        return self.context.run_coroutine(coro)

    sync_proxy_impl.__name__ = method_spec.name
    sync_proxy_impl.__doc__ = f"Sync proxy for API method {method_spec.name}(...)"
    return sync_proxy_impl


@implement_api(StealthApi, method_factory=create_sync_proxy_method)
class SyncStealthApiClient(SyncInterface):
    """
    Stealth synchronous client using the StealthContext for execution context.

    You can define HOW and WHERE the code runs by passing a `context`:
    - ThreadedContext (default): Runs in a background thread. Thread-safe.
    - DirectContext: Runs in the current thread (requires care with loops).
    """
    def __init__(self, context: StealthContext = None, session: StealthSession = None):
        if context is None:
            context = DefaultContextManager.context()

        self.context = context
        self._async_client = AsyncStealthApiClient(session)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        # Ensure context is running (lazy start logic in context itself will handle it, but explicit start is fine too)
        self.context.start()

        # Execute connect() in the context
        self.context.run_coroutine(self._async_client.connect())

    def close(self):
        # We should close the connection gracefully first
        try:
            # Try to close connection if context is still running
            if self.context.is_running():
                self.context.run_coroutine(self._async_client.close())
        except Exception:
            pass

    def get_event(self) -> Optional[StealthEvent]:
        coro = self._async_client.get_event()
        try:
            return self.context.run_coroutine(coro)
        except Exception:
            # If context is dead or error occurs
            return None
