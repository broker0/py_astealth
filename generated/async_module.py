###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from datetime import datetime



async def AddToSystemJournal(Text: str) -> None: pass
async def CharName() -> str: pass
async def ClearEventCallback(EventIndex: int) -> None: pass
async def ClickOnObject(ObjID: int) -> None: pass
async def ConnectedTime() -> datetime: pass
async def FindTypeEx(ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
async def GetColor(ID: int) -> int: pass
async def GetDirection(ID: int) -> int: pass
async def GetFindedList() -> list[int]: pass
async def GetGumpTextLines(GumpIndex: int) -> list[str]: pass
async def GetLineTime() -> datetime: pass
async def GetMultiAllParts(MultiID: int) -> list[MultiPart]: pass
async def GetMultis() -> list[Multi]: pass
async def GetName(ObjectID: int) -> str: pass
async def GetNotoriety(ID: int) -> int: pass
async def GetPathArray3D(StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
async def GetStaticTilesArray(Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
async def GetStealthInfo() -> AboutData: pass
async def GetType(ID: int) -> int: pass
async def GetX(ID: int) -> int: pass
async def GetY(ID: int) -> int: pass
async def GetZ(ID: int) -> int: pass
async def Ignore(ID: int) -> None: pass
async def IgnoreOff(ID: int) -> None: pass
async def IgnoreReset() -> None: pass
async def IsObjectExists(ID: int) -> bool: pass
async def ObjAtLayerEx(Layer: int, ID: int) -> int: pass
async def Self() -> int: pass
async def SetEventCallback(EventIndex: int) -> None: pass
async def SetFindDistance(Value: int) -> None: pass
async def SetFindVertical(Value: int) -> None: pass
async def Step(Direction: int, Running: bool) -> int: pass
async def StepQ(Direction: int, Running: bool) -> int: pass
async def WorldNum() -> int: pass