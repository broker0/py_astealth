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
    session_per_profile = 10
    client_per_session = 15

    tasks = []

    # ** single session for all clients **
    # session = StealthSession()
    # await session.negotiate_port()

    for profile in profiles:
        # ** single session per profile **
        # session = StealthSession(profile=profile, script_name=f"profile#{profile}")
        # await session.negotiate_port()

        for session_n in range(session_per_profile):
            # ** (normal mode) single session for "session" **
            session = StealthSession(profile=profile, script_name=f"session#{session_n}")
            await session.negotiate_port()

            for client_n in range(client_per_session):
                # ** single session per client **
                # session = StealthSession(profile=profile, script_name=f"client#{client_n})
                # await session.negotiate_port()

                client = AsyncStealthApiClient(session=session)
                await client.connect()
                client_id = f"{await client.CharName()}#{client_n}#{session.script_port}"

                tasks.append(asyncio.create_task(client_task(client, client_id)))
                # await asyncio.sleep(0.1)

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
