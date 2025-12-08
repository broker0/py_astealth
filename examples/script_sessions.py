import asyncio

from py_astealth.api_client import AsyncStealthApiClient
from py_astealth.examples.example_lib import graceful_shutdown
from py_astealth.stealth_session import StealthSession


@graceful_shutdown
async def client_task(client: AsyncStealthApiClient, task_id: str):
    await client.AddToSystemJournal(f"{task_id} task started")

    while True:
        await client.AddToSystemJournal(f"message from {task_id}")
        # delay = 1.0 + random.random()*2.0
        delay = 2.0
        await asyncio.sleep(delay)


async def main():
    # list of profiles
    profiles = ["(0)", "(1)", "(2)"]
    # script session for each profile
    sessions = [StealthSession(profile=profile) for profile in profiles]
    # connections per session
    connections = 5

    tasks = []
    for session in sessions:
        for i in range(connections):
            # all clients of one session = one "script" in stealth
            client = AsyncStealthApiClient(session=session)
            await client.connect()
            client_id = f"{await client.CharName()}#{i}"

            tasks.append(asyncio.create_task(client_task(client, client_id)))
            await asyncio.sleep(0.1)

    while True:
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        print(f"task complete {done}")
        for task in done:
            r = task.cancel()

        if pending:
            tasks = pending
        else:
            break

    await asyncio.gather(*pending, return_exceptions=False)


if __name__ == "__main__":
    asyncio.run(main())
