"""Multi-run wrapper around benchmark.py: runs each row N times and reports
the per-row median (plus spread and the raw run values).

Edit `METHOD_NAME` to swap the benched method without touching the row code.
Single-run mode is still available via `benchmark.py`.
"""
import asyncio
import operator
import os
import statistics
from datetime import datetime

from py_astealth.async_client import AsyncStealthApiClient
from py_astealth.async_pool import AsyncClientPool
from py_astealth.stealth_session import StealthSession
from py_astealth.sync import SyncStealthApiClient, FastContext

import py_stealth
from py_astealth import stealth as new_stealth

old_stealth = py_stealth


# Tunables
COUNT = 15000
RUNS = 3
METHOD_NAME = "Self"  # any zero-arg method


# benchmark name -> list of ops/sec values (one per run)
RESULTS: dict[str, list[float]] = {}


def _detect_timeout_mode() -> str:
    """Report the actual per-call RPC timeout state by probing a MethodSpec.

    Source-agnostic — the timeout could have been set via the env var
    `PY_ASTEALTH_NO_TIMEOUT=1` at import time OR via `set_per_call_timeout()`
    at runtime. Either way, what matters for the banner is what `call_method`
    will actually do, which is governed by `spec.timeout`.
    """
    from py_astealth.stealth_api import StealthApi

    sample = StealthApi.ProfileName.method_spec.timeout
    if sample is None:
        return "OFF -- hung Stealth server calls block indefinitely"
    return f"ON ({sample}s per call)"


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


def log_stats(name: str, start_time: datetime) -> None:
    dt = datetime.now() - start_time
    total_ms = dt.total_seconds() * 1000
    avg_ms = total_ms / COUNT
    ops_sec = COUNT / dt.total_seconds() if dt.total_seconds() > 0 else 0
    RESULTS.setdefault(name, []).append(ops_sec)
    print(f"| {name:<40} | {total_ms:>8.0f} ms | {avg_ms:>6.3f} ms/op | {ops_sec:>8.0f} ops/sec |")


def bench_sync(name: str, obj) -> None:
    start = datetime.now()
    func = getattr(obj, METHOD_NAME)
    for _ in range(COUNT):
        func()
    log_stats(name, start)


async def bench_async(name: str) -> None:
    async with AsyncStealthApiClient() as client:
        method = getattr(client, METHOD_NAME)
        start = datetime.now()
        for _ in range(COUNT):
            await method()
    log_stats(name, start)


async def bench_async_pool(name: str) -> None:
    async with AsyncClientPool(StealthSession(), size=16) as client_pool:
        caller = operator.methodcaller(METHOD_NAME)
        start = datetime.now()
        await client_pool.run([caller] * COUNT, pipelining=16)
    log_stats(name, start)


def run_once(idx: int) -> None:
    print(f"\n=== Run {idx + 1}/{RUNS} (Count={COUNT}, Method={METHOD_NAME}) ===")
    print("-" * 92)
    print(f"| {'BENCHMARK NAME':<40} | {'TOTAL':>11} | {'AVG':>12} | {'SPEED':>16} |")
    print("-" * 92)

    bench_sync("Classic sync module (py_stealth)", old_stealth)
    bench_sync("Modern sync module (emulate py_stealth)", new_stealth)

    with SyncStealthApiClient() as client_threaded:
        bench_sync("Modern Sync client (Threaded)", client_threaded)

    with SyncStealthApiClient(FastContext()) as client_fast:
        bench_sync("Modern Sync client (Single Thread)", client_fast)

    asyncio.run(bench_async("Modern Async client"))
    asyncio.run(bench_async_pool("Pool of Async clients"))

    print("-" * 92)


def print_summary() -> None:
    print(f"\n=== Summary: median across {RUNS} runs (Method={METHOD_NAME}) ===")
    width = 100
    print("-" * width)
    print(f"| {'BENCHMARK NAME':<40} | {'MEDIAN':>10} | {'SPREAD':>8} | {'RUNS (ops/sec)':<29} |")
    print("-" * width)
    for name, ops in RESULTS.items():
        med = statistics.median(ops)
        spread_pct = (max(ops) - min(ops)) / med * 100 if med else 0
        runs_str = "  ".join(f"{v:.0f}" for v in ops)
        print(f"| {name:<40} | {med:>8.0f}/s | {spread_pct:>7.1f}% | {runs_str:<29} |")
    print("-" * width)
    print("SPREAD = (max - min) / median x 100. A row with spread > ~15% is too noisy")
    print("to draw conclusions from; either rerun or increase RUNS at the top of the file.")


def main() -> None:
    print(f"Multi-run benchmark (Count={COUNT}, Runs={RUNS}, Method={METHOD_NAME})")
    print(f"Event loop: {_detect_event_loop()}")
    print(f"Timeouts:   {_detect_timeout_mode()}")
    for i in range(RUNS):
        run_once(i)
    print_summary()


if __name__ == "__main__":
    main()
