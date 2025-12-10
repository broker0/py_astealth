import asyncio
import threading
from abc import ABC, abstractmethod
from typing import Any, Coroutine, Optional


class StealthContext(ABC):
    """
    Abstract base class for Stealth execution contexts.
    A Context defines WHERE and HOW the coroutines (API calls) are executed.
    """

    @abstractmethod
    def run_coroutine(self, coro: Coroutine) -> Any:
        """
        Executes the coroutine and returns the result synchronously.
        This is the bridge between the synchronous Client and the asynchronous Core.
        """
        pass

    @abstractmethod
    def start(self):
        """
        Explicitly starts resources (threads/loops).
        Implementation should be idempotent (calling start multiple times is safe).
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stops the context and releases resources (if any).
        """
        pass

    @abstractmethod
    def is_running(self) -> bool:
        """
        Checks if the context is active and ready to process requests.
        """
        pass


class ThreadedContext(StealthContext):
    """
    Executes coroutines in a dedicated background thread with its own asyncio loop.
    This provides isolation and prevents blocking the main thread.
    """

    def __init__(self, name: str):
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._thread: Optional[threading.Thread] = None
        self._ready_event = threading.Event()
        self._name = name
        self._lock = threading.Lock()

    def start(self):
        with self._lock:
            if self._thread is not None and self._thread.is_alive():
                return

            self._ready_event.clear()
            self._thread = threading.Thread(target=self._run_event_loop, name=self._name, daemon=True)
            self._thread.start()

            if not self._ready_event.wait(timeout=10):
                raise RuntimeError(f"StealthContext '{self._name}' failed to start background thread.")

    def stop(self):
        with self._lock:
            if self._loop is None or not self._loop.is_running():
                return

            # Stop the loop safely from the loop's thread
            self._loop.call_soon_threadsafe(self._loop.stop)
            
            if self._thread:
                self._thread.join()
                self._thread = None
            
            self._loop = None
            self._ready_event.clear()

    def is_running(self) -> bool:
        return self._loop is not None and self._loop.is_running()

    def run_coroutine(self, coro: Coroutine) -> Any:
        # Lazy Initialization
        if not self.is_running():
            self.start()

        try:
            future = asyncio.run_coroutine_threadsafe(coro, self._loop)
            # wait for the result indefinitely (or we could expose timeout option here)
            return future.result()
        except Exception as e:
            # Re-raise exceptions from the coroutine in the calling thread
            raise e

    def _run_event_loop(self):
        """Background thread entry point."""
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        
        self._ready_event.set()
        
        try:
            self._loop.run_forever()
        finally:
            # Clean up pending tasks
            try:
                tasks = asyncio.all_tasks(self._loop)
                for task in tasks:
                    task.cancel()
                if tasks:
                    self._loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
                self._loop.run_until_complete(self._loop.shutdown_asyncgens())
            finally:
                self._loop.close()


class FastContext(StealthContext):
    """
    Executes coroutines in the Current Thread's event loop.
    Warning: This blocks the current thread until the coroutine completes.
    Useful for simple scripts, debugging, or when you are already inside an async environment
    and want to control the execution flow manually.
    """

    def __init__(self):
        self._loop = None

    def start(self):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)

    def stop(self):
        if self._loop:
            self._loop.close()
        self._loop = None

    def is_running(self) -> bool:
        # For FastContext, "is_running" implies we have access to a loop
        # We don't check .is_running() because the loop might be stopped waiting for run_until_complete
        return True

    def run_coroutine(self, coro: Coroutine) -> Any:
        if self._loop is None:
            self.start()

        # If the loop is already running (e.g. we are called from within an async def),
        # strictly speaking we cannot use run_until_complete. 
        # This implementation assumes we are in a Sync Thread calling this.
        if self._loop.is_running():
            raise RuntimeError("Cannot use DirectContext.run_coroutine from inside a running event loop.")

        return self._loop.run_until_complete(coro)


class DefaultContextManager:
    """
    Singleton manager for the default shared ThreadedContext.
    Ensures that only one global background thread is created for implicit usages.
    """
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def context(cls) -> StealthContext:
        """
        Convenience wrapper to access the global default context.
        """
        return cls.get_instance().get_context()

    def __init__(self):
        self._context: Optional[ThreadedContext] = None
        self._context_lock = threading.Lock()

    def get_context(self) -> StealthContext:
        """
        Returns the lazily initialized global context.
        """
        if self._context is None:
            with self._context_lock:
                if self._context is None:
                    self._context = ThreadedContext(name="default thread client runner")
        return self._context
