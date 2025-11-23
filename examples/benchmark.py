import asyncio
from datetime import datetime

from py_astealth.api_client import AsyncStealthApiClient, SyncStealthApiClient
import py_stealth as stealth

from py_astealth import stealth as nstealth

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
    client = AsyncStealthApiClient()
    await client.connect()

    start_time = datetime.now()
    for x in range(0, COUNT):
        await client.Self()
    time = datetime.now() - start_time
    ms = time.total_seconds() * 1000 + time.microseconds / 1000
    print(f"{COUNT} calls in {ms} milliseconds, {ms / COUNT} ms per call, {(COUNT / ms) * 1000} calls in one seconds")

    client.close()


def modern_sync_stealth():
    client = SyncStealthApiClient()
    client.connect()

    start_time = datetime.now()
    for x in range(0, COUNT):
        client.Self()
    time = datetime.now() - start_time
    ms = time.total_seconds() * 1000 + time.microseconds / 1000
    print(f"{COUNT} calls in {ms} milliseconds, {ms / COUNT} ms per call, {(COUNT / ms) * 1000} calls in one seconds")

    client.close()


def modern_fast_sync_stealth():
    client = SyncStealthApiClient(threaded=False)
    client.connect()

    start_time = datetime.now()
    for x in range(0, COUNT):
        client.Self()
    time = datetime.now() - start_time
    ms = time.total_seconds() * 1000 + time.microseconds / 1000
    print(f"{COUNT} calls in {ms} milliseconds, {ms / COUNT} ms per call, {(COUNT / ms) * 1000} calls in one seconds")

    client.close()


def modern_sync_in_classic():
    start_time = datetime.now()
    for x in range(0, COUNT):
        nstealth.Self()
    time = datetime.now() - start_time
    ms = time.total_seconds() * 1000 + time.microseconds / 1000
    print(f"{COUNT} calls in {ms} milliseconds, {ms / COUNT} ms per call, {(COUNT / ms) * 1000} calls in one seconds")


def main():
    print("======= Classic sync stealth benchmark =======")
    classic_sync_stealth()
    print("======= Modern sync stealth benchmark =======")
    modern_sync_stealth()
    print("======= Modern sync in classic interface benchmark =======")
    modern_sync_in_classic()
    print("======= Fast sync stealth benchmark =======")
    modern_fast_sync_stealth()
    print("======= Modern async stealth benchmark =======")
    asyncio.run(modern_async_stealth())


if __name__ == "__main__":
    main()
