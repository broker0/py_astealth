import asyncio
from datetime import datetime
from py_astealth.api_client import AsyncStealthApiClient, SyncStealthApiClient
import py_stealth as old_stealth
from py_astealth import stealth as new_stealth
from py_astealth.core.context import DirectContext

COUNT = 15000


def log_stats(name: str, start_time: datetime):
    dt = datetime.now() - start_time
    total_ms = dt.total_seconds() * 1000
    avg_ms = total_ms / COUNT
    ops_sec = COUNT / dt.total_seconds() if dt.total_seconds() > 0 else 0

    print(f"| {name:<40} | {total_ms:>8.0f} ms | {avg_ms:>6.3f} ms/op | {ops_sec:>8.0f} ops/sec |")


def bench_sync(name: str, obj):
    start = datetime.now()
    func = obj.Self     # ! METHOD func
    for _ in range(COUNT):
        func()          # ! METHOD args
    log_stats(name, start)


async def bench_async(name: str):
    async with AsyncStealthApiClient() as client:
        method = client.Self       # ! METHOD func
        start = datetime.now()
        for _ in range(COUNT):
            await method()         # ! METHOD args

    log_stats(name, start)


def main():
    print(f"Starting Benchmark (Count={COUNT})\n")
    print("-" * 92)
    print(f"| {'BENCHMARK NAME':<40} | {'TOTAL':>11} | {'AVG':>12} | {'SPEED':>16} |")
    print("-" * 92)

    # 1. Classic py_stealth
    bench_sync("Classic sync module (py_stealth)", old_stealth)

    # 2. Modern sync wrapper (emulation)
    bench_sync("Modern sync module (emulate py_stealth)", new_stealth)

    # 3. Modern Sync Client (Threaded)
    with SyncStealthApiClient() as client_threaded:
        bench_sync("Modern Sync client (Threaded)", client_threaded)

    # 4. Modern Sync Client (Single Thread)
    with SyncStealthApiClient(DirectContext()) as client_fast:
        bench_sync("Modern Sync client (Single Thread)", client_fast)

    # 5. Async Client
    asyncio.run(bench_async("Modern Async client"))
    print("-" * 92)


if __name__ == "__main__":
    main()
