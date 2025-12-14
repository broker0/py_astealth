import asyncio

from typing import List, Callable, Any, Awaitable

from py_astealth.async_client import AsyncStealthApiClient
from py_astealth.stealth_session import StealthSession


class AsyncClientPool:
    """
    A pool of pre-connected AsyncStealthApiClient instances.
    All clients share the same StealthSession.
    Default capacity - 4 clients
    """
    def __init__(self, session: StealthSession, size: int = 4):
        self.session = session
        self.size = size
        self.clients: List[AsyncStealthApiClient] = []
    
    async def connect_all(self):
        """Create and connect all clients in the pool."""
        for _ in range(self.size):
            client = AsyncStealthApiClient(self.session)
            await client.connect()
            self.clients.append(client)
    
    def close_all(self):
        """Close all clients in the pool."""
        for client in self.clients:
            client.close()
        self.clients.clear()
    
    def __len__(self):
        return len(self.clients)
    
    def __getitem__(self, index: int) -> AsyncStealthApiClient:
        return self.clients[index]
    
    async def __aenter__(self):
        await self.connect_all()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close_all()

    async def run(self, items: List[Any], processor: Callable[[AsyncStealthApiClient, Any], Awaitable[Any]] = None, pipelining: int = 1) -> List[Any]:
        """
        Execute tasks on a pool of clients

        Args:
            items: List of data items OR list of task factories (if processor is None).
            processor: Async function(client, item) -> result.
                       If None, items are assumed to be awaitables/factories calling(client).
            pipelining: Number of items to claim/execute per batch per client.
        
        Returns:
            List of results matching 'items' order.
        """
        if not items:
            return []

        # Pre-allocate results array
        results = [None] * len(items)
        
        # Shared atomic counter (simple list to pass by reference) for zero-copy processing items
        # [current_index]
        shared_index = [0]
        
        total_items = len(items)
        
        # worker does all the work to execute our tasks.
        async def worker(client: AsyncStealthApiClient):
            while True:
                # claim batch of items for processing
                start = shared_index[0]
                if start >= total_items:
                    break
                
                end = min(start + pipelining, total_items)
                shared_index[0] = end

                items_batch = (items[i] for i in range(start, end))

                try:
                    current_batch_coros = []

                    # processing of batch
                    if processor:   # Item processing mode
                        for item in items_batch:
                            current_batch_coros.append(processor(client, item))

                    else:   # Task factory mode (item is callable(client))
                        for factory in items_batch:
                            current_batch_coros.append(factory(client))
                    
                    # concurrent execution of batch coros
                    batch_results = await asyncio.gather(*current_batch_coros, return_exceptions=True)
                    
                    for i, res in enumerate(batch_results):
                        if isinstance(res, Exception):
                            print(f"[Error] Item {start + i} failed: {res}")
                        results[start + i] = res
                        
                except Exception as e:
                    print(f"Worker generic error: {e}")
                    for i in range(start, end): # Fill failed slots with exception to avoid hanging
                        results[i] = e

        # calculate number of worker for item processing
        required_workers = (total_items + pipelining - 1) // pipelining
        num_workers = max(1, min(required_workers, len(self.clients)))

        # spawn workers and wait for completion
        tasks = [asyncio.create_task(worker(self.clients[i])) for i in range(num_workers)]
        await asyncio.gather(*tasks)
        
        return results
