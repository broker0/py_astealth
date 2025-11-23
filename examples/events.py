import asyncio
import random
from datetime import datetime

from py_astealth.api_client import AsyncStealthApiClient
from py_astealth.stealth_client import EventType
from py_astealth.examples.example_lib import graceful_shutdown
from py_stealth.protocol import get_port


@graceful_shutdown
async def event_handler(client: AsyncStealthApiClient):
    await client.AddToSystemJournal("event handler started")
    while True:
        event = await client.events.get()
        print(event)


@graceful_shutdown
async def clicker(client: AsyncStealthApiClient):
    await client.AddToSystemJournal("clicker handler started")
    while True:
        # click every 2-5 seconds
        await asyncio.sleep(random.random()*3.0+2.0)
        # await client.FindTypeEx(0xFFFF, 0xFFFF, 0, True)
        # item = random.choice(await client.GetFindedList())
        item = await client.Self()
        await client.ClickOnObject(item)


async def main():
    client = AsyncStealthApiClient("127.0.0.1", get_port())
    try:
        await client.connect()
        await client.SetEventCallback(EventType.EvSpeech)

        _tasks = [
            asyncio.create_task(clicker(client)),
            asyncio.create_task(event_handler(client)),
        ]

        done, pending = await asyncio.wait(_tasks, return_when=asyncio.FIRST_COMPLETED)

        print(f"{len(done)} task(s) completed. Initiating shutdown...")

    except ConnectionRefusedError:
        print("Connection refused. Make sure Stealth client is running.")
    finally:
        if '_tasks' in locals():
            for task in _tasks:
                if not task.done():
                    task.cancel()

            # waiting complete task
            await asyncio.gather(*_tasks, return_exceptions=True)

        await client.ClearEventCallback(EventType.EvSpeech)
        client.close()

if __name__ == "__main__":
    asyncio.run(main())
