"""
Example: Parallel Data Collection using Multiple Async Clients

This example demonstrates how to collect object information in parallel
by distributing the work across multiple async clients. Each client
handles a portion of the found objects, collecting type/color/x/y/z data.

A pool of clients is created upfront and reused for all operations.
"""

import asyncio
import time

from dataclasses import dataclass
from typing import List

from py_astealth import AsyncClientPool, StealthSession, AsyncStealthApiClient


@dataclass
class ObjectInfo:
    """Information about a single game object."""
    obj_id: int
    obj_type: int
    color: int
    x: int
    y: int
    z: int


# use for imitation of heavy work
REPEAT_CALL = 1


async def get_object_info_simple(client: AsyncStealthApiClient, obj_id: int) -> ObjectInfo:
    """simple version of get_object_info"""
    for _ in range(REPEAT_CALL):
        obj_type = await client.GetType(obj_id)
        color = await client.GetColor(obj_id)
        x = await client.GetX(obj_id)
        y = await client.GetY(obj_id)
        z = await client.GetZ(obj_id)

    return ObjectInfo(obj_id, obj_type, color, x, y, z)


async def get_object_info_concurrent(client: AsyncStealthApiClient, obj_id):
    """concurrent version of get_object_info"""
    for _ in range(REPEAT_CALL):
        obj_type, color, x, y, z = await asyncio.gather(
            client.GetType(obj_id),
            client.GetColor(obj_id),
            client.GetX(obj_id),
            client.GetY(obj_id),
            client.GetZ(obj_id)
        )

    return ObjectInfo(obj_id, obj_type, color, x, y, z)


async def collect_objects_list_info(client: AsyncStealthApiClient, obj_ids: List[int]) -> List[ObjectInfo]:
    result = []
    for obj_id in obj_ids:
        result.append(await get_object_info_simple(client, obj_id))

    return result


async def benchmark():
    """Compare single vs parallel collection performance."""
    session = StealthSession()
    
    # Create pool with maximum clients we'll test
    max_clients = 32
    async with AsyncClientPool(session, size=max_clients) as pool:
        # Use first client from pool to find objects
        finder = pool[0]
        await finder.SetFindDistance(100)
        await finder.SetFindVertical(100)

        await finder.FindTypeEx(0xFFFF, 0xFFFF, 0, True)
        found_ids = await finder.GetFindedList()
        
        if not found_ids:
            print("No objects found for benchmark!")
            return
        
        print(f"Benchmarking Single client with {len(found_ids)} objects...\n")

        # 1. Single client (using pool[0]), sync mode, item by item
        start = time.perf_counter()
        single_result = await collect_objects_list_info(pool[0], found_ids)
        single_time = time.perf_counter() - start
        print(f"Single client plain for:   {single_time:.3f}s for {len(single_result)} objects")

        # 1. Single client (using pool[0]), list comprehension mode
        start = time.perf_counter()
        single_result = [await get_object_info_simple(pool[0], obj_id) for obj_id in found_ids]
        single_time = time.perf_counter() - start
        print(f"Single client list simp:   {single_time:.3f}s for {len(single_result)} objects")

        # 1. Single client (using pool[0]), list comprehension mode
        start = time.perf_counter()
        single_result = [await get_object_info_concurrent(pool[0], obj_id) for obj_id in found_ids]
        single_time = time.perf_counter() - start
        print(f"Single client list conc:   {single_time:.3f}s for {len(single_result)} objects")

        print(f"\nBenchmarking Pool with {len(found_ids)} objects...")
        
        # test with full pool
        start = time.perf_counter()
        parallel_results = await pool.run(found_ids, processor=get_object_info_simple, pipelining=16)
        parallel_time = time.perf_counter() - start
        print(f"Pool Run ({pool.size} clients) simp: {parallel_time:.3f}s, speedup: {single_time / parallel_time:.2f}x")

        start = time.perf_counter()
        parallel_results = await pool.run(found_ids, processor=get_object_info_concurrent, pipelining=16)
        parallel_time = time.perf_counter() - start
        print(f"Pool Run ({pool.size} clients) conc: {parallel_time:.3f}s, speedup: {single_time / parallel_time:.2f}x")


if __name__ == "__main__":
    asyncio.run(benchmark())
