###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *


class SyncInterface:
    """base class defining the interface of StealthApi."""

    def AddToSystemJournal(self, text: str) -> None:
        raise NotImplementedError

    def CharName(self) -> str:
        raise NotImplementedError

    def ClearEventCallback(self, EventIndex: int) -> None:
        raise NotImplementedError

    def ClickOnObject(self, ObjID: int) -> None:
        raise NotImplementedError

    def FindTypeEx(self, ObjType: int, Color: int, Container: int, InSub: bool) -> int:
        raise NotImplementedError

    def GetDirection(self, ID: int) -> int:
        raise NotImplementedError

    def GetFindedList(self) -> list[int]:
        raise NotImplementedError

    def GetPathArray3D(self, StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]:
        raise NotImplementedError

    def GetSelfID(self) -> int:
        raise NotImplementedError

    def GetStaticTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]:
        raise NotImplementedError

    def SetEventCallback(self, EventIndex: int) -> None:
        raise NotImplementedError

    def Step(self, Direction: int, Running: bool) -> int:
        raise NotImplementedError

    def StepQ(self, Direction: int, Running: bool) -> int:
        raise NotImplementedError
