###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from datetime import datetime


class AsyncInterface:
    """base class defining the interface of StealthApi."""

    async def AddToSystemJournal(self, Text: str) -> None: pass
    async def CharName(self) -> str: pass
    async def ClearEventCallback(self, EventIndex: int) -> None: pass
    async def ClickOnObject(self, ObjID: int) -> None: pass
    async def ConnectedTime(self) -> datetime: pass
    async def FindTypeEx(self, ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
    async def GetColor(self, ID: int) -> int: pass
    async def GetDirection(self, ID: int) -> int: pass
    async def GetFindedList(self) -> list[int]: pass
    async def GetGumpTextLines(self, GumpIndex: int) -> list[str]: pass
    async def GetLineTime(self) -> datetime: pass
    async def GetMultiAllParts(self, MultiID: int) -> list[MultiPart]: pass
    async def GetMultis(self) -> list[Multi]: pass
    async def GetName(self, ObjectID: int) -> str: pass
    async def GetNotoriety(self, ID: int) -> int: pass
    async def GetPathArray3D(self, StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
    async def GetStaticTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
    async def GetStealthInfo(self) -> AboutData: pass
    async def GetType(self, ID: int) -> int: pass
    async def GetX(self, ID: int) -> int: pass
    async def GetY(self, ID: int) -> int: pass
    async def GetZ(self, ID: int) -> int: pass
    async def Ignore(self, ID: int) -> None: pass
    async def IgnoreOff(self, ID: int) -> None: pass
    async def IgnoreReset(self) -> None: pass
    async def IsObjectExists(self, ID: int) -> bool: pass
    async def ObjAtLayerEx(self, Layer: int, ID: int) -> int: pass
    async def Self(self) -> int: pass
    async def SetEventCallback(self, EventIndex: int) -> None: pass
    async def SetFindDistance(self, Value: int) -> None: pass
    async def SetFindVertical(self, Value: int) -> None: pass
    async def Step(self, Direction: int, Running: bool) -> int: pass
    async def StepQ(self, Direction: int, Running: bool) -> int: pass
    async def WorldNum(self) -> int: pass