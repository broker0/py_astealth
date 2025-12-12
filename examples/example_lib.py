import asyncio
import functools
from py_astealth.async_client import AsyncStealthApiClient


def graceful_shutdown(coro):
    @functools.wraps(coro)
    async def wrapper(client: AsyncStealthApiClient, *args, **kwargs):
        task_name = coro.__name__
        await client.AddToSystemJournal(f"{task_name.capitalize()} started")
        try:
            return await coro(client, *args, **kwargs)
        except asyncio.CancelledError:
            await client.AddToSystemJournal(f"{task_name.capitalize()} cancelled")
            raise
        except Exception as e:
            print(f"[!] Exception in {task_name.capitalize()}: {e}")
        finally:
            await client.AddToSystemJournal(f"{task_name.capitalize()} completed")

    return wrapper
