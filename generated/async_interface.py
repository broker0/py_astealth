###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *


class AsyncInterface:
    """base class defining the interface of StealthApi."""

    async def AddToSystemJournal(self, text: str) -> None:
        raise NotImplementedError

    async def CharName(self) -> str:
        raise NotImplementedError

    async def ClearEventCallback(self, EventIndex: int) -> None:
        raise NotImplementedError

    async def ClickOnObject(self, ObjID: int) -> None:
        raise NotImplementedError

    async def FindTypeEx(self, ObjType: int, Color: int, Container: int, InSub: bool) -> int:
        raise NotImplementedError

    async def GetDirection(self, ID: int) -> int:
        raise NotImplementedError

    async def GetFindedList(self) -> list[int]:
        raise NotImplementedError

    async def GetPathArray3D(self, StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]:
        raise NotImplementedError

    async def GetSelfID(self) -> int:
        raise NotImplementedError

    async def GetStaticTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]:
        raise NotImplementedError

    async def SetEventCallback(self, EventIndex: int) -> None:
        raise NotImplementedError

    async def Step(self, Direction: int, Running: bool) -> int:
        raise NotImplementedError

    async def StepQ(self, Direction: int, Running: bool) -> int:
        raise NotImplementedError
