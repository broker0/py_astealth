###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from datetime import datetime


class SyncInterface:
    """base class defining the interface of StealthApi."""

    def AddToSystemJournal(self, text: str) -> None: pass
    def CharName(self) -> str: pass
    def ClearEventCallback(self, EventIndex: int) -> None: pass
    def ClickOnObject(self, ObjID: int) -> None: pass
    def ConnectedTime(self) -> datetime: pass
    def FindTypeEx(self, ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
    def GetDirection(self, ID: int) -> int: pass
    def GetFindedList(self) -> list[int]: pass
    def GetLineTime(self) -> RPCType: pass
    def GetPathArray3D(self, StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
    def GetSelfID(self) -> int: pass
    def GetStaticTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
    def SetEventCallback(self, EventIndex: int) -> None: pass
    def Step(self, Direction: int, Running: bool) -> int: pass
    def StepQ(self, Direction: int, Running: bool) -> int: pass