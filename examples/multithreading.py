import threading
import time
from concurrent.futures import ThreadPoolExecutor

from py_astealth.sync import SyncStealthApiClient
from py_astealth.sync import ThreadedContext
from py_astealth.stealth_session import StealthSession

# Event to stop periodic workers gracefully
STOP_WORKERS = threading.Event()


def periodic_worker(client: SyncStealthApiClient, name: str):
    thread_name = threading.current_thread().name
    print(f"[{name}] Starting periodic loop on '{thread_name}'")

    try:
        client.connect()
        while not STOP_WORKERS.is_set():
            # Perform periodic task
            client.AddToSystemJournal(f"[{name}] Alive at {time.strftime('%H:%M:%S')}")

            # Wait for next tick (e.g. 1 second)
            time.sleep(1.0)

    except Exception as e:
        print(f"[{name}] Error: {e}")
    finally:
        print(f"[{name}] Stopping.")
        client.close()


def main():
    ctx_periodic = ThreadedContext("CTX_Periodic")

    workers = []
    for i in range(5):
        session = StealthSession(script_name=f"session#{i}")  # new session for client
        client = SyncStealthApiClient(session=session, context=ctx_periodic)
        workers.append((client, f"Worker_{i}"))

    with ThreadPoolExecutor(max_workers=10) as executor:
        # Start Periodic Workers
        print("[Main] Starting periodic workers...")
        worker_futures = [executor.submit(periodic_worker, c, n) for c, n in workers]

        # Let them run for a bit
        time.sleep(10)

        # Stop Workers
        print("[Main] Signaling workers to stop...")
        STOP_WORKERS.set()

        # Wait for workers to finish
        for f in worker_futures:
            f.result()

    print("\n[Main] Cleanup contexts...")
    ctx_periodic.stop()
    print("[Main] All done.")


if __name__ == "__main__":
    main()
