from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import asyncio
from datetime import datetime, timedelta
import time

from py_astealth import AsyncClientPool, StealthSession

TIME = timedelta(seconds=5)
PROCESSES = 4
SESSIONS = 16
CLIENTS = 16
BATCH = 128
PIPELINING = 16


def process_task(tnum):
    async def async_loop():
        async def session(name):
            session_obj = StealthSession(script_name=name)
            end = datetime.now() + TIME

            requests_count = 0
            batches_count = 0
            total_batch_time = 0.0

            async with AsyncClientPool(session_obj, size=CLIENTS) as pool:
                while datetime.now() < end:
                    start_op = time.perf_counter()

                    # --- WORKLOAD ---
                    # await pool.run([lambda c: c.GetWorldItems() for _ in range(BATCH)], pipelining=PIPELINING)
                    await pool.run([lambda c: c.Self() for _ in range(BATCH)], pipelining=PIPELINING)
                    # --- WORKLOAD ---

                    op_duration = time.perf_counter() - start_op

                    total_batch_time += op_duration
                    requests_count += BATCH
                    batches_count += 1

                    if not batches_count % 25:
                        await pool[0].AddToSystemJournal(f'{name}: {batches_count} batches. Last batch: {op_duration:.4f}s')

            return requests_count, batches_count, total_batch_time

        tasks = [asyncio.create_task(session(f"T#{tnum}-S#{i}")) for i in range(SESSIONS)]
        results = await asyncio.gather(*tasks)

        t_reqs = sum(r[0] for r in results)
        t_batches = sum(r[1] for r in results)
        t_time = sum(r[2] for r in results)

        return t_reqs, t_batches, t_time

    return asyncio.run(async_loop())


if __name__ == '__main__':
    print(f"[Main] Config: Threads={PROCESSES}, Sessions={SESSIONS}, Clients={CLIENTS}, Batch={BATCH}")
    print(f"[Main] Planned Duration: {TIME.total_seconds()}s")
    print("[Main] Starting...")

    global_start = time.perf_counter()

    total_reqs = 0
    total_batches = 0
    sum_batch_times = 0.0

    with ProcessPoolExecutor(max_workers=PROCESSES) as executor:
        futures = [executor.submit(process_task, tnum) for tnum in range(PROCESSES)]

        for f in futures:
            r_reqs, r_batches, r_time = f.result()
            total_reqs += r_reqs
            total_batches += r_batches
            sum_batch_times += r_time

    global_end = time.perf_counter()

    total_duration = global_end - global_start
    rps = total_reqs / total_duration if total_duration > 0 else 0

    avg_batch_time = (sum_batch_times / total_batches) if total_batches > 0 else 0
    avg_req_time_ms = (avg_batch_time / BATCH) * 1000

    print("\n" + "=" * 40)
    print(f"DONE.")
    print(f"Total Wall Time  : {total_duration:.4f} sec")
    print(f"Total Requests   : {total_reqs:,}")
    print(f"Total Batches    : {total_batches:,}")
    print("-" * 40)
    print(f"RPS (Throughput) : {rps:,.2f} req/sec")
    print(f"Avg Batch Time   : {avg_batch_time:.4f} sec")
    print(f"Avg Request Latency: {avg_req_time_ms:.4f} ms")
    print("=" * 40)
