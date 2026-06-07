"""Multi-run wrapper around benchmark.py: runs each row N times and reports
the per-row median (plus spread and the raw run values).

Edit `METHOD_NAME` to swap the benched method without touching the row code.
Single-run mode is still available via `benchmark.py`.
"""
import asyncio
from io import StringIO
import operator
import time
import statistics
import sys

from datetime import datetime

from py_astealth.async_client import AsyncStealthApiClient
from py_astealth.async_pool import AsyncClientPool
from py_astealth.stealth_session import StealthSession
from py_astealth.sync import SyncStealthApiClient
from py_astealth.sync import FastContext

import py_stealth as old_stealth
from py_astealth import stealth as new_stealth


# Tunables
DURATION = 15.0         # seconds per test
POOL_BATCH = 1000       # ops per batch for the async pool benchmark
RUNS = 3                # How many runs?
METHOD_NAME = "Self"    # any zero-arg method exposed by every backend

RUN_FILE_NAME = f"{datetime.now():%Y-%m-%d_%H-%M-%S}.log"
COPY_TO_CLIP = False
WRITE_TO_FILE = False

# benchmark name -> list of ops/sec values (one per run)
RESULTS: dict[str, list[float]] = {}

TXT_OUT = StringIO()


def _detect_event_loop() -> str:
    """Identify which asyncio event loop implementation is currently active.

    Reports what the global event loop policy returns from `new_event_loop()` —
    i.e. what `asyncio.run(...)`, `ThreadedContext`, and the async client all use.
    `FastContext` deliberately bypasses this and uses the stdlib loop class
    directly (see `py_astealth/sync/context.py`), so it is unaffected.
    """
    loop = asyncio.new_event_loop()
    try:
        mod = type(loop).__module__
        cls = type(loop).__name__
    finally:
        loop.close()
    if mod.startswith("winloop"):
        return f"winloop ({mod}.{cls})"
    if mod.startswith("uvloop"):
        return f"uvloop ({mod}.{cls})"
    return f"stdlib asyncio ({mod}.{cls})"


def log_stats(name: str, count: int, elapsed: float):
    total_ms = elapsed * 1000
    avg_ms = total_ms / count if count > 0 else 0
    ops_sec = count / elapsed if elapsed > 0 else 0

    RESULTS.setdefault(name, []).append(ops_sec)

    out_txt = f"| {name:<40} | {count:>10} | {avg_ms:>6.3f} ms/op | {ops_sec:>8.0f} ops/sec |\n"
    TXT_OUT.writelines([out_txt])

    print(out_txt, end="")


def bench_sync(name: str, obj):
    func = getattr(obj, METHOD_NAME)
    count = 0
    start = time.perf_counter()
    deadline = start + DURATION
    while time.perf_counter() < deadline:
        func()  # ! METHOD args
        count += 1
    elapsed = time.perf_counter() - start
    log_stats(name, count, elapsed)


async def bench_async(name: str):
    async with AsyncStealthApiClient() as client:
        method = getattr(client, METHOD_NAME)
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
        caller = operator.methodcaller(METHOD_NAME)
        count = 0
        start = time.perf_counter()
        deadline = start + DURATION
        while time.perf_counter() < deadline:
            await client_pool.run([caller] * POOL_BATCH, pipelining=16)
            count += POOL_BATCH
        elapsed = time.perf_counter() - start

    log_stats(name, count, elapsed)


def run_once(idx: int) -> None:
    line1 = f"\n=== Run {idx + 1}/{RUNS} (Duration={DURATION:g}s per test, Method={METHOD_NAME}) ===\n"
    line2 = "-" * 92 + "\n"
    line3 = f"| {'BENCHMARK NAME':<40} | {'COUNT':>10} | {'AVG':>12} | {'SPEED':>16} |\n"

    TXT_OUT.writelines ([line1, line2, line3, line2])

    print(line1, end="")
    print(line2, end="")
    print(line3, end="")
    print(line2, end="")

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

    TXT_OUT.writelines([line2])
    print(line2, end="")


def print_summary() -> None:
    width = 100

    line1 = f"\n=== Summary: median across {RUNS} runs (Method={METHOD_NAME}) ===\n"
    line2 = f"| {'BENCHMARK NAME':<40} | {'MEDIAN':>10} | {'SPREAD':>8} | {'RUNS (ops/sec)':<29} |\n"
    line_widht = "-" * width + "\n"

    TXT_OUT.writelines([line1, line_widht, line2, line_widht])
    print(line1, end="")
    print(line_widht, end="")
    print(line2, end="")
    print(line_widht, end="")

    for name, ops in RESULTS.items():
        med = statistics.median(ops)
        spread_pct = (max(ops) - min(ops)) / med * 100 if med else 0
        runs_str = "  ".join(f"{v:.0f}" for v in ops)

        line3 = f"| {name:<40} | {med:>8.0f}/s | {spread_pct:>7.1f}% | {runs_str:<29} |\n"

        TXT_OUT.writelines([line3])
        print(line3, end="")

    TXT_OUT.writelines([line_widht])
    print(line_widht, end="")

    line4 = "SPREAD = (max - min) / median x 100. A row with spread > ~15% is too noisy\n"
    line5 = "to draw conclusions from; either rerun or increase RUNS at the top of the file.\n"

    TXT_OUT.writelines([line4, line5])
    print(line4, end="")
    print(line5, end="")


def main() -> None:
    line1 = f"Multi-run benchmark (Duration={DURATION:g}s per test, Runs={RUNS}, Method={METHOD_NAME})\n"
    line2 = f"Event loop: {_detect_event_loop()}\n"

    TXT_OUT.writelines([line1, line2])
    print(line1, end="")
    print(line2, end="")

    for i in range(RUNS):
        run_once(i)
    print_summary()

    if COPY_TO_CLIP:
        if sys.platform == 'win32':
            import subprocess
            subprocess.run("clip", input=TXT_OUT.getvalue(), check=True, encoding="utf-8")

    if WRITE_TO_FILE:
        with open(RUN_FILE_NAME, "w") as f:
            f.write(TXT_OUT.getvalue())


if __name__ == "__main__":
    main()
