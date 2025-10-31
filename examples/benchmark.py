import asyncio
from datetime import datetime

from py_astealth.api_client import AsyncStealthApiClient, SyncStealthApiClient
from py_stealth.protocol import get_port
import py_stealth as stealth

# how many times will we call the method
COUNT = 5000


def classic_sync_stealth():
    start_time = datetime.now()
    for x in range(0, COUNT):
        stealth.Self()
    time = datetime.now() - start_time
    ms = time.total_seconds() * 1000 + time.microseconds / 1000
    print(f"{COUNT} calls in {ms} milliseconds, {ms / COUNT} ms per call, {(COUNT / ms) * 1000} calls in one seconds")


async def modern_async_stealth():
    client = AsyncStealthApiClient("127.0.0.1", get_port())
    await client.connect()

    start_time = datetime.now()
    for x in range(0, COUNT):
        await client.GetSelfID()
    time = datetime.now() - start_time
    ms = time.total_seconds() * 1000 + time.microseconds / 1000
    print(f"{COUNT} calls in {ms} milliseconds, {ms / COUNT} ms per call, {(COUNT / ms) * 1000} calls in one seconds")

    client.close()


def modern_sync_stealth():
    client = SyncStealthApiClient('127.0.0.1', get_port())
    client.connect()

    start_time = datetime.now()
    for x in range(0, COUNT):
        client.GetSelfID()
    time = datetime.now() - start_time
    ms = time.total_seconds() * 1000 + time.microseconds / 1000
    print(f"{COUNT} calls in {ms} milliseconds, {ms / COUNT} ms per call, {(COUNT / ms) * 1000} calls in one seconds")


def main():
    print("======= Classic sync stealth benchmark =======")
    classic_sync_stealth()
    print("======= Modern sync stealth benchmark =======")
    modern_sync_stealth()
    print("======= Modern async stealth benchmark =======")
    asyncio.run(modern_async_stealth())


if __name__ == "__main__":
    main()
