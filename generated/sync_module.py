###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from datetime import datetime



def AddToSystemJournal(Text: str) -> None: pass
def CharName() -> str: pass
def ClearEventCallback(EventIndex: int) -> None: pass
def ClickOnObject(ObjID: int) -> None: pass
def ConnectedTime() -> datetime: pass
def FindTypeEx(ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
def GetColor(ID: int) -> int: pass
def GetDirection(ID: int) -> int: pass
def GetFindedList() -> list[int]: pass
def GetGumpTextLines(GumpIndex: int) -> list[str]: pass
def GetLineTime() -> datetime: pass
def GetMultiAllParts(MultiID: int) -> list[MultiPart]: pass
def GetMultis() -> list[Multi]: pass
def GetName(ObjectID: int) -> str: pass
def GetNotoriety(ID: int) -> int: pass
def GetPathArray3D(StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
def GetStaticTilesArray(Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
def GetStealthInfo() -> AboutData: pass
def GetType(ID: int) -> int: pass
def GetX(ID: int) -> int: pass
def GetY(ID: int) -> int: pass
def GetZ(ID: int) -> int: pass
def Ignore(ID: int) -> None: pass
def IgnoreOff(ID: int) -> None: pass
def IgnoreReset() -> None: pass
def IsObjectExists(ID: int) -> bool: pass
def ObjAtLayerEx(Layer: int, ID: int) -> int: pass
def Self() -> int: pass
def SetEventCallback(EventIndex: int) -> None: pass
def SetFindDistance(Value: int) -> None: pass
def SetFindVertical(Value: int) -> None: pass
def Step(Direction: int, Running: bool) -> int: pass
def StepQ(Direction: int, Running: bool) -> int: pass
def WorldNum() -> int: pass