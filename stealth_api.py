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

    ####################################################################################################################
    # connection management
    ####################################################################################################################
    @ApiSpecification.method(12)
    def Connected(self) -> Bool:
        pass

    @ApiSpecification.method(21)
    def GetARStatus(self) -> Bool:
        pass

    @ApiSpecification.method(22)
    def SetARStatus(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(354)
    def SetARExtParams(self, ShardName: String = '', CharName: String = '', UseAtEveryConnect: Bool = False) -> None:
        pass

    @ApiSpecification.method(38)
    def ConnectedTime(self) -> DateTime:
        pass

    @ApiSpecification.method(39)
    def DisconnectedTime(self) -> DateTime:
        pass

    @ApiSpecification.method(45)
    def Connect(self) -> None:
        pass

    @ApiSpecification.method(46)
    def Disconnect(self) -> None:
        pass


    ####################################################################################################################
    # events
    ####################################################################################################################
    @ApiSpecification.method(7)
    def SetEventCallback(self, EventIndex: U8) -> None:
        pass

    @ApiSpecification.method(8)
    def ClearEventCallback(self, EventIndex: U8) -> None:
        pass

    ####################################################################################################################
    # profile management
    ####################################################################################################################
    @ApiSpecification.method(11)
    def ProfileName(self) -> String:
        pass

    @ApiSpecification.method(20)
    def ChangeProfile(self, Name: String) -> int:
        pass

    @ApiSpecification.method(343)
    def ProfileShardName(self) -> String:
        pass

    @ApiSpecification.method(352)
    def ExtChangeProfile(self, ProfileName: String, ShardName: String = '', CharName: String = '') -> int:
        pass

    ####################################################################################################################
    # stealth info
    ####################################################################################################################
    @ApiSpecification.method(387)
    def GetStealthInfo(self) -> AboutData:
        pass

    @ApiSpecification.method(305)
    def StealthPath(self) -> String:
        pass

    @ApiSpecification.method(306)
    def StealthProfilePath(self) -> String:
        pass

    ####################################################################################################################
    # main information
    ####################################################################################################################
    @ApiSpecification.method(307)
    def ShardPath(self) -> String:
        pass

    @ApiSpecification.method(341)
    def GameServerIPString(self) -> String:
        pass


    @ApiSpecification.method(14)
    def Self(self) -> U32:
        pass

    @ApiSpecification.method(18)
    def WorldNum(self) -> U8:
        pass

    @ApiSpecification.method(19)
    def CharName(self) -> String:
        pass


    @ApiSpecification.method(48)
    def Backpack(self) -> U32:
        pass

    @ApiSpecification.method(143)
    def PredictedX(self) -> U16:
        pass

    @ApiSpecification.method(144)
    def PredictedY(self) -> U16:
        pass

    @ApiSpecification.method(145)
    def PredictedZ(self) -> U8:
        pass

    @ApiSpecification.method(146)
    def PredictedDirection(self) -> U8:
        pass

    @ApiSpecification.method(25)
    def Sex(self) -> U8:
        pass

    @ApiSpecification.method(26)
    def CharTitle(self) -> String:
        pass

    @ApiSpecification.method(27)
    def Gold(self) -> U32:
        pass

    @ApiSpecification.method(28)
    def Armor(self) -> I16:
        pass

    @ApiSpecification.method(29)
    def Weight(self) -> U16:
        pass

    @ApiSpecification.method(30)
    def MaxWeight(self) -> U16:
        pass

    @ApiSpecification.method(31)
    def Race(self) -> U8:
        pass

    @ApiSpecification.method(32)
    def PetsMax(self) -> U8:
        pass

    @ApiSpecification.method(33)
    def PetsCurrent(self) -> U8:
        pass

    @ApiSpecification.method(34)
    def FireResist(self) -> U16:
        pass

    @ApiSpecification.method(35)
    def ColdResist(self) -> U16:
        pass

    @ApiSpecification.method(36)
    def PoisonResist(self) -> U16:
        pass

    @ApiSpecification.method(37)
    def EnergyResist(self) -> U16:
        pass

    @ApiSpecification.method(47)
    def ShardName(self) -> String:
        pass

    @ApiSpecification.method(52)
    def Life(self) -> int:
        pass

    @ApiSpecification.method(55)
    def MaxLife(self) -> int:
        pass

    @ApiSpecification.method(58)
    def Luck(self) -> int:
        pass

    @ApiSpecification.method(59)
    def GetExtInfo(self) -> ExtendedInfo:
        pass

    @ApiSpecification.method(63)
    def Hidden(self) -> Bool:
        pass

    @ApiSpecification.method(64)
    def Poisoned(self) -> Bool:
        pass

    @ApiSpecification.method(65)
    def Paralyzed(self) -> Bool:
        pass

    @ApiSpecification.method(66)
    def Dead(self) -> Bool:
        pass



    ####################################################################################################################
    # object information
    ####################################################################################################################
    @ApiSpecification.method(155)
    def IsObjectExists(self, ID: U32) -> Bool:
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

    @ApiSpecification.method(157)
    def GetDirection(self, ID: U32) -> U8:
        pass

    @ApiSpecification.method(158)
    def GetDistance(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(151)
    def GetType(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(159)
    def GetColor(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(154)
    def GetQuantity(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(156)
    def GetPrice(self, ObjID: U32) -> U32:
        pass

    @ApiSpecification.method(147)
    def GetName(ObjID: U32) -> String:
        pass

    @ApiSpecification.method(148)
    def GetAltName(self, ObjID: U32) -> String:
        pass

    @ApiSpecification.method(149)
    def GetTitle(self, ObjID: U32) -> String:
        pass

    @ApiSpecification.method(169)
    def GetNotoriety(self, ID: U32) -> U8:
        pass

    @ApiSpecification.method(160)
    def GetStr(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(161)
    def GetInt(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(162)
    def GetDex(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(163)
    def GetHP(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(164)
    def GetMaxHP(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(165)
    def GetMana(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(166)
    def GetMaxMana(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(167)
    def GetStam(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(168)
    def GetMaxStam(self, ObjID: U32) -> int:
        pass

    @ApiSpecification.method(170)
    def GetParent(self, ObjID: U32) -> U32:
        pass

    @ApiSpecification.method(171)
    def IsWarMode(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(172)
    def IsNPC(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(173)
    def IsDead(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(174)
    def IsRunning(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(175)
    def IsContainer(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(176)
    def IsHidden(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(177)
    def IsMovable(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(178)
    def IsYellowHits(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(179)
    def IsPoisoned(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(180)
    def IsParalyzed(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(181)
    def IsFemale(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(233)
    def ObjAtLayerEx(self, Layer: U8, ID: U32) -> U32:
        pass

    @ApiSpecification.method(234)
    def GetLayer(self, ObjID: U32) -> U8:
        pass

    @ApiSpecification.method(253)
    def MobileCanBeRenamed(self, MobID: U32) -> Bool:
        pass

    @ApiSpecification.method(382)
    def IsHouse(self, ObjID: U32) -> Bool:
        pass

    ####################################################################################################################
    # past information
    ####################################################################################################################
    @ApiSpecification.method(40)
    def LastContainer(self) -> U32:
        pass

    @ApiSpecification.method(41)
    def LastTarget(self) -> U32:
        pass

    @ApiSpecification.method(42)
    def LastAttack(self) -> U32:
        pass

    @ApiSpecification.method(43)
    def LastStatus(self) -> U32:
        pass

    @ApiSpecification.method(44)
    def LastObject(self) -> U32:
        pass



    ####################################################################################################################
    # journal
    ####################################################################################################################
    @ApiSpecification.method(13)
    def AddToSystemJournal(self, Text: String) -> None:
        pass

    @ApiSpecification.method(346)
    def ClearSystemJournal(self) -> None:
        pass

    @ApiSpecification.method(115)
    def AddJournalIgnore(self, Str: String) -> None:
        pass

    @ApiSpecification.method(116)
    def ClearJournalIgnore(self) -> None:
        pass

    @ApiSpecification.method(117)
    def AddChatUserIgnore(self, Mobile: String) -> None:
        pass

    @ApiSpecification.method(118)
    def ClearChatUserIgnore(self) -> None:
        pass

    @ApiSpecification.method(119)
    def ClearJournal(self) -> None:
        pass

    @ApiSpecification.method(120)
    def LastJournalMessage(self) -> String:
        pass

    @ApiSpecification.method(121)
    def InJournal(self, Str: String) -> I32:
        pass

    @ApiSpecification.method(122)
    def InJournalBetweenTimes(self, Str: String, TimeBegin: DateTime, TimeEnd: DateTime) -> int:
        pass

    @ApiSpecification.method(123)
    def Journal(self, StringIndex: I32) -> String:
        pass

    @ApiSpecification.method(124)
    def SetJournalLine(self, StringIndex: I32, Text: String) -> None:
        pass

    @ApiSpecification.method(125)
    def LowJournal(self) -> I32:
        pass

    @ApiSpecification.method(126)
    def HighJournal(self) -> I32:
        pass

    @ApiSpecification.method(304)
    def AddToJournal(self, Text: String) -> None:
        pass

    @ApiSpecification.method(105)
    def FoundedParamID(self) -> int:
        pass

    @ApiSpecification.method(106)
    def LineID(self) -> U32:
        pass

    @ApiSpecification.method(107)
    def LineType(self) -> U16:
        pass

    @ApiSpecification.method(108)
    def GetLineTime(self) -> DateTime:
        pass

    @ApiSpecification.method(108)
    def LineTime(self) -> DateTime:
        pass

    @ApiSpecification.method(109)
    def LineMsgType(self) -> U8:
        pass

    @ApiSpecification.method(110)
    def LineTextColor(self) -> U16:
        pass

    @ApiSpecification.method(111)
    def LineTextFont(self) -> U16:
        pass

    @ApiSpecification.method(112)
    def LineIndex(self) -> int:
        pass

    @ApiSpecification.method(113)
    def LineCount(self) -> int:
        pass

    @ApiSpecification.method(114)
    def LineName(self) -> String:
        pass

    ####################################################################################################################
    # actions
    ####################################################################################################################
    @ApiSpecification.method(69)
    def Attack(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(101)
    def UseObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(102)
    def UseType(self, ObjType: U16, Color: U16) -> U32:
        pass

    @ApiSpecification.method(103)
    def UseFromGround(self, ObjType: U16, Color: U16) -> U32:
        pass

    @ApiSpecification.method(104)
    def ClickOnObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(88)
    def ToggleFly(self) -> None:
        pass

    @ApiSpecification.method(96)
    def Cast(self, SpellID: I32) -> None:
        pass

    @ApiSpecification.method(182)
    def OpenDoor(self) -> None:
        pass

    @ApiSpecification.method(183)
    def Bow(self) -> None:
        pass

    @ApiSpecification.method(184)
    def Salute(self) -> None:
        pass

    @ApiSpecification.method(252)
    def RenameMobile(self, MobID: U32, NewName: String) -> None:
        pass

    @ApiSpecification.method(308)
    def UOSay(self, Text: String) -> None:
        pass

    @ApiSpecification.method(309)
    def UOSayColor(self, Text: String, Color: U16) -> None:
        pass

    @ApiSpecification.method(359)
    def UseItemOnMobile(self, ItemSerial: U32, TargetSerial: U32) -> None:
        pass

    @ApiSpecification.method(360)
    def BandageSelf(self) -> None:
        pass

    ####################################################################################################################
    # skills related functions
    ####################################################################################################################
    @ApiSpecification.method(90)
    def UseSkill(self, SkillID: I32) -> None:
        pass

    @ApiSpecification.method(91)
    def SetSkillLockState(self, SkillName: String, skillState: U8) -> None:
        pass

    @ApiSpecification.method(92)
    def GetSkillCap(self, SkillName: String) -> F64:
        pass

    @ApiSpecification.method(93)
    def GetSkillValue(self, SkillName: String) -> F64:
        pass

    @ApiSpecification.method(351)
    def GetSkillCurrentValue(self, SkillName: String) -> F64:
        pass

    @ApiSpecification.method(369)
    def GetSkillLockState(self, SkillName: String) -> U8:
        pass

    ####################################################################################################################
    # search and all that
    ####################################################################################################################
    @ApiSpecification.method(127)
    def SetFindDistance(self, Value: U32) -> None: pass
    @ApiSpecification.method(128)
    def GetFindDistance(self) -> U32: pass
    @ApiSpecification.method(129)
    def SetFindVertical(self, Value: U32) -> None: pass
    @ApiSpecification.method(130)
    def GetFindVertical(self) -> U32: pass
    @ApiSpecification.method(131)
    def FindTypeEx(self, ObjType: U16, Color: U16, Container: U32, InSub: Bool) -> U32: pass
    @ApiSpecification.method(340)
    def FindTypesArrayEx(self, ObjTypes: list[U16], Colors: list[U16], Containers: list[U32], InSub: Bool) -> U32: pass
    @ApiSpecification.method(132)
    def FindNotoriety(self, ObjType: U16, Notoriety: U8) -> U32: pass
    @ApiSpecification.method(138)
    def GetFindedList(self) -> list[U32]: pass
    @ApiSpecification.method(134)
    def Ignore(self, ID: U32) -> None: pass
    @ApiSpecification.method(135)
    def IgnoreOff(self, ID: U32) -> None: pass
    @ApiSpecification.method(136)
    def IgnoreReset(self) -> None: pass
    @ApiSpecification.method(137)
    def GetIgnoreList(self) -> list[U32]: pass
    @ApiSpecification.method(133)
    def FindAtCoord(self, X: U16, Y: U16) -> U32: pass
    @ApiSpecification.method(139)
    def FindItem(self) -> U32: pass
    @ApiSpecification.method(140)
    def FindCount(self) -> int: pass
    @ApiSpecification.method(141)
    def FindQuantity(self) -> int: pass
    @ApiSpecification.method(142)
    def FindFullQuantity(self) -> int: pass

    ####################################################################################################################
    # multis
    ####################################################################################################################
    @ApiSpecification.method(380)
    def GetMultiPartsAtPosition(self, X: U16, Y: U16) -> list[MultiPart]:
        pass

    @ApiSpecification.method(381)
    def GetMultiAllParts(self, MultiID: U32) -> list[MultiPart]:
        pass

    @ApiSpecification.method(347)
    def GetMultis(self) -> list[Multi]:
        pass

    ####################################################################################################################
    # movement
    ####################################################################################################################
    @ApiSpecification.method(316)
    def SetRunUnmountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(317)
    def SetWalkMountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(318)
    def SetRunMountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(319)
    def SetWalkUnmountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(320)
    def GetRunMountTimer(self) -> U16:
        pass

    @ApiSpecification.method(321)
    def GetWalkMountTimer(self) -> U16:
        pass

    @ApiSpecification.method(322)
    def GetRunUnmountTimer(self) -> U16:
        pass

    @ApiSpecification.method(323)
    def GetWalkUnmountTimer(self) -> U16:
        pass

    @ApiSpecification.method(324)
    def Step(self, Direction: U8, Running: Bool) -> U8:
        pass

    @ApiSpecification.method(325)
    def StepQ(self, Direction: U8, Running: Bool) -> I32:
        pass

    @ApiSpecification.method(326)
    def MoveXYZ(self, Xdst: U16, Ydst: U16, Zdst: I16, AccuracyXY: I32, AccuracyZ: I32, Running: Bool) -> Bool:
        pass

    @ApiSpecification.method(327)
    def MoveXY(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32, Running: Bool) -> Bool:
        pass

    @ApiSpecification.method(353)
    def MoverStop(self) -> None:
        pass

    ####################################################################################################################
    # pathfinding, los
    ####################################################################################################################

    @ApiSpecification.method(285)
    def IsWorldCellPassable(self, CurrX: U16, CurrY: U16, CurrZ: I16, DestX: U16, DestY: U16, DestZ: I16, WorldNum: U8) -> Bool:
        pass

    @ApiSpecification.method(333)
    def CheckLOS(self, Xfrom: U16, Yfrom: U16, Zfrom: I16, Xto: I32, Yto: I32, Zto: I16, WorldNum: U8) -> Bool:
        pass

    @ApiSpecification.method(334)
    def GetPathArray(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32) -> list[WorldPoint]:
        pass

    @ApiSpecification.method(335)
    def GetPathArray3D(self,
                       StartX: U16, StartY: U16, StartZ: I8,
                       FinishX: U16, FinishY: U16, FinishZ: I8,
                       WorldNum: U8,
                       AccuracyXY: I32, AccuracyZ: I32,
                       Run: Bool) -> list[WorldPoint]:
        pass


    @ApiSpecification.method(366)
    def GetNextStepZ(self, CurrX: U16, CurrY: U16, DestX: U16, DestY: U16, WorldNum: U8, CurrZ: I16) -> I8:
        pass

    @ApiSpecification.method(328)
    def SetBadLocation(self, X: U16, Y: U16) -> None:
        pass

    @ApiSpecification.method(329)
    def SetGoodLocation(self, X: U16, Y: U16) -> None:
        pass

    @ApiSpecification.method(330)
    def ClearBadLocationList(self) -> None:
        pass

    @ApiSpecification.method(331)
    def SetBadObject(self, ObjType: U16, Color: U16, Radius: U8) -> None:
        pass

    @ApiSpecification.method(332)
    def ClearBadObjectList(self) -> None:
        pass


    ####################################################################################################################
    # map, statics
    ####################################################################################################################
    @ApiSpecification.method(286)
    def GetStaticTilesArray(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: list[U16]) -> list[FoundTile]:
        pass

    @ApiSpecification.method(287)
    def GetLandTilesArray(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileType: list[U16]) -> list[FoundTile]:
        pass

    @ApiSpecification.method(278)
    def GetTileFlags(self, Group: U8, Tile: U16) -> U32:
        pass

    @ApiSpecification.method(280)
    def GetLandTileData(self, Tile: U16) -> LandTileData:
        pass

    @ApiSpecification.method(281)
    def GetStaticTileData(self, Tile: U16) -> StaticTileData:
        pass

    @ApiSpecification.method(282)
    def GetLayerCount(self, x: U16, y: U16, WorldNum: U8) -> U8:
        pass

    @ApiSpecification.method(283)
    def ReadStaticsXY(self, X: U16, Y: U16, WorldNum: U8) -> list[StaticItemRealXY]:
        pass

    @ApiSpecification.method(284)
    def GetSurfaceZ(self, X: U16, Y: U16, WorldNum: U8) -> U8:
        pass

    @ApiSpecification.method(388)
    def GetCell(self, X: U16, Y: U16, WorldNum: U8) -> MapCell:
        pass

    ####################################################################################################################
    # gumps
    ####################################################################################################################
    @ApiSpecification.method(211)
    def WaitGump(self, Value: String) -> None:
        pass

    @ApiSpecification.method(213)
    def GumpAutoTextEntry(self, TextEntryID: I32, Value: String) -> None:
        pass

    @ApiSpecification.method(214)
    def GumpAutoRadiobutton(self, RadiobuttonID: I32, Value: I32) -> None:
        pass

    @ApiSpecification.method(215)
    def GumpAutoCheckBox(self, CheckBoxID: I32, Value: I32) -> None:
        pass

    @ApiSpecification.method(216)
    def NumGumpButton(self, GumpIndex: U16, Value: I32) -> Bool:
        pass

    @ApiSpecification.method(217)
    def NumGumpTextEntry(self, GumpIndex: U16, TextEntryID: I32, Value: String) -> Bool:
        pass

    @ApiSpecification.method(218)
    def NumGumpRadiobutton(self, GumpIndex: U16, RadiobuttonID: I32, Value: I32) -> Bool:
        pass

    @ApiSpecification.method(219)
    def NumGumpCheckBox(self, GumpIndex: U16, CBID: I32, Value: I32) -> Bool:
        pass

    @ApiSpecification.method(220)
    def GetGumpsCount(self) -> U32:
        pass

    @ApiSpecification.method(221)
    def CloseSimpleGump(self, GumpIndex: U16) -> None:
        pass

    @ApiSpecification.method(222)
    def GetGumpSerial(self, GumpIndex: U16) -> U32:
        pass

    @ApiSpecification.method(223)
    def GetGumpID(self, GumpIndex: U16) -> U32:
        pass

    @ApiSpecification.method(224)
    def IsGumpCanBeClosed(self, GumpIndex: U16) -> Bool:
        pass

    @ApiSpecification.method(225)
    def GetGumpTextLines(self, GumpIndex: U16) -> list[String]: pass


    @ApiSpecification.method(226)
    def GetGumpFullLines(self, GumpIndex: U16) -> list[String]:
        pass

    @ApiSpecification.method(227)
    def GetGumpShortLines(self, GumpIndex: U16) -> list[String]:
        pass

    @ApiSpecification.method(228)
    def GetGumpButtonsDescription(self, GumpIndex: U16) -> list[String]:
        pass

    @ApiSpecification.method(229)
    def GetGumpInfo(self, GumpIndex: U16) -> GumpInfo:
        pass

    @ApiSpecification.method(230)
    def AddGumpIgnoreByID(self, ID: U32) -> None:
        pass

    @ApiSpecification.method(231)
    def AddGumpIgnoreBySerial(self, Serial: U32) -> None:
        pass

    @ApiSpecification.method(232)
    def ClearGumpsIgnore(self) -> None:
        pass


    ####################################################################################################################
    # menu
    ####################################################################################################################
    @ApiSpecification.method(205)
    def WaitMenu(self, MenuCaption: String, ElementCaption: String) -> None:
        pass

    @ApiSpecification.method(206)
    def AutoMenu(self, MenuCaption: String, ElementCaption: String) -> None:
        pass

    @ApiSpecification.method(207)
    def MenuHookPresent(self) -> Bool:
        pass

    @ApiSpecification.method(208)
    def MenuPresent(self) -> Bool:
        pass

    @ApiSpecification.method(209)
    def CancelMenu(self) -> None:
        pass

    @ApiSpecification.method(210)
    def CloseMenu(self) -> None:
        pass

    @ApiSpecification.method(338)
    def GetMenuItems(self, Caption: String) -> list[String]:
        pass

    @ApiSpecification.method(339)
    def GetLastMenuItems(self) -> list[String]:
        pass

    @ApiSpecification.method(358)
    def GetMenuItemsEx(self, Caption: String) -> list[MenuItem]:
        pass

    ####################################################################################################################
    # context menu
    ####################################################################################################################
    @ApiSpecification.method(193)
    def RequestContextMenu(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(194)
    def SetContextMenuHook(self, MenuID: U32, EntryNumber: U8) -> None:
        pass

    @ApiSpecification.method(195)
    def GetContextMenu(self) -> list[String]:
        pass

    @ApiSpecification.method(196)
    def ClearContextMenu(self) -> None:
        pass

    ####################################################################################################################
    # scripts management
    ####################################################################################################################
    @ApiSpecification.method(4)
    def PauseResumeScript(self, ScriptIndex: U16) -> None:
        pass

    @ApiSpecification.method(450)
    def GetScriptsCount(self) -> U16:
        pass

    @ApiSpecification.method(451)
    def GetScriptPath(self, ScriptIndex: U16) -> String:
        pass

    @ApiSpecification.method(452)
    def GetScriptState(self, ScriptIndex: U16) -> U8:
        pass

    @ApiSpecification.method(453)
    def StartScript(self, ScriptPath: String) -> U16:
        pass

    @ApiSpecification.method(454)
    def StopScript(self, ScriptIndex: U16) -> None:
        pass

    @ApiSpecification.method(456)
    def StopAllScripts(self) -> None:
        pass

    @ApiSpecification.method(457)
    def SetScriptName(self, ScriptIndex: U16, Value: String) -> None:
        pass

    @ApiSpecification.method(458)
    def GetScriptName(self, ScriptIndex: U16) -> String:
        pass

    @ApiSpecification.method(23)
    def GetPauseScriptOnDisconnectStatus(self) -> Bool:
        pass

    @ApiSpecification.method(24)
    def SetPauseScriptOnDisconnectStatus(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(460)
    def GetScriptsList(self) -> list[ScriptInfo]:
        pass
    #
    ####################################################################################################################
    # map drawing
    ####################################################################################################################
    @ApiSpecification.method(550)
    def AddFigure(self, figure: MapFigure) -> U32:
        pass

    @ApiSpecification.method(551)
    def RemoveFigure(self, FigureID: U32) -> Bool:
        pass

    @ApiSpecification.method(552)
    def UpdateFigure(self, FigureID: U32, figure: MapFigure) -> Bool:
        pass

    @ApiSpecification.method(553)
    def ClearFigures(self) -> None:
        pass

    ####################################################################################################################
    # books management
    ####################################################################################################################
    @ApiSpecification.method(373)
    def BookGetPageText(self, Page: U16) -> String:
        pass

    @ApiSpecification.method(374)
    def BookSetText(self, Text: String) -> None:
        pass

    @ApiSpecification.method(375)
    def BookSetPageText(self, Page: U16, Text: String) -> None:
        pass

    @ApiSpecification.method(376)
    def BookClearText(self) -> None:
        pass

    @ApiSpecification.method(377)
    def BookSetHeader(self, Title: String, Author: String) -> None:
        pass

    ####################################################################################################################
    # party related functions
    ####################################################################################################################
    @ApiSpecification.method(262)
    def InviteToParty(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(263)
    def RemoveFromParty(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(264)
    def PartyPrivateMessageTo(self, ObjID: U32, Msg: String) -> None:
        pass

    @ApiSpecification.method(265)
    def PartySay(self, Msg: String) -> None:
        pass

    @ApiSpecification.method(266)
    def PartyCanLootMe(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(267)
    def PartyAcceptInvite(self) -> None:
        pass

    @ApiSpecification.method(268)
    def PartyDeclineInvite(self) -> None:
        pass

    @ApiSpecification.method(269)
    def PartyLeave(self) -> None:
        pass

    @ApiSpecification.method(270)
    def PartyMembersList(self) -> list[U32]:
        pass

    @ApiSpecification.method(271)
    def InParty(self) -> Bool:
        pass

    ####################################################################################################################
    # targets
    ####################################################################################################################
    @ApiSpecification.method(72)
    def TargetID(self) -> U32:
        pass

    @ApiSpecification.method(73)
    def CancelTarget(self) -> None:
        pass

    @ApiSpecification.method(74)
    def TargetToObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(75)
    def TargetToXYZ(self, X: U16, Y: U16, Z: I16) -> None:
        pass

    @ApiSpecification.method(76)
    def TargetToTile(self, Tile: U16, X: U16, Y: U16, Z: I16) -> None:
        pass

    @ApiSpecification.method(77)
    def WaitTargetObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(78)
    def WaitTargetTile(self, Tile: U16, X: U16, Y: U16, Z: I16) -> None:
        pass

    @ApiSpecification.method(79)
    def WaitTargetXYZ(self, X: U16, Y: U16, Z: I16) -> None:
        pass

    @ApiSpecification.method(80)
    def WaitTargetSelf(self) -> None:
        pass

    @ApiSpecification.method(81)
    def WaitTargetType(self, ObjType: U16) -> None:
        pass

    @ApiSpecification.method(82)
    def CancelWaitTarget(self) -> None:
        pass

    @ApiSpecification.method(83)
    def WaitTargetGround(self, ObjType: U16) -> None:
        pass

    @ApiSpecification.method(84)
    def WaitTargetLast(self) -> None:
        pass

    @ApiSpecification.method(389)
    def TargetByResource(self, ObjID: U32, Resource: U16) -> None:
        pass


    ####################################################################################################################
    # item manipulations
    ####################################################################################################################
    @ApiSpecification.method(191)
    def DragItem(self, ObjID: U32, Count: I32) -> Bool:
        pass

    @ApiSpecification.method(192)
    def DropItem(self, MoveIntoID: U32, X: I32, Y: I32, Z: I32) -> Bool:
        pass

    @ApiSpecification.method(235)
    def WearItem(self, Layer: U8, ObjID: U32) -> Bool:
        pass

    ####################################################################################################################
    # trade
    ####################################################################################################################
    @ApiSpecification.method(197)
    def IsTrade(self) -> Bool:
        pass

    @ApiSpecification.method(198)
    def GetTradeContainer(self, TradeNum: U8, Num: U8) -> U32:
        pass

    @ApiSpecification.method(199)
    def GetTradeOpponent(self, TradeNum: U8) -> U32:
        pass

    @ApiSpecification.method(200)
    def TradeCount(self) -> U8:
        pass

    @ApiSpecification.method(201)
    def GetTradeOpponentName(self, TradeNum: U8) -> String:
        pass

    @ApiSpecification.method(202)
    def TradeCheck(self, TradeNum: U8, Num: U8) -> Bool:
        pass

    @ApiSpecification.method(203)
    def ConfirmTrade(self, TradeNum: U8) -> None:
        pass

    @ApiSpecification.method(204)
    def CancelTrade(self, TradeNum: U8) -> Bool:
        pass

    ####################################################################################################################
    # buy/sell
    ####################################################################################################################
    @ApiSpecification.method(240)
    def AutoBuy(self, ItemType: U16, ItemColor: U16, Quantity: U16) -> None:
        pass

    @ApiSpecification.method(241)
    def GetShopList(self) -> list[String]:
        pass

    @ApiSpecification.method(242)
    def ClearShopList(self) -> None:
        pass

    @ApiSpecification.method(243)
    def AutoBuyEx(self, ItemType: U16, ItemColor: U16, Quantity: U16, Price: U32, Name: String) -> None:
        pass

    @ApiSpecification.method(244)
    def GetAutoBuyDelay(self) -> U16:
        pass

    @ApiSpecification.method(245)
    def SetAutoBuyDelay(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(246)
    def GetAutoSellDelay(self) -> U16:
        pass

    @ApiSpecification.method(247)
    def SetAutoSellDelay(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(248)
    def AutoSell(self, ItemType: U16, ItemColor: U16, Quantity: U16) -> None:
        pass

    ####################################################################################################################
    # global chat
    ####################################################################################################################
    @ApiSpecification.method(361)
    def GlobalChatJoinChannel(self, ChName: String) -> None:
        pass

    @ApiSpecification.method(362)
    def GlobalChatLeaveChannel(self) -> None:
        pass

    @ApiSpecification.method(363)
    def GlobalChatSendMsg(self, MsgText: String) -> None:
        pass

    @ApiSpecification.method(364)
    def GlobalChatActiveChannel(self) -> String:
        pass

    @ApiSpecification.method(365)
    def GlobalChatChannelsList(self) -> list[String]:
        pass

    ####################################################################################################################
    # proxy related
    ####################################################################################################################
    @ApiSpecification.method(60)
    def ProxyIP(self) -> String:
        pass

    @ApiSpecification.method(61)
    def ProxyPort(self) -> U16:
        pass

    @ApiSpecification.method(62)
    def UseProxy(self) -> Bool:
        pass

    ####################################################################################################################
    # client interaction
    ####################################################################################################################
    @ApiSpecification.method(289)
    def ClientPrint(self, Text: String) -> None:
        pass

    @ApiSpecification.method(290)
    def ClientPrintEx(self, SenderID: U32, Color: U16, Font: U16, Text: String) -> None:
        pass

    @ApiSpecification.method(291)
    def CloseClientUIWindow(self, UIWindowType: U8, ID: U32) -> None:
        pass

    @ApiSpecification.method(292)
    def ClientRequestObjectTarget(self) -> None:
        pass

    @ApiSpecification.method(293)
    def ClientRequestTileTarget(self) -> None:
        pass

    @ApiSpecification.method(294)
    def ClientTargetResponsePresent(self) -> Bool:
        pass

    @ApiSpecification.method(295)
    def ClientTargetResponse(self) -> TargetInfo:
        pass

    @ApiSpecification.method(342)
    def CloseClientGump(self, ID: U32) -> None:
        pass

    @ApiSpecification.method(368)
    def ClientHide(self, ObjID: U32) -> Bool:
        pass

    ####################################################################################################################
    # UserStatic functions
    ####################################################################################################################
    @ApiSpecification.method(383)
    def AddUserStatic(self, StaticItem: UserStaticItem, WorldNum: U8) -> int:
        pass

    @ApiSpecification.method(384)
    def RemoveUserStatic(self, ID: I32) -> Bool:
        pass

    @ApiSpecification.method(385)
    def ClearUserStatics(self) -> None:
        pass

    ####################################################################################################################
    # abilities functions
    ####################################################################################################################
    @ApiSpecification.method(85)
    def UsePrimaryAbility(self) -> None:
        pass

    @ApiSpecification.method(86)
    def UseSecondaryAbility(self) -> None:
        pass

    @ApiSpecification.method(87)
    def GetActiveAbility(self) -> String:
        pass

    @ApiSpecification.method(98)
    def IsActiveSpellAbility(self, SpellName: String) -> Bool:
        pass


    ####################################################################################################################
    # http functions
    ####################################################################################################################
    @ApiSpecification.method(258)
    def HTTP_Get(self, URL: String) -> None:
        pass

    @ApiSpecification.method(259)
    def HTTP_Post(self, URL: String, PostData: String) -> String:
        pass

    @ApiSpecification.method(260)
    def HTTP_Body(self) -> String:
        pass

    @ApiSpecification.method(261)
    def HTTP_Header(self) -> String:
        pass

    ####################################################################################################################
    # war functions
    ####################################################################################################################
    @ApiSpecification.method(67)
    def WarTargetID(self) -> U32:
        pass

    @ApiSpecification.method(68)
    def SetWarMode(self, Value: Bool) -> None:
        pass


    ####################################################################################################################
    # unclassified functions
    ####################################################################################################################
    @ApiSpecification.method(70)
    def UseSelfPaperdollScroll(self) -> None:
        pass

    @ApiSpecification.method(71)
    def UseOtherPaperdollScroll(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(94)
    def ReqVirtuesGump(self) -> None:
        pass

    @ApiSpecification.method(95)
    def UseVirtue(self, VirtueName: String) -> None:
        pass

    @ApiSpecification.method(99)
    def SetCatchBag(self, ObjID: U32) -> U8:
        pass

    @ApiSpecification.method(100)
    def UnsetCatchBag(self) -> None:
        pass


    #########################################
    #########################################
    # Autogenerated signatures, not checked #
    #########################################
    #########################################

    @ApiSpecification.method(152)
    def GetTooltipRec(self, ObjID: U32) -> list[ClilocRec]:
        pass

    @ApiSpecification.method(153)
    def GetClilocByID(self, ClilocID: U32) -> String:
        pass

    @ApiSpecification.method(212)
    def WaitTextEntry(self, Value: String) -> None:
        pass

    @ApiSpecification.method(233)
    def ObjAtLayerEx(self, LayerType: U8, PlayerID: U32) -> U32:
        pass

    @ApiSpecification.method(238)
    def SetDress(self) -> None:
        pass

    @ApiSpecification.method(249)
    def RequestStats(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(250)
    def HelpRequest(self) -> None:
        pass

    @ApiSpecification.method(251)
    def QuestRequest(self) -> None:
        pass

    @ApiSpecification.method(254)
    def SetStatState(self, statNum: U8, statState: U8) -> None:
        pass

    @ApiSpecification.method(372)
    def GetStatLockState(self, statNum: U8) -> U8:
        pass

    # @ApiSpecification.method(255)
    # def GetStaticArt(self, ObjType: U32, Hue: U16) -> ???:
    #     pass

    # @ApiSpecification.method(256)
    # def PrintScriptMethodsList(self, FileName: String = ', SortedList: Boolean = False) -> None:
    #     pass

    @ApiSpecification.method(300)
    def GetQuestArrow(self) -> Point:
        pass

    @ApiSpecification.method(301)
    def SetSilentMode(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(303)
    def FillInfoWindow(self, s: String) -> None:
        pass

    @ApiSpecification.method(310)
    def SetGlobal(self, GlobalRegion: String, VarName: String, VarValue: String) -> None:
        pass

    @ApiSpecification.method(311)
    def GetGlobal(self, GlobalRegion: String, VarName: String) -> String:
        pass

    @ApiSpecification.method(312)
    def ConsoleEntryReply(self, Text: String) -> None:
        pass

    @ApiSpecification.method(313)
    def ConsoleEntryUnicodeReply(self, Text: String) -> None:
        pass

    @ApiSpecification.method(348)
    def ClearInfoWindow(self) -> None:
        pass

    @ApiSpecification.method(349)
    def GetBuffBarInfo(self) -> list[BuffBarInfo]:
        pass

    @ApiSpecification.method(350)
    def ConvertIntegerToFlags(self, Group: U8, Flags: U32) -> list[String]:
        pass


    @ApiSpecification.method(367)
    def DumpObjectsCache(self) -> None:
        pass

    @ApiSpecification.method(370)
    def EquipLastWeapon(self) -> None:
        pass

    @ApiSpecification.method(390)
    def GetPlayerStatusText(self, ObjID: U32) -> String:
        pass

    #############################
    # Invalid method_id block
    #############################

    # @ApiSpecification.method(999)
    # def WaitJournalLine(self, StartTime: TDateTime, Str: String, MaxWaitTimeMS: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def WaitJournalLineSystem(self, StartTime: TDateTime, Str: String, MaxWaitTimeMS: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def CurrentScriptPath(self) -> String:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def FillNewWindow(self, s: String) -> None:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Ground(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def WarMode(self) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def TargetPresent(self) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def WaitForTarget(self, MaxWaitTimeMS: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def CastToObject(self, SpellName: String, ObjID: U32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def FindType(self, ObjType: U16, Container: U32) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GetFindedList(self, UserList: TStringList) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GetCliloc(self, ObjID: U32) -> String:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GetTooltip(self, ObjID: U32) -> String:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def MoveItem(self, ObjID: U32, Count: I32, MoveIntoID: U32, X: I32, Y: I32, Z: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Grab(self, ObjID: U32, Count: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Drop(self, ObjID: U32, Count: I32, X: I32, Y: I32, Z: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def DropHere(self, ItemID: U32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def MoveItems(self, Container: U32, ItemsType: U16, ItemsColor: U16, MoveIntoID: U32, X: I32, Y: I32, Z: I32, DelayMS: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def MoveItemsEx(self, Container: U32, ItemsType: U16, ItemsColor: U16, MoveIntoID: U32, X: I32, Y: I32, Z: I32, DelayMS: I32, MaxItems: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def CancelAllMenuHooks(self) -> None:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def IsGump(self) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Disarm(self) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Equip(self, Layer: U8, ObjID: U32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Equipt(self, Layer: U8, ObjType: U16) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Unequip(self, Layer: U8) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Undress(self) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def DressSavedSet(self) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def EquipDressSet(self) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def Count(self, ObjType: U16) -> int:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def CountGround(self, ObjType: U16) -> int:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def CountEx(self, ObjType: U16, Color: U16, Container: U32) -> int:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def BP(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def BM(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GA(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GS(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def MR(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def NS(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def SA(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def SS(self) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def BPCount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def BMCount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GACount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GSCount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def MRCount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def NSCount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def SACount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def SSCount(self) -> U32:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GetLandTilesArrayEx(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: array of Word, LandTilesArray: TFoundTilesArray) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GetLandTilesArrayEx(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: array of Word) -> ???:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GetStaticTilesArrayEx(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: array of Word, FoundTilesArray: TFoundTilesArray) -> U16:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def GetStaticTilesArrayEx(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: array of Word) -> ???:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def CheckLag(self, timeoutMS: I32) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def CalcDir(self, Xfrom: U16, Yfrom: U16, Xto: U16, Yto: U16) -> U8:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def newMoveXY(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32, Running: Bool) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def newMoveXY(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32, Running: Bool, StepCallback: TMoverStepCallBack = nil) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def EmptyContainer(self, Container: U32, DestContainer: U32, DelayMS: U16) -> Bool:
    #     pass
    #
    # @ApiSpecification.method(999)
    # def WaitForClientTargetResponse(self, MaxWaitTimeMS: I32) -> Bool:
    #     pass
