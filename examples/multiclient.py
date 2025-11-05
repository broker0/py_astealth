import asyncio
from datetime import datetime

from py_astealth.api_client import AsyncStealthApiClient
from py_astealth.examples.example_lib import graceful_shutdown
from py_stealth.protocol import get_port


@graceful_shutdown
async def find_long_path(client: AsyncStealthApiClient):
    await client.AddToSystemJournal("[+] Pathfinding in progress")
    t1 = datetime.now()
    path = await client.GetPathArray3D(
        656, 1344, 0,
        1374, 1808, 0,
        0,
        1, 1,
        True
    )
    await client.AddToSystemJournal(f"[+] Pathfinding completed in {datetime.now() - t1}.")
    return path


@graceful_shutdown
async def periodic_clicker(client: AsyncStealthApiClient):
    await client.AddToSystemJournal("Clicker started")

    self_id = await client.Self()
    while True:
        await client.AddToSystemJournal(f"[*] Click on {self_id}")
        await client.ClickOnObject(self_id)
        await asyncio.sleep(1)


async def main():
    client1 = AsyncStealthApiClient("127.0.0.1", get_port())
    await client1.connect()
    client2 = AsyncStealthApiClient("127.0.0.1", get_port())
    await client2.connect()

    # create tasks
    path_task = asyncio.create_task(find_long_path(client1))
    clicker_task = asyncio.create_task(periodic_clicker(client2))

    # wait first task completion
    tasks = {path_task, clicker_task}
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    if path_task in done:
        try:
            path_result = path_task.result()
            print(f"Path length: {len(path_result) if path_result else 0} steps.")
        except Exception as e:
            print(f"[!] Pathfinding exception: {e}")

    # cancel all pending tasks (clicker_task)
    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)

    client1.close()
    client2.close()


if __name__ == "__main__":
    asyncio.run(main())
