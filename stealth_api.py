from py_astealth.core.api_specification import ApiSpecification
from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *


# TODO declare all other Stealth api methods
class StealthApi(ApiSpecification):
    """
    Declarative API description using decorators.
    The key is the method signatures with a detailed description of the argument types and the return type.
    Methods do not have to have an implementation, they are just a protocol specification.
    """

    @ApiSpecification.method(7)
    def SetEventCallback(self, EventIndex: U8) -> None:
        pass

    @ApiSpecification.method(8)
    def ClearEventCallback(self, EventIndex: U8) -> None:
        pass

    @ApiSpecification.method(14)
    def Self(self) -> U32:
        pass

    @ApiSpecification.method(233)
    def ObjAtLayerEx(self, Layer: U8, ID: U32) -> U32:
        pass

    @ApiSpecification.method(151)
    def GetType(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(159)
    def GetColor(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(169)
    def GetNotoriety(self, ID: U32) -> U8:
        pass

    @ApiSpecification.method(104)
    def ClickOnObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(19)
    def CharName(self) -> String:
        pass

    @ApiSpecification.method(147)
    def GetName(ObjectID: U32) -> String:
        pass

    @ApiSpecification.method(13)
    def AddToSystemJournal(self, Text: String) -> None:
        pass

    @ApiSpecification.method(127)
    def SetFindDistance(self, Value: U32) -> None:
        pass

    @ApiSpecification.method(129)
    def SetFindVertical(self, Value: U32) -> None:
        pass

    @ApiSpecification.method(155)
    def IsObjectExists(self, ID: U32) -> Bool:
        pass

    @ApiSpecification.method(131)
    def FindTypeEx(self, ObjType: U16, Color: U16, Container: U32, InSub: Bool) -> U32:
        pass

    @ApiSpecification.method(138)
    def GetFindedList(self) -> list[U32]:
        pass

    @ApiSpecification.method(134)
    def Ignore(self, ID: U32) -> None:
        pass

    @ApiSpecification.method(135)
    def IgnoreOff(self, ID: U32) -> None:
        pass

    @ApiSpecification.method(136)
    def IgnoreReset(self) -> None:
        pass

    @ApiSpecification.method(286)
    def GetStaticTilesArray(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: list[U16]) -> list[FoundTile]:
        pass

    @ApiSpecification.method(335)
    def GetPathArray3D(self,
                       StartX: U16, StartY: U16, StartZ: I8,
                       FinishX: U16, FinishY: U16, FinishZ: I8,
                       WorldNum: U8,
                       AccuracyXY: I32, AccuracyZ: I32,
                       Run: Bool) -> list[WorldPoint]:
        pass

    @ApiSpecification.method(324)
    def Step(self, Direction: U8, Running: Bool) -> U8:
        pass

    @ApiSpecification.method(325)
    def StepQ(self, Direction: U8, Running: Bool) -> I32:
        pass

    @ApiSpecification.method(15)
    def GetX(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(16)
    def GetY(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(17)
    def GetZ(self, ID: U32) -> I8:
        pass

    @ApiSpecification.method(18)
    def WorldNum(self) -> U8:
        pass

    @ApiSpecification.method(157)
    def GetDirection(self, ID: U32) -> U8:
        pass

    @ApiSpecification.method(108)
    def GetLineTime(self) -> DateTime:
        pass

    @ApiSpecification.method(39)
    def ConnectedTime(self) -> DateTime:
        pass

    @ApiSpecification.method(381)
    def GetMultiAllParts(self, MultiID: U32) -> list[MultiPart]:
        pass

    @ApiSpecification.method(347)
    def GetMultis(self) -> list[Multi]:
        pass

    @ApiSpecification.method(387)
    def GetStealthInfo(self) -> AboutData:
        pass

    @ApiSpecification.method(225)
    def GetGumpTextLines(self, GumpIndex: U16) -> list[String]:
        pass
