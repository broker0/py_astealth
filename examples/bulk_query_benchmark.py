import asyncio
from datetime import datetime
from typing import Callable

from py_astealth import AsyncStealthApiClient
from py_astealth.stealth_structs import WorldItemData


async def query_simple(client: AsyncStealthApiClient):
    await client.FindTypeEx(0xFFFF, 0xFFFF, 0x00000000, False)
    serials = await client.GetFindedList()
    # return serials

    result = []
    for serial in serials:
        if await client.IsNPC(serial) or await client.IsHouse(serial):
            continue

        result.append(WorldItemData(
            serial,
            await client.GetType(serial),
            await client.GetColor(serial),
            await client.GetX(serial),
            await client.GetY(serial),
            await client.GetZ(serial),
            await client.WorldNum(),
            await client.GetQuantity(serial),
            await client.IsMovable(serial)
        ))

    return result


async def query_bulk(client: AsyncStealthApiClient):
    return await client.GetWorldItems()


async def test_methods(client: AsyncStealthApiClient):
    self_id = await client.Self()
    backpack_id = await client.Backpack()

    print(await client.GetMobile(self_id))
    print(await client.GetMobiles())
    backpack_content = await client.GetContent(backpack_id)
    print(len(backpack_content), backpack_content)

    equipment = await client.GetEquipment(self_id)
    print(len(equipment), equipment)


async def main():
    async with AsyncStealthApiClient() as client:
        # await test_methods(client)

        await client.SetFindDistance(50)
        await client.SetFindVertical(250)

        COUNT = 500

        # time = datetime.now()
        # for _ in range(COUNT):
        #     res = await query_simple(client)
        #
        # time = datetime.now() - time
        # time_ms = time.total_seconds() * 1000
        # print(len(res))
        # print(f"simple query: {time_ms:>8.1f}, avg {time_ms/COUNT:>8.4f}")

        time = datetime.now()
        for _ in range(COUNT):
            res = await query_bulk(client)

        time = datetime.now() - time
        time_ms = time.total_seconds() * 1000
        print(len(res))
        print(f"bulk query: {time_ms:>8.1f}, avg {time_ms/COUNT:>8.4f}")


def profile_proc(c: Callable):
    import cProfile as profile
    import pstats
    from pstats import SortKey

    pr = profile.Profile()
    pr.enable()

    c()

    pr.disable()
    # Back in outer section of code
    pr.dump_stats('profile.pstat')

    p = pstats.Stats('profile.pstat')
    p.sort_stats(SortKey.TIME).print_stats()


if __name__ == "__main__":

    # profile_proc(lambda: asyncio.run(main()))
    for _ in range(10):
        asyncio.run(main())


