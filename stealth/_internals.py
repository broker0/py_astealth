import threading
from typing import List
import atexit

from py_astealth.sync.client import SyncStealthApiClient
from py_astealth.stealth_session import StealthSession
from py_astealth.core.api_specification import MethodSpec
from py_astealth.sync.context import DefaultContextManager


class _ThreadLocalClientProxy:
    """
    A proxy object that tracks its own lifecycle and causes cleanup when garbage collected.
    """
    def __init__(self, client: SyncStealthApiClient, manager):
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
    manages clients for threads
    """
    def __init__(self):
        self._local_storage = threading.local()
        self._local_storage.handlers = {}
        self._session = StealthSession()
        
        self._all_clients: List[SyncStealthApiClient] = []
        self._clients_lock = threading.Lock()
        self._is_shutting_down = False

    def get_client_for_thread(self) -> SyncStealthApiClient:
        """
        return or create client for current thread
        """
        proxy = getattr(self._local_storage, 'client_proxy', None)
        if proxy is None:
            if self._is_shutting_down:
                raise RuntimeError("Stealth manager is shutting down.")

            # Create a client and connect immediately
            client = SyncStealthApiClient(session=self._session, context=DefaultContextManager.context())
            client.connect()

            self._local_storage.client = client
            with self._clients_lock:
                self._all_clients.append(client)

            proxy = _ThreadLocalClientProxy(client, self)
            self._local_storage.client_proxy = proxy

        return proxy

    def get_event_for_thread(self):
        client = self.get_client_for_thread()
        return client.get_event()

    def get_handler_for_thread(self, event_type):
        return getattr(self._local_storage, 'handlers', {}).get(event_type)

    def set_handler_for_thread(self, event_type, handler):
        if not hasattr(self._local_storage, 'handlers'):
            self._local_storage.handlers = {}
            
        if handler:
            self._local_storage.handlers[event_type] = handler
        elif handler is None and event_type in self._local_storage.handlers:
            del self._local_storage.handlers[event_type]

    def close_client_for_thread(self, client: SyncStealthApiClient):
        """
        Safely closes the client and removes it from the watchlist.
        """
        with self._clients_lock:
            if self._is_shutting_down:
                return
            try:
                self._all_clients.remove(client)
            except ValueError:
                pass

        # Close the connection (gracefully stops session)
        try:
            client.close()
        except Exception:
            pass

    def shutdown(self):
        with self._clients_lock:
            if self._is_shutting_down:
                return
            self._is_shutting_down = True
            
            # Close all robust clients
            for client in self._all_clients:
                try:
                    client.close()
                except Exception:
                    pass
            self._all_clients.clear()

        # Stop the global context logic
        DefaultContextManager.context().stop()


_manager = _StealthManager()
atexit.register(_manager.shutdown)


def _create_global_proxy(method_spec: MethodSpec):
    """
    Creates a proxy function that converts a global call `stealth.Method()`
    into `current_thread_client.Method()`.
    """

    def global_api_proxy(*args, **kwargs):
        client = _manager.get_client_for_thread()
        method = getattr(client, method_spec.name)
        return method(*args, **kwargs)

    global_api_proxy.__name__ = method_spec.name
    global_api_proxy.__doc__ = f"Global API call for {method_spec.name}."
    return global_api_proxy
