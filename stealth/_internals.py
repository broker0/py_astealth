import asyncio
import threading
from typing import Optional, List
import atexit

from py_astealth.api_client import AsyncStealthApiClient
from py_astealth.core.api_specification import MethodSpec

from py_astealth.utilites.connection import get_stealth_port


class _ThreadLocalClientProxy:
    """
    A proxy object that tracks its own lifecycle and causes cleanup when garbage collected.
    """
    def __init__(self, client: AsyncStealthApiClient, manager):
        self._client = client
        self._manager = manager

    def __getattr__(self, name):
        # redirect all requests to attributes to the real client
        return getattr(self._client, name)

    def __del__(self):
        if self._manager and self._client:
            self._manager.close_client_for_thread(self._client)


class _StealthManager:
    """
    manages the event loop and clients
    """
    def __init__(self):
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._thread: Optional[threading.Thread] = None
        self._is_shutting_down = False

        self._local_storage = threading.local()
        self._local_storage.handlers = {}
        self._all_clients: List[AsyncStealthApiClient] = []
        self._clients_lock = threading.Lock()

        self._start_event_loop()
        self.get_client_for_thread()    # generate client for current (main) thread

    def get_client_for_thread(self) -> AsyncStealthApiClient:
        """
        return or create client for current thread
        """
        proxy = getattr(self._local_storage, 'client_proxy', None)
        if proxy is None:
            if self._is_shutting_down:
                raise RuntimeError("Stealth manager is shutting down.")

            host, port = get_stealth_port()
            print("port", port)
            client = AsyncStealthApiClient(host, port)

            future = asyncio.run_coroutine_threadsafe(client.connect(), self._loop)
            future.result(timeout=10)

            self._local_storage.client = client
            with self._clients_lock:
                self._all_clients.append(client)

            proxy = _ThreadLocalClientProxy(client, self)
            self._local_storage.client_proxy = proxy

        return proxy

    def get_event_for_thread(self):
        client = self.get_client_for_thread()
        future = asyncio.run_coroutine_threadsafe(client.get_event(), self._loop)
        return future.result(timeout=10)

    def get_handler_for_thread(self, event_type):
        return self._local_storage.handlers.get(event_type)

    def set_handler_for_thread(self, event_type, handler):
        if handler:
            self._local_storage.handlers[event_type] = handler
        elif handler is None and event_type in self._local_storage.handlers:
            del self._local_storage.handlers[event_type]

    def close_client_for_thread(self, client: AsyncStealthApiClient):
        """
        Safely closes the client and removes it from the watchlist.
        Called from the __del__ proxy object.
        """
        with self._clients_lock:
            if self._is_shutting_down:
                return

            try:
                self._all_clients.remove(client)
            except ValueError:
                pass

        client.close()

    def _start_event_loop(self):
        ready_event = threading.Event()
        self._loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self._run_forever, args=(ready_event,), daemon=True)
        self._thread.start()
        if not ready_event.wait(timeout=10):
            raise RuntimeError("Stealth background thread failed to start.")

    def shutdown(self):
        with self._clients_lock:
            if self._is_shutting_down or not (self._loop and self._loop.is_running()):
                return
            self._is_shutting_down = True

        with self._clients_lock:
            for client in self._all_clients:
                client.close()
            self._all_clients.clear()

        self._loop.call_soon_threadsafe(self._loop.stop)
        self._thread.join()
        self._thread = None
        self._loop = None
        print("Stealth manager shut down gracefully.")

    def _run_forever(self, ready_event: threading.Event):
        asyncio.set_event_loop(self._loop)
        ready_event.set()
        try:
            self._loop.run_forever()
        finally:
            tasks = asyncio.all_tasks(loop=self._loop)
            if tasks:
                for task in tasks: task.cancel()
                group = asyncio.gather(*tasks, return_exceptions=True)
                self._loop.run_until_complete(group)
            self._loop.close()


_manager = _StealthManager()
atexit.register(_manager.shutdown)


def _create_global_proxy(method_spec: MethodSpec):
    """Creates a proxy function that delegates calls to the manager."""

    def global_api_proxy(*args, **kwargs):
        async_client_proxy = _manager.get_client_for_thread()

        # Perform an asynchronous call through the manager's event loop
        async_method = getattr(async_client_proxy, method_spec.name)
        coro = async_method(*args, **kwargs)
        future = asyncio.run_coroutine_threadsafe(coro, _manager._loop)
        return future.result(timeout=30)

    global_api_proxy.__name__ = method_spec.name
    global_api_proxy.__doc__ = f"Global API call for {method_spec.name}."
    return global_api_proxy


