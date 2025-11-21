import asyncio
import math
from py_astealth.api_client import AsyncStealthApiClient
from py_astealth.stealth_client import get_stealth_port
from py_astealth.stealth_structs import WorldPoint


class SharedState:
    def __init__(self):
        self.master_pos = None
        self.running = True
        self.updated_event = asyncio.Event()


async def get_position(client):
    return (await client.PredictedX(),
            await client.PredictedY(),
            await client.PredictedZ(),
            await client.PredictedDirection())


def calc_direction(Xfrom, Yfrom, Xto, Yto):
    dx = abs(Xto - Xfrom)
    dy = abs(Yto - Yfrom)
    if dx == dy == 0:
        return 100
    elif (dx / (dy + 0.1)) >= 2:
        return 6 if Xfrom > Xto else 2
    elif (dy / (dx + 0.1)) >= 2:
        return 0 if Yfrom > Yto else 4
    elif Xfrom > Xto:
        return 7 if Yfrom > Yto else 5
    elif Xfrom < Xto:
        return 1 if Yfrom > Yto else 3


async def track_master(client, state: SharedState):
    print("Tracker task started")
    while state.running:
        pos = await get_position(client)
        if pos != state.master_pos:
            state.master_pos = pos
            state.updated_event.set()
        await asyncio.sleep(10/1000)


async def control_slave(client, state: SharedState):
    print("Slave control task started")
    
    min_dist = 2
    run_flag = True
    
    while state.running:
        if not state.master_pos:
            await asyncio.sleep(100/1000)
            continue

        mx, my, mz, mdir = state.master_pos
        sx, sy, sz, sdir = await get_position(client)

        dist = max(abs(mx-sx), abs(my-sy))

        if dist <= min_dist:
            try:
                await asyncio.wait_for(state.updated_event.wait(), timeout=1.0)
                state.updated_event.clear()
            except asyncio.TimeoutError:
                pass

            continue

        world_num = await client.WorldNum()
        path = await client.GetPathArray3D(sx, sy, sz, mx, my, mz, world_num, 1, 1, run_flag)

        if not path:
            print("No path found!")
            await asyncio.sleep(1.0)
            continue

        if len(path) > 0:
            next_point = path[0]
            direction = calc_direction(sx, sy, next_point.x, next_point.y)

            result = await client.StepQ(direction, run_flag)
            # result = await client.Step(direction, run_flag)

        await asyncio.sleep(5/1000)


async def complex_follower(master, slave):
    state = SharedState()
    state.master_pos = await get_position(master)

    # Create tasks
    tracker = asyncio.create_task(track_master(master, state))
    controller = asyncio.create_task(control_slave(slave, state))

    print("Multifollower started. Press Ctrl+C to stop.")

    try:
        await asyncio.gather(tracker, controller)
    except asyncio.CancelledError:
        state.running = False
        print("Stopping...")


async def simple_follower(master, slave):
    path = []
    curr_pos = await get_position(master)
    run_flag = True

    while True:
        mx, my, mz, mdir = await get_position(master)
        sx, sy, sz, sdir = await get_position(slave)
        world_num = await master.WorldNum()

        if (mx, my, mz, mdir) != curr_pos:
            await slave.AddToSystemJournal(f"Master position updated {mx, my}")
            curr_pos = (mx, my, mz, mdir)
            # update path
            path = await slave.GetPathArray3D(sx, sy, sz, mx, my, mz, world_num, 1, 1, run_flag)

        if path:
            sx, sy, sz, sdir = await get_position(slave)
            next_point = path[0]
            dx, dy = sx-next_point.x, sy-next_point.y
            if abs(dx) < 2 and abs(dy) < 2 and abs(dx) + abs(dy) > 0:
                direction = calc_direction(sx, sy, next_point.x, next_point.y)
                await master.AddToSystemJournal(f"Slave move to {next_point.x}, {next_point.y}")
                result = await slave.Step(direction, run_flag)
                path.pop(0)
            else:
                await master.AddToSystemJournal(f"recalc path, because dx, dy=({dx}, {dy})")
                path = await slave.GetPathArray3D(sx, sy, sz, mx, my, mz, world_num, 1, 1, run_flag)

        await asyncio.sleep(1/1000)





async def main():
    print("Connecting to Master...")
    master = AsyncStealthApiClient(*get_stealth_port())
    await master.connect()
    print(f"Master connected. Profile: {await master.ProfileName()}")

    print("\n!!! Please switch to the SLAVE profile in Stealth now !!!")
    input("Press Enter when ready...")

    print("Connecting to Slave...")
    slave = AsyncStealthApiClient(*get_stealth_port())
    await slave.connect()
    print(f"Slave connected. Profile: {await slave.ProfileName()}")

    # await complex_follower(master, slave)
    await simple_follower(master, slave)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
