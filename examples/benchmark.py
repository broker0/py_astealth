import asyncio
import time

from py_astealth.async_client import AsyncStealthApiClient
from py_astealth.async_pool import AsyncClientPool
from py_astealth.stealth_session import StealthSession
from py_astealth.sync import SyncStealthApiClient
from py_astealth.sync import FastContext

import py_stealth as old_stealth
from py_astealth import stealth as new_stealth


DURATION = 15.0          # seconds per test
POOL_BATCH = 1000       # ops per batch for the async pool benchmark


def log_stats(name: str, count: int, elapsed: float):
    total_ms = elapsed * 1000
    avg_ms = total_ms / count if count > 0 else 0
    ops_sec = count / elapsed if elapsed > 0 else 0

    print(f"| {name:<40} | {count:>10} | {avg_ms:>6.3f} ms/op | {ops_sec:>8.0f} ops/sec |")


def bench_sync(name: str, obj):
    func = obj.Self     # ! METHOD func
    count = 0
    start = time.perf_counter()
    deadline = start + DURATION
    while time.perf_counter() < deadline:
        func()          # ! METHOD args
        count += 1
    elapsed = time.perf_counter() - start
    log_stats(name, count, elapsed)


async def bench_async(name: str):
    async with AsyncStealthApiClient() as client:
        method = client.Self       # ! METHOD func
        count = 0
        start = time.perf_counter()
        deadline = start + DURATION
        while time.perf_counter() < deadline:
            await method()         # ! METHOD args
            count += 1
        elapsed = time.perf_counter() - start

    log_stats(name, count, elapsed)


async def bench_async_pool(name: str):
    async with AsyncClientPool(StealthSession(), size=16) as client_pool:
        count = 0
        start = time.perf_counter()
        deadline = start + DURATION
        while time.perf_counter() < deadline:
            await client_pool.run([lambda c: c.Self() for _ in range(POOL_BATCH)], pipelining=16)
            count += POOL_BATCH
        elapsed = time.perf_counter() - start

    log_stats(name, count, elapsed)


def main():
    print(f"Starting Benchmark (Duration={DURATION:g}s per test)\n")
    print("-" * 92)
    print(f"| {'BENCHMARK NAME':<40} | {'COUNT':>10} | {'AVG':>12} | {'SPEED':>16} |")
    print("-" * 92)

    # 1. Classic py_stealth
    bench_sync("Classic sync module (py_stealth)", old_stealth)

    # 2. Modern sync wrapper (emulation)
    bench_sync("Modern sync module (emulate py_stealth)", new_stealth)

    # 3. Modern Sync Client (Threaded)
    with SyncStealthApiClient() as client_threaded:
        bench_sync("Modern Sync client (Threaded)", client_threaded)

    # 4. Modern Sync Client (Single Thread)
    with SyncStealthApiClient(FastContext()) as client_fast:
        bench_sync("Modern Sync client (Single Thread)", client_fast)

    # 5. Async Client
    asyncio.run(bench_async("Modern Async client"))

    # 6. Async pool of clients
    asyncio.run(bench_async_pool("Pool of Async clients"))

    print("-" * 92)


if __name__ == "__main__":
    main()
