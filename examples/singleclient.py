import asyncio
from datetime import datetime

import py_stealth
import stealth
from py_astealth.api_client import AsyncStealthApiClient
from py_astealth.examples.example_lib import graceful_shutdown
from py_astealth.utilites.connection import get_stealth_port


class StealthBot(AsyncStealthApiClient):
    def __init__(self, host, port):
        super().__init__(host, port)
        self._tasks = []

    @graceful_shutdown
    async def periodic_clicker(self):
        self_id = await self.Self()
        while True:
            await self.AddToSystemJournal(f"[*] Click on {self_id}")
            await self.ClickOnObject(self_id)
            await asyncio.sleep(2)

    @graceful_shutdown
    async def periodic_log(self):
        counter = 1
        while True:
            await self.AddToSystemJournal(f"[*] wait 3 seconds... {counter}")
            counter += 1
            await asyncio.sleep(3)

    @graceful_shutdown
    async def mover(self):
        self_id = await self.Self()
        current_dir = await self.GetDirection(self_id)
        for step in range(1, 11):
            await asyncio.sleep(1)
            t = datetime.now()
            step_res = await self.StepQ(current_dir, True)
            await self.AddToSystemJournal(f"Step {step} - {step_res} {datetime.now()-t}")
            if step_res < 0:
                await self.AddToSystemJournal(f"Cannot do step, stopping")
                break

    async def run(self):
        self._tasks = [
            asyncio.create_task(self.periodic_clicker()),
            asyncio.create_task(self.periodic_log()),
            asyncio.create_task(self.mover())
        ]

        done, pending = await asyncio.wait(self._tasks, return_when=asyncio.FIRST_COMPLETED)

        print(f"{len(done)} task(s) completed. Initiating shutdown...")

        for task in self._tasks:
            if not task.done():
                task.cancel()

        if self._tasks:
            await asyncio.gather(*self._tasks, return_exceptions=True)


async def main():
    bot = StealthBot(*get_stealth_port())
    await bot.connect()
    await bot.run()
    bot.close()


if __name__ == "__main__":
    asyncio.run(main())
