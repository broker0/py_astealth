###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from datetime import datetime


class AsyncInterface:
    """base class defining the interface of StealthApi."""

    async def AddToSystemJournal(self, text: str) -> None: pass
    async def CharName(self) -> str: pass
    async def ClearEventCallback(self, EventIndex: int) -> None: pass
    async def ClickOnObject(self, ObjID: int) -> None: pass
    async def ConnectedTime(self) -> datetime: pass
    async def FindTypeEx(self, ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
    async def GetDirection(self, ID: int) -> int: pass
    async def GetFindedList(self) -> list[int]: pass
    async def GetGumpTextLines(self, GumpIndex: int) -> list[str]: pass
    async def GetLineTime(self) -> datetime: pass
    async def GetMultiAllParts(self, MultiID: int) -> list[MultiPart]: pass
    async def GetMultis(self) -> list[Multi]: pass
    async def GetPathArray3D(self, StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
    async def GetSelfID(self) -> int: pass
    async def GetStaticTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
    async def GetStealthInfo(self) -> AboutData: pass
    async def SetEventCallback(self, EventIndex: int) -> None: pass
    async def Step(self, Direction: int, Running: bool) -> int: pass
    async def StepQ(self, Direction: int, Running: bool) -> int: pass