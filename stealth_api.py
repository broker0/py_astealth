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
    # special and callback methods
    ####################################################################################################################
    @ApiSpecification.method(1)
    def _FunctionResult(self, CallId: U16, Result: Buffer) -> None:
        pass

    @ApiSpecification.method(2)
    def _StopScript(self) -> None:
        pass

    @ApiSpecification.method(5)
    def _LangVersion(self, Lang: U8, Major: U8, Minor: U8, Revision: U8, Build: U8):
        pass

    @ApiSpecification.method(6)
    def _EventCallback(self, EventId: U8, Arguments: TypedTuple) -> None:
        pass

    @ApiSpecification.method(9)
    def _ScriptPathRequest(self) -> None:
        pass

    @ApiSpecification.method(10)
    def _ScriptPath(self, ScriptName: String) -> None:
        pass

    @ApiSpecification.method(11)
    def _SelectProfile(self, ProfileName: String) -> None:
        pass

    ####################################################################################################################
    # connection management
    ####################################################################################################################
    @ApiSpecification.method(20)
    def Connected(self) -> Bool:
        pass

    @ApiSpecification.method(28)
    def GetARStatus(self) -> Bool:
        pass

    @ApiSpecification.method(29)
    def SetARStatus(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(529)
    def SetARExtParams(self, ShardName: String, CharName: String, UseAtEveryConnect: Bool) -> None:
        pass

    @ApiSpecification.method(21)
    def ConnectedTime(self) -> DateTime:
        pass

    @ApiSpecification.method(22)
    def DisconnectedTime(self) -> DateTime:
        pass

    @ApiSpecification.method(23)
    def Connect(self) -> None:
        pass

    @ApiSpecification.method(24)
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
    @ApiSpecification.method(34)
    def ProfileName(self) -> String:
        pass

    @ApiSpecification.method(35)
    def ChangeProfile(self, Name: String) -> I32:
        pass

    @ApiSpecification.method(527)
    def ProfileShardName(self) -> String:
        pass

    @ApiSpecification.method(528)
    def ExtChangeProfile(self, ProfileName: String, ShardName: String, CharName: String) -> I32:
        pass

    ####################################################################################################################
    # stealth info
    ####################################################################################################################
    @ApiSpecification.method(86)
    def GetStealthInfo(self) -> AboutData:
        pass

    @ApiSpecification.method(36)
    def StealthPath(self) -> String:
        pass

    @ApiSpecification.method(37)
    def StealthProfilePath(self) -> String:
        pass

    ####################################################################################################################
    # main information
    ####################################################################################################################
    @ApiSpecification.method(531)
    def GetCharsListForShard(self) -> list[String]:
        pass

    @ApiSpecification.method(38)
    def ShardPath(self) -> String:
        pass

    @ApiSpecification.method(526)
    def GameServerIPString(self) -> String:
        pass

    @ApiSpecification.method(200)
    def Self(self) -> U32:
        pass

    @ApiSpecification.method(204)
    def WorldNum(self) -> U8:
        pass

    @ApiSpecification.method(32)
    def CharName(self) -> String:
        pass

    @ApiSpecification.method(228)
    def Backpack(self) -> U32:
        pass

    @ApiSpecification.method(463)
    def PredictedX(self) -> U16:
        pass

    @ApiSpecification.method(464)
    def PredictedY(self) -> U16:
        pass

    @ApiSpecification.method(465)
    def PredictedZ(self) -> I8:
        pass

    @ApiSpecification.method(466)
    def PredictedDirection(self) -> U8:
        pass

    @ApiSpecification.method(205)
    def Sex(self) -> U8:
        pass

    @ApiSpecification.method(206)
    def CharTitle(self) -> String:
        pass

    @ApiSpecification.method(207)
    def Gold(self) -> U32:
        pass

    @ApiSpecification.method(208)
    def Armor(self) -> U16:
        pass

    @ApiSpecification.method(209)
    def Weight(self) -> U16:
        pass

    @ApiSpecification.method(210)
    def MaxWeight(self) -> U16:
        pass

    @ApiSpecification.method(211)
    def Race(self) -> U8:
        pass

    @ApiSpecification.method(212)
    def PetsMax(self) -> U8:
        pass

    @ApiSpecification.method(213)
    def PetsCurrent(self) -> U8:
        pass

    @ApiSpecification.method(214)
    def FireResist(self) -> U16:
        pass

    @ApiSpecification.method(215)
    def ColdResist(self) -> U16:
        pass

    @ApiSpecification.method(216)
    def PoisonResist(self) -> U16:
        pass

    @ApiSpecification.method(217)
    def EnergyResist(self) -> U16:
        pass

    @ApiSpecification.method(33)
    def ShardName(self) -> String:
        pass

    @ApiSpecification.method(227)
    def Luck(self) -> U16:
        pass

    @ApiSpecification.method(317)
    def GetExtInfo(self) -> ExtendedInfo:
        pass

    @ApiSpecification.method(318)
    def Hidden(self) -> Bool:
        pass

    @ApiSpecification.method(319)
    def Poisoned(self) -> Bool:
        pass

    @ApiSpecification.method(320)
    def Paralyzed(self) -> Bool:
        pass

    @ApiSpecification.method(321)
    def Dead(self) -> Bool:
        pass



    ####################################################################################################################
    # object information
    ####################################################################################################################
    @ApiSpecification.method(87)
    def IsObjectExists(self, ID: U32) -> Bool:
        pass

    @ApiSpecification.method(201)
    def GetX(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(202)
    def GetY(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(203)
    def GetZ(self, ID: U32) -> I8:
        pass

    @ApiSpecification.method(331)
    def GetDirection(self, ID: U32) -> U8:
        pass

    @ApiSpecification.method(332)
    def GetDistance(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(326)
    def GetType(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(333)
    def GetColor(self, ID: U32) -> U16:
        pass

    @ApiSpecification.method(329)
    def GetQuantity(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(330)
    def GetPrice(self, ObjID: U32) -> U32:
        pass

    @ApiSpecification.method(322)
    def GetName(ObjID: U32) -> String:
        pass

    @ApiSpecification.method(323)
    def GetAltName(self, ObjID: U32) -> String:
        pass

    @ApiSpecification.method(324)
    def GetTitle(self, ObjID: U32) -> String:
        pass

    @ApiSpecification.method(343)
    def GetNotoriety(self, ID: U32) -> U8:
        pass

    @ApiSpecification.method(334)
    def GetStr(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(335)
    def GetInt(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(336)
    def GetDex(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(337)
    def GetHP(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(338)
    def GetMaxHP(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(339)
    def GetMana(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(340)
    def GetMaxMana(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(341)
    def GetStam(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(342)
    def GetMaxStam(self, ObjID: U32) -> I32:
        pass

    @ApiSpecification.method(344)
    def GetParent(self, ObjID: U32) -> U32:
        pass

    @ApiSpecification.method(345)
    def IsWarMode(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(346)
    def IsNPC(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(347)
    def IsDead(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(348)
    def IsRunning(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(349)
    def IsContainer(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(350)
    def IsHidden(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(351)
    def IsMovable(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(352)
    def IsYellowHits(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(353)
    def IsPoisoned(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(354)
    def IsParalyzed(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(355)
    def IsFemale(self, ObjID: U32) -> Bool:
        pass

    @ApiSpecification.method(401)
    def ObjAtLayerEx(self, Layer: U8, ID: U32) -> U32:
        pass

    @ApiSpecification.method(402)
    def GetLayer(self, ObjID: U32) -> U8:
        pass

    @ApiSpecification.method(421)
    def MobileCanBeRenamed(self, MobID: U32) -> Bool:
        pass

    @ApiSpecification.method(356)
    def IsHouse(self, ObjID: U32) -> Bool:
        pass

    ####################################################################################################################
    # past information
    ####################################################################################################################
    @ApiSpecification.method(230)
    def LastContainer(self) -> U32:
        pass

    @ApiSpecification.method(231)
    def LastTarget(self) -> U32:
        pass

    @ApiSpecification.method(232)
    def LastAttack(self) -> U32:
        pass

    @ApiSpecification.method(233)
    def LastStatus(self) -> U32:
        pass

    @ApiSpecification.method(234)
    def LastObject(self) -> U32:
        pass



    ####################################################################################################################
    # journal
    ####################################################################################################################
    @ApiSpecification.method(39)
    def AddToSystemJournal(self, Text: String) -> None:
        pass

    @ApiSpecification.method(41)
    def ClearSystemJournal(self) -> None:
        pass

    @ApiSpecification.method(293)
    def AddJournalIgnore(self, Str: String) -> None:
        pass

    @ApiSpecification.method(294)
    def ClearJournalIgnore(self) -> None:
        pass

    @ApiSpecification.method(295)
    def AddChatUserIgnore(self, Mobile: String) -> None:
        pass

    @ApiSpecification.method(296)
    def ClearChatUserIgnore(self) -> None:
        pass

    @ApiSpecification.method(43)
    def ClearJournal(self) -> None:
        pass

    @ApiSpecification.method(44)
    def LastJournalMessage(self) -> String:
        pass

    @ApiSpecification.method(45)
    def InJournal(self, Str: String) -> I32:
        pass

    @ApiSpecification.method(46)
    def InJournalBetweenTimes(self, Str: String, TimeBegin: DateTime, TimeEnd: DateTime) -> I32:
        pass

    @ApiSpecification.method(47)
    def Journal(self, StringIndex: I32) -> String:
        pass

    @ApiSpecification.method(48)
    def SetJournalLine(self, StringIndex: I32, Text: String) -> None:
        pass

    @ApiSpecification.method(49)
    def LowJournal(self) -> I32:
        pass

    @ApiSpecification.method(50)
    def HighJournal(self) -> I32:
        pass

    @ApiSpecification.method(42)
    def AddToJournal(self, Text: String) -> None:
        pass

    @ApiSpecification.method(51)
    def FoundedParamID(self) -> I32:
        pass

    @ApiSpecification.method(52)
    def LineID(self) -> U32:
        pass

    @ApiSpecification.method(53)
    def LineType(self) -> U16:
        pass

    @ApiSpecification.method(54)
    def GetLineTime(self) -> DateTime:
        pass

    @ApiSpecification.method(54)
    def LineTime(self) -> DateTime:
        pass

    @ApiSpecification.method(55)
    def LineMsgType(self) -> U8:
        pass

    @ApiSpecification.method(56)
    def LineTextColor(self) -> U16:
        pass

    @ApiSpecification.method(57)
    def LineTextFont(self) -> U16:
        pass

    @ApiSpecification.method(58)
    def LineIndex(self) -> I32:
        pass

    @ApiSpecification.method(59)
    def LineCount(self) -> I32:
        pass

    @ApiSpecification.method(60)
    def LineName(self) -> String:
        pass

    ####################################################################################################################
    # actions
    ####################################################################################################################
    @ApiSpecification.method(237)
    def Attack(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(273)
    def UseObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(274)
    def UseType(self, ObjType: U16, Color: U16) -> U32:
        pass

    @ApiSpecification.method(275)
    def UseFromGround(self, ObjType: U16, Color: U16) -> U32:
        pass

    @ApiSpecification.method(276)
    def ClickOnObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(270)
    def ToggleFly(self) -> None:
        pass

    @ApiSpecification.method(262)
    def Cast(self, SpellID: I32) -> None:
        pass

    @ApiSpecification.method(280)
    def OpenDoor(self) -> None:
        pass

    @ApiSpecification.method(281)
    def Bow(self) -> None:
        pass

    @ApiSpecification.method(282)
    def Salute(self) -> None:
        pass

    @ApiSpecification.method(420)
    def RenameMobile(self, MobID: U32, NewName: String) -> None:
        pass

    @ApiSpecification.method(459)
    def UOSay(self, Text: String) -> None:
        pass

    @ApiSpecification.method(460)
    def UOSayColor(self, Text: String, Color: U16) -> None:
        pass

    @ApiSpecification.method(277)
    def UseItemOnMobile(self, ItemSerial: U32, TargetSerial: U32) -> None:
        pass

    @ApiSpecification.method(278)
    def BandageSelf(self) -> None:
        pass

    ####################################################################################################################
    # skills related functions
    ####################################################################################################################
    @ApiSpecification.method(261)
    def UseSkill(self, SkillID: I32) -> None:
        pass

    @ApiSpecification.method(256)
    def SetSkillLockState(self, SkillID: I32, skillState: U8) -> None:
        pass

    @ApiSpecification.method(258)
    def GetSkillCap(self, SkillID: I32) -> F64:
        pass

    @ApiSpecification.method(259)
    def GetSkillValue(self, SkillID: I32) -> F64:
        pass

    @ApiSpecification.method(257)
    def GetSkillCurrentValue(self, SkillID: I32) -> F64:
        pass

    @ApiSpecification.method(255)
    def GetSkillLockState(self, SkillID: I32) -> I8:
        pass

    ####################################################################################################################
    # search and all that
    ####################################################################################################################
    @ApiSpecification.method(297)
    def SetFindDistance(self, Value: U32) -> None: pass
    @ApiSpecification.method(298)
    def GetFindDistance(self) -> U32: pass
    @ApiSpecification.method(299)
    def SetFindVertical(self, Value: U32) -> None: pass
    @ApiSpecification.method(300)
    def GetFindVertical(self) -> U32: pass
    @ApiSpecification.method(301)
    def FindTypeEx(self, ObjType: U16, Color: U16, Container: U32, InSub: Bool) -> U32: pass
    @ApiSpecification.method(302)
    def FindTypesArrayEx(self, ObjTypes: list[U16], Colors: list[U16], Containers: list[U32], InSub: Bool) -> U32: pass
    @ApiSpecification.method(303)
    def FindNotoriety(self, ObjType: U16, Notoriety: U8) -> U32: pass
    @ApiSpecification.method(309)
    def GetFindedList(self) -> list[U32]: pass
    @ApiSpecification.method(305)
    def Ignore(self, ID: U32) -> None: pass
    @ApiSpecification.method(306)
    def IgnoreOff(self, ID: U32) -> None: pass
    @ApiSpecification.method(307)
    def IgnoreReset(self) -> None: pass
    @ApiSpecification.method(308)
    def GetIgnoreList(self) -> list[U32]: pass
    @ApiSpecification.method(304)
    def FindAtCoord(self, X: U16, Y: U16) -> U32: pass
    @ApiSpecification.method(310)
    def FindItem(self) -> U32: pass
    @ApiSpecification.method(311)
    def FindCount(self) -> I32: pass
    @ApiSpecification.method(312)
    def FindQuantity(self) -> I32: pass
    @ApiSpecification.method(313)
    def FindFullQuantity(self) -> I32: pass

    ####################################################################################################################
    # multis
    ####################################################################################################################
    @ApiSpecification.method(517)
    def GetMultiPartsAtPosition(self, X: U16, Y: U16) -> list[MultiPart]:
        pass

    @ApiSpecification.method(518)
    def GetMultiAllParts(self, MultiID: U32) -> list[MultiPart]:
        pass

    @ApiSpecification.method(516)
    def GetMultis(self) -> list[Multi]:
        pass

    ####################################################################################################################
    # movement
    ####################################################################################################################
    @ApiSpecification.method(481)
    def SetRunUnmountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(482)
    def SetWalkMountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(483)
    def SetRunMountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(484)
    def SetWalkUnmountTimer(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(485)
    def GetRunMountTimer(self) -> U16:
        pass

    @ApiSpecification.method(486)
    def GetWalkMountTimer(self) -> U16:
        pass

    @ApiSpecification.method(487)
    def GetRunUnmountTimer(self) -> U16:
        pass

    @ApiSpecification.method(488)
    def GetWalkUnmountTimer(self) -> U16:
        pass

    @ApiSpecification.method(490)
    def Step(self, Direction: U8, Running: Bool) -> U8:
        pass

    @ApiSpecification.method(491)
    def StepQ(self, Direction: U8, Running: Bool) -> I32:
        pass

    @ApiSpecification.method(492)
    def MoveXYZ(self, Xdst: U16, Ydst: U16, Zdst: I8, AccuracyXY: I32, AccuracyZ: I32, Running: Bool) -> Bool:
        pass

    @ApiSpecification.method(493)
    def MoveXY(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32, Running: Bool) -> Bool:
        pass

    @ApiSpecification.method(502)
    def MoverStop(self) -> None:
        pass

    ####################################################################################################################
    # pathfinding, los
    ####################################################################################################################

    @ApiSpecification.method(438)
    def IsWorldCellPassable(self, CurrX: U16, CurrY: U16, CurrZ: I8, DestX: U16, DestY: U16, DestZ: I8, WorldNum: U8) -> Bool:
        pass

    @ApiSpecification.method(499)
    def CheckLOS(self, Xfrom: U16, Yfrom: U16, Zfrom: I8, Xto: I32, Yto: I32, Zto: I8, WorldNum: U8) -> Bool:
        pass

    @ApiSpecification.method(500)
    def GetPathArray(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32) -> list[WorldPoint]:
        pass

    @ApiSpecification.method(501)
    def GetPathArray3D(self,
                       StartX: U16, StartY: U16, StartZ: I8,
                       FinishX: U16, FinishY: U16, FinishZ: I8,
                       WorldNum: U8,
                       AccuracyXY: I32, AccuracyZ: I32,
                       Run: Bool) -> list[WorldPoint]:
        pass


    @ApiSpecification.method(489)
    def GetNextStepZ(self, CurrX: U16, CurrY: U16, DestX: U16, DestY: U16, WorldNum: U8, CurrZ: I8) -> I8:
        pass

    @ApiSpecification.method(494)
    def SetBadLocation(self, X: U16, Y: U16) -> None:
        pass

    @ApiSpecification.method(495)
    def SetGoodLocation(self, X: U16, Y: U16) -> None:
        pass

    @ApiSpecification.method(496)
    def ClearBadLocationList(self) -> None:
        pass

    @ApiSpecification.method(497)
    def SetBadObject(self, ObjType: U16, Color: U16, Radius: U8) -> None:
        pass

    @ApiSpecification.method(498)
    def ClearBadObjectList(self) -> None:
        pass


    ####################################################################################################################
    # map, statics
    ####################################################################################################################
    @ApiSpecification.method(439)
    def GetStaticTilesArray(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: list[U16]) -> list[FoundTile]:
        pass

    @ApiSpecification.method(440)
    def GetLandTilesArray(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileType: list[U16]) -> list[FoundTile]:
        pass

    @ApiSpecification.method(432)
    def GetTileFlags(self, Group: U8, Tile: U16) -> U32:
        pass

    @ApiSpecification.method(433)
    def GetLandTileData(self, Tile: U16) -> LandTileData:
        pass

    @ApiSpecification.method(434)
    def GetStaticTileData(self, Tile: U16) -> StaticTileData:
        pass

    @ApiSpecification.method(435)
    def GetLayerCount(self, x: U16, y: U16, WorldNum: U8) -> U8:
        pass

    @ApiSpecification.method(436)
    def ReadStaticsXY(self, X: U16, Y: U16, WorldNum: U8) -> list[StaticItemRealXY]:
        pass

    @ApiSpecification.method(437)
    def GetSurfaceZ(self, X: U16, Y: U16, WorldNum: U8) -> I8:
        pass

    @ApiSpecification.method(441)
    def GetCell(self, X: U16, Y: U16, WorldNum: U8) -> MapCell:
        pass

    ####################################################################################################################
    # gumps
    ####################################################################################################################
    @ApiSpecification.method(379)
    def WaitGump(self, Value: I32) -> None:
        pass

    @ApiSpecification.method(381)
    def GumpAutoTextEntry(self, TextEntryID: I32, Value: String) -> None:
        pass

    @ApiSpecification.method(382)
    def GumpAutoRadiobutton(self, RadiobuttonID: I32, Value: I32) -> None:
        pass

    @ApiSpecification.method(383)
    def GumpAutoCheckBox(self, CheckBoxID: I32, Value: I32) -> None:
        pass

    @ApiSpecification.method(384)
    def NumGumpButton(self, GumpIndex: U16, Value: I32) -> Bool:
        pass

    @ApiSpecification.method(385)
    def NumGumpTextEntry(self, GumpIndex: U16, TextEntryID: I32, Value: String) -> Bool:
        pass

    @ApiSpecification.method(386)
    def NumGumpRadiobutton(self, GumpIndex: U16, RadiobuttonID: I32, Value: I32) -> Bool:
        pass

    @ApiSpecification.method(387)
    def NumGumpCheckBox(self, GumpIndex: U16, CBID: I32, Value: I32) -> Bool:
        pass

    @ApiSpecification.method(388)
    def GetGumpsCount(self) -> U16:
        pass

    @ApiSpecification.method(389)
    def CloseSimpleGump(self, GumpIndex: U16) -> None:
        pass

    @ApiSpecification.method(390)
    def GetGumpSerial(self, GumpIndex: U16) -> U32:
        pass

    @ApiSpecification.method(391)
    def GetGumpID(self, GumpIndex: U16) -> U32:
        pass

    @ApiSpecification.method(392)
    def IsGumpCanBeClosed(self, GumpIndex: U16) -> Bool:
        pass

    @ApiSpecification.method(393)
    def GetGumpTextLines(self, GumpIndex: U16) -> list[String]: pass


    @ApiSpecification.method(394)
    def GetGumpFullLines(self, GumpIndex: U16) -> list[String]:
        pass

    @ApiSpecification.method(395)
    def GetGumpShortLines(self, GumpIndex: U16) -> list[String]:
        pass

    @ApiSpecification.method(396)
    def GetGumpButtonsDescription(self, GumpIndex: U16) -> list[String]:
        pass

    @ApiSpecification.method(397)
    def GetGumpInfo(self, GumpIndex: U16) -> GumpInfo:
        pass

    @ApiSpecification.method(398)
    def AddGumpIgnoreByID(self, ID: U32) -> None:
        pass

    @ApiSpecification.method(399)
    def AddGumpIgnoreBySerial(self, Serial: U32) -> None:
        pass

    @ApiSpecification.method(400)
    def ClearGumpsIgnore(self) -> None:
        pass


    ####################################################################################################################
    # menu
    ####################################################################################################################
    @ApiSpecification.method(370)
    def WaitMenu(self, MenuCaption: String, ElementCaption: String) -> None:
        pass

    @ApiSpecification.method(371)
    def AutoMenu(self, MenuCaption: String, ElementCaption: String) -> None:
        pass

    @ApiSpecification.method(372)
    def MenuHookPresent(self) -> Bool:
        pass

    @ApiSpecification.method(373)
    def MenuPresent(self) -> Bool:
        pass

    @ApiSpecification.method(374)
    def CancelMenu(self) -> None:
        pass

    @ApiSpecification.method(375)
    def CloseMenu(self) -> None:
        pass

    @ApiSpecification.method(376)
    def GetMenuItems(self, Caption: String) -> list[String]:
        pass

    @ApiSpecification.method(378)
    def GetLastMenuItems(self) -> list[String]:
        pass

    @ApiSpecification.method(377)
    def GetMenuItemsEx(self, Caption: String) -> list[MenuItem]:
        pass

    ####################################################################################################################
    # context menu
    ####################################################################################################################
    @ApiSpecification.method(357)
    def RequestContextMenu(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(358)
    def SetContextMenuHook(self, MenuID: U32, EntryNumber: U8) -> None:
        pass

    @ApiSpecification.method(359)
    def GetContextMenu(self) -> list[String]:
        pass

    @ApiSpecification.method(360)
    def ClearContextMenu(self) -> None:
        pass

    ####################################################################################################################
    # scripts management
    ####################################################################################################################
    @ApiSpecification.method(67)
    def GetScriptsCount(self) -> U16:
        pass

    @ApiSpecification.method(68)
    def GetScriptPath(self, ScriptIndex: U16) -> String:
        pass

    @ApiSpecification.method(69)
    def GetScriptState(self, ScriptIndex: U16) -> U8:
        pass

    @ApiSpecification.method(70)
    def StartScript(self, ScriptPath: String) -> U16:
        pass

    @ApiSpecification.method(71)
    def _StopScript(self, ScriptIndex: U16) -> None:
        pass

    @ApiSpecification.method(72)
    def PauseResumeSelScript (self, ScriptIndex: U16) -> None:
        pass

    @ApiSpecification.method(73)
    def StopAllScripts(self) -> None:
        pass

    @ApiSpecification.method(74)
    def SetScriptName(self, ScriptIndex: U16, Value: String) -> None:
        pass

    @ApiSpecification.method(75)
    def GetScriptName(self, ScriptIndex: U16) -> String:
        pass

    @ApiSpecification.method(30)
    def GetPauseScriptOnDisconnectStatus(self) -> Bool:
        pass

    @ApiSpecification.method(31)
    def SetPauseScriptOnDisconnectStatus(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(77)
    def GetScriptsList(self) -> list[ScriptInfo]:
        pass
    #
    ####################################################################################################################
    # map drawing
    ####################################################################################################################
    @ApiSpecification.method(522)
    def AddFigure(self, figure: MapFigure) -> U32:
        pass

    @ApiSpecification.method(523)
    def RemoveFigure(self, FigureID: U32) -> Bool:
        pass

    @ApiSpecification.method(524)
    def UpdateFigure(self, FigureID: U32, figure: MapFigure) -> Bool:
        pass

    @ApiSpecification.method(525)
    def ClearFigures(self) -> None:
        pass

    ####################################################################################################################
    # books management
    ####################################################################################################################
    @ApiSpecification.method(504)
    def BookGetPageText(self, Page: U16) -> String:
        pass

    @ApiSpecification.method(505)
    def BookSetText(self, Text: String) -> None:
        pass

    @ApiSpecification.method(506)
    def BookSetPageText(self, Page: U16, Text: String) -> None:
        pass

    @ApiSpecification.method(507)
    def BookClearText(self) -> None:
        pass

    @ApiSpecification.method(508)
    def BookSetHeader(self, Title: String, Author: String) -> None:
        pass

    ####################################################################################################################
    # party related functions
    ####################################################################################################################
    @ApiSpecification.method(422)
    def InviteToParty(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(423)
    def RemoveFromParty(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(424)
    def PartyPrivateMessageTo(self, ObjID: U32, Msg: String) -> None:
        pass

    @ApiSpecification.method(425)
    def PartySay(self, Msg: String) -> None:
        pass

    @ApiSpecification.method(426)
    def PartyCanLootMe(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(427)
    def PartyAcceptInvite(self) -> None:
        pass

    @ApiSpecification.method(428)
    def PartyDeclineInvite(self) -> None:
        pass

    @ApiSpecification.method(429)
    def PartyLeave(self) -> None:
        pass

    @ApiSpecification.method(430)
    def PartyMembersList(self) -> list[U32]:
        pass

    @ApiSpecification.method(431)
    def InParty(self) -> Bool:
        pass

    ####################################################################################################################
    # targets
    ####################################################################################################################
    @ApiSpecification.method(240)
    def TargetID(self) -> U32:
        pass

    @ApiSpecification.method(241)
    def CancelTarget(self) -> None:
        pass

    @ApiSpecification.method(242)
    def TargetToObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(243)
    def TargetToXYZ(self, X: U16, Y: U16, Z: I8) -> None:
        pass

    @ApiSpecification.method(244)
    def TargetToTile(self, Tile: U16, X: U16, Y: U16, Z: I8) -> None:
        pass

    @ApiSpecification.method(245)
    def WaitTargetObject(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(246)
    def WaitTargetTile(self, Tile: U16, X: U16, Y: U16, Z: I8) -> None:
        pass

    @ApiSpecification.method(247)
    def WaitTargetXYZ(self, X: U16, Y: U16, Z: I8) -> None:
        pass

    @ApiSpecification.method(248)
    def WaitTargetSelf(self) -> None:
        pass

    @ApiSpecification.method(249)
    def WaitTargetType(self, ObjType: U16) -> None:
        pass

    @ApiSpecification.method(250)
    def CancelWaitTarget(self) -> None:
        pass

    @ApiSpecification.method(251)
    def WaitTargetGround(self, ObjType: U16) -> None:
        pass

    @ApiSpecification.method(252)
    def WaitTargetLast(self) -> None:
        pass

    @ApiSpecification.method(279)
    def TargetByResource(self, ObjID: U32, Resource: U16) -> None:
        pass


    ####################################################################################################################
    # item manipulations
    ####################################################################################################################
    @ApiSpecification.method(291)
    def DragItem(self, ObjID: U32, Count: I32) -> Bool:
        pass

    @ApiSpecification.method(292)
    def DropItem(self, MoveIntoID: U32, X: I32, Y: I32, Z: I8) -> Bool:
        pass

    @ApiSpecification.method(403)
    def WearItem(self, Layer: U8, ObjID: U32) -> Bool:
        pass

    ####################################################################################################################
    # trade
    ####################################################################################################################
    @ApiSpecification.method(362)
    def IsTrade(self) -> Bool:
        pass

    @ApiSpecification.method(363)
    def GetTradeContainer(self, TradeNum: U8, Num: U8) -> U32:
        pass

    @ApiSpecification.method(364)
    def GetTradeOpponent(self, TradeNum: U8) -> U32:
        pass

    @ApiSpecification.method(365)
    def TradeCount(self) -> U8:
        pass

    @ApiSpecification.method(366)
    def GetTradeOpponentName(self, TradeNum: U8) -> String:
        pass

    @ApiSpecification.method(367)
    def TradeCheck(self, TradeNum: U8, Num: U8) -> Bool:
        pass

    @ApiSpecification.method(368)
    def ConfirmTrade(self, TradeNum: U8) -> None:
        pass

    @ApiSpecification.method(369)
    def CancelTrade(self, TradeNum: U8) -> Bool:
        pass

    ####################################################################################################################
    # buy/sell
    ####################################################################################################################
    @ApiSpecification.method(411)
    def AutoBuy(self, ItemType: U16, ItemColor: U16, Quantity: U16) -> None:
        pass

    @ApiSpecification.method(412)
    def GetShopList(self) -> list[String]:
        pass

    @ApiSpecification.method(413)
    def ClearShopList(self) -> None:
        pass

    @ApiSpecification.method(414)
    def AutoBuyEx(self, ItemType: U16, ItemColor: U16, Quantity: U16, Price: U32, Name: String) -> None:
        pass

    @ApiSpecification.method(415)
    def GetAutoBuyDelay(self) -> U16:
        pass

    @ApiSpecification.method(416)
    def SetAutoBuyDelay(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(417)
    def GetAutoSellDelay(self) -> U16:
        pass

    @ApiSpecification.method(418)
    def SetAutoSellDelay(self, Value: U16) -> None:
        pass

    @ApiSpecification.method(419)
    def AutoSell(self, ItemType: U16, ItemColor: U16, Quantity: U16) -> None:
        pass

    ####################################################################################################################
    # global chat
    ####################################################################################################################
    @ApiSpecification.method(509)
    def GlobalChatJoinChannel(self, ChName: String) -> None:
        pass

    @ApiSpecification.method(510)
    def GlobalChatLeaveChannel(self) -> None:
        pass

    @ApiSpecification.method(511)
    def GlobalChatSendMsg(self, MsgText: String) -> None:
        pass

    @ApiSpecification.method(512)
    def GlobalChatActiveChannel(self) -> String:
        pass

    @ApiSpecification.method(513)
    def GlobalChatChannelsList(self) -> list[String]:
        pass

    ####################################################################################################################
    # proxy related
    ####################################################################################################################
    @ApiSpecification.method(25)
    def ProxyIP(self) -> String:
        pass

    @ApiSpecification.method(26)
    def ProxyPort(self) -> U16:
        pass

    @ApiSpecification.method(27)
    def UseProxy(self) -> Bool:
        pass

    ####################################################################################################################
    # client interaction
    ####################################################################################################################
    @ApiSpecification.method(446)
    def ClientPrint(self, Text: String) -> None:
        pass

    @ApiSpecification.method(447)
    def ClientPrintEx(self, SenderID: U32, Color: U16, Font: U16, Text: String) -> None:
        pass

    @ApiSpecification.method(448)
    def CloseClientUIWindow(self, UIWindowType: U8, ID: U32) -> None:
        pass

    @ApiSpecification.method(449)
    def ClientRequestObjectTarget(self) -> None:
        pass

    @ApiSpecification.method(450)
    def ClientRequestTileTarget(self) -> None:
        pass

    @ApiSpecification.method(451)
    def ClientTargetResponsePresent(self) -> Bool:
        pass

    @ApiSpecification.method(452)
    def ClientTargetResponse(self) -> TargetInfo:
        pass

    @ApiSpecification.method(444)
    def CloseClientGump(self, ID: U32) -> None:
        pass

    @ApiSpecification.method(445)
    def ClientHide(self, ObjID: U32) -> Bool:
        pass

    ####################################################################################################################
    # UserStatic functions
    ####################################################################################################################
    @ApiSpecification.method(519)
    def AddUserStatic(self, StaticItem: UserStaticItem, WorldNum: U8) -> I32:
        pass

    @ApiSpecification.method(520)
    def RemoveUserStatic(self, StaticID: I32) -> Bool:
        pass

    @ApiSpecification.method(521)
    def ClearUserStatics(self) -> None:
        pass

    ####################################################################################################################
    # abilities functions
    ####################################################################################################################
    @ApiSpecification.method(264)
    def UsePrimaryAbility(self) -> None:
        pass

    @ApiSpecification.method(265)
    def UseSecondaryAbility(self) -> None:
        pass

    @ApiSpecification.method(266)
    def GetActiveAbility(self) -> String:
        pass

    @ApiSpecification.method(263)
    def IsActiveSpellAbility(self, SpellID: I32) -> Bool:
        pass


    ####################################################################################################################
    # http functions
    ####################################################################################################################
    @ApiSpecification.method(61)
    def HTTP_Get(self, URL: String) -> None:
        pass

    @ApiSpecification.method(62)
    def HTTP_Post(self, URL: String, PostData: String) -> String:
        pass

    @ApiSpecification.method(63)
    def HTTP_Body(self) -> String:
        pass

    @ApiSpecification.method(64)
    def HTTP_Header(self) -> String:
        pass

    ####################################################################################################################
    # war functions
    ####################################################################################################################
    @ApiSpecification.method(235)
    def WarTargetID(self) -> U32:
        pass

    @ApiSpecification.method(236)
    def SetWarMode(self, Value: Bool) -> None:
        pass


    ####################################################################################################################
    # unclassified functions
    ####################################################################################################################
    @ApiSpecification.method(238)
    def UseSelfPaperdollScroll(self) -> None:
        pass

    @ApiSpecification.method(239)
    def UseOtherPaperdollScroll(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(271)
    def ReqVirtuesGump(self) -> None:
        pass

    @ApiSpecification.method(272)
    def UseVirtue(self, VirtueID: U32) -> None:
        pass

    @ApiSpecification.method(283)
    def SetCatchBag(self, ObjID: U32) -> U8:
        pass

    @ApiSpecification.method(284)
    def UnsetCatchBag(self) -> None:
        pass


    #########################################
    #########################################
    # Autogenerated signatures, not checked #
    #########################################
    #########################################
    @ApiSpecification.method(90)
    def GetNowUnix(self) -> I64:
        pass

    @ApiSpecification.method(91)
    def GetNow(self) -> DateTime:
        pass

    @ApiSpecification.method(78)
    def GetShowIPCExceptionWindow(self) -> Bool:
        pass

    @ApiSpecification.method(79)
    def SetShowIPCExceptionWindow(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(327)
    def GetTooltipRec(self, ObjID: U32) -> list[ClilocRec]:
        pass

    @ApiSpecification.method(328)
    def GetClilocByID(self, ClilocID: U32) -> String:
        pass

    @ApiSpecification.method(380)
    def WaitTextEntry(self, Value: String) -> None:
        pass

    @ApiSpecification.method(401)
    def ObjAtLayerEx(self, LayerType: U8, PlayerID: U32) -> U32:
        pass

    @ApiSpecification.method(406)
    def SetDress(self) -> None:
        pass

    @ApiSpecification.method(267)
    def RequestStats(self, ObjID: U32) -> None:
        pass

    @ApiSpecification.method(268)
    def HelpRequest(self) -> None:
        pass

    @ApiSpecification.method(269)
    def QuestRequest(self) -> None:
        pass

    @ApiSpecification.method(254)
    def SetStatState(self, statNum: U8, statState: U8) -> None:
        pass

    @ApiSpecification.method(253)
    def GetStatLockState(self, statNum: U8) -> I8:
        pass

    @ApiSpecification.method(443)
    def GetStaticArt(self, ObjType: U32, Hue: U16) -> list[U8]:
        pass

    # @ApiSpecification.method(88)
    # def PrintScriptMethodsList(self, FileName: String = ', SortedList: Boolean = False) -> None:
    #     pass

    @ApiSpecification.method(456)
    def GetQuestArrow(self) -> Point:
        pass

    @ApiSpecification.method(457)
    def SetSilentMode(self, Value: Bool) -> None:
        pass

    @ApiSpecification.method(65)
    def SetGlobal(self, GlobalRegion: U8, VarName: String, VarValue: String) -> None:
        pass

    @ApiSpecification.method(66)
    def GetGlobal(self, GlobalRegion: U8, VarName: String) -> String:
        pass

    @ApiSpecification.method(461)
    def ConsoleEntryReply(self, Text: String) -> None:
        pass

    @ApiSpecification.method(462)
    def ConsoleEntryUnicodeReply(self, Text: String) -> None:
        pass

    @ApiSpecification.method(514)
    def FillInfoWindow(self, s: String) -> None:
        pass

    @ApiSpecification.method(515)
    def ClearInfoWindow(self) -> None:
        pass

    @ApiSpecification.method(229)
    def GetBuffBarInfo(self) -> list[BuffBarInfo]:
        pass

    @ApiSpecification.method(442)
    def ConvertIntegerToFlags(self, Group: U8, Flags: U32) -> list[String]:
        pass


    @ApiSpecification.method(367)
    def DumpObjectsCache(self) -> None:
        pass

    @ApiSpecification.method(410)
    def EquipLastWeapon(self) -> None:
        pass

    @ApiSpecification.method(316)
    def GetPlayerStatusText(self, ObjID: U32) -> String:
        pass

    # new methods
    @ApiSpecification.method(218)
    def GetSelfStr(self) -> I32:
        pass
    @ApiSpecification.method(219)
    def GetSelfInt(self) -> I32:
        pass
    @ApiSpecification.method(220)
    def GetSelfDex(self) -> I32:
        pass
    @ApiSpecification.method(221)
    def GetSelfLife(self) -> I32:
        pass
    @ApiSpecification.method(222)
    def GetSelfMana(self) -> I32:
        pass
    @ApiSpecification.method(223)
    def GetSelfStam(self) -> I32:
        pass
    @ApiSpecification.method(224)
    def GetSelfMaxLife(self) -> I32:
        pass
    @ApiSpecification.method(225)
    def GetSelfMaxMana(self) -> I32:
        pass
    @ApiSpecification.method(226)
    def GetSelfMaxStam(self) -> I32:
        pass
    @ApiSpecification.method(260)
    def GetSkillID(self, SkillName: String) -> I32:
        pass
    @ApiSpecification.method(325)
    def GetTooltip(self, ObjID: U32) -> String:
        pass
    @ApiSpecification.method(285)
    def GetPickupedItem(self) -> U32:
        pass
    @ApiSpecification.method(286)
    def SetPickupedItem(self, ID: U32) -> None:
        pass
    @ApiSpecification.method(287)
    def GetDropCheckCoord(self) -> Bool:
        pass
    @ApiSpecification.method(288)
    def SetDropCheckCoord(self, Value: Bool) -> None:
        pass
    @ApiSpecification.method(289)
    def GetDropDelay(self) -> U32:
        pass
    @ApiSpecification.method(290)
    def SetDropDelay(self, Value: U32) -> None:
        pass
    @ApiSpecification.method(404)
    def GetDressSpeed(self) -> U16:
        pass
    @ApiSpecification.method(405)
    def SetDressSpeed(self, Value: U16) -> None:
        pass
    @ApiSpecification.method(407)
    def GetDressSet(self) -> list[LayerObject]:
        pass
    @ApiSpecification.method(88)
    def PrintScriptMethodsList(self, FileName: String, SortedList: Bool) -> None:
        pass
    @ApiSpecification.method(89)
    def SetAlarm(self) -> None:
        pass
    @ApiSpecification.method(453)
    def CheckLagBegin(self) -> None:
        pass
    @ApiSpecification.method(454)
    def CheckLagEnd(self) -> None:
        pass
    @ApiSpecification.method(455)
    def IsCheckLagEnd(self) -> Bool:
        pass
    @ApiSpecification.method(458)
    def GetSilentMode(self) -> Bool:
        pass
    @ApiSpecification.method(314)
    def SetFindInNulPoint(self, Value: Bool) -> None:
        pass
    @ApiSpecification.method(315)
    def GetFindInNulPoint(self) -> Bool:
        pass
    @ApiSpecification.method(503)
    def GetLastStepQUsedDoor(self) -> U32:
        pass
    @ApiSpecification.method(361)
    def GetContextMenuRec(self) -> ContextMenuRec:
        pass
    @ApiSpecification.method(532)
    def GetClientVersionInt(self) -> I32:
        pass
    @ApiSpecification.method(408)
    def UnequipItemsSetMacro(self) -> None:
        pass
    @ApiSpecification.method(409)
    def EquipItemsSetMacro(self) -> None:
        pass

    @ApiSpecification.method(530)
    def CreateChar(self,
                   ProfileName: String,
                   ShardName: String,
                   CharName: String,
                   Gender: Bool,
                   Race: I8,
                   Strn: I8, Dex: I8, Int: I8,
                   Skill1: String, Skill2: String, Skill3: String, Skill4: String,
                   SkillValue1: I32, SkillValue2: I32, SkillValue3: I32, SkillValue4: I32,
                   City: I8, Slot: U32) -> None:
        pass
    @ApiSpecification.method(40)
    def AddToSystemJournalEx(self, value: String, textcolor: I32, bgcolor: I32, fontsize: I32, fontname: String) -> None:
        pass
    @ApiSpecification.method(467)
    def SetMoveOpenDoor(self, Value: Bool) -> None:
        pass
    @ApiSpecification.method(468)
    def GetMoveOpenDoor(self) -> Bool:
        pass
    @ApiSpecification.method(469)
    def SetMoveThroughNPC(self, Value: U16) -> None:
        pass
    @ApiSpecification.method(470)
    def GetMoveThroughNPC(self) -> U16:
        pass
    @ApiSpecification.method(471)
    def SetMoveThroughCorner(self, Value: Bool) -> None:
        pass
    @ApiSpecification.method(472)
    def GetMoveThroughCorner(self) -> Bool:
        pass
    @ApiSpecification.method(473)
    def SetMoveHeuristicMult(self, Value: I32) -> None:
        pass
    @ApiSpecification.method(474)
    def GetMoveHeuristicMult(self) -> I32:
        pass
    @ApiSpecification.method(475)
    def SetMoveCheckStamina(self, Value: U16) -> None:
        pass
    @ApiSpecification.method(476)
    def GetMoveCheckStamina(self) -> U16:
        pass
    @ApiSpecification.method(477)
    def SetMoveTurnCost(self, Value: I32) -> None:
        pass
    @ApiSpecification.method(478)
    def GetMoveTurnCost(self) -> I32:
        pass
    @ApiSpecification.method(479)
    def SetMoveBetweenTwoCorners(self, Value: Bool) -> None:
        pass
    @ApiSpecification.method(480)
    def GetMoveBetweenTwoCorners(self) -> Bool:
        pass
    @ApiSpecification.method(72)
    def PauseResumeSelScript(self, ScriptIndex: U16) -> None:
        pass
    @ApiSpecification.method(76)
    def GetScriptParams(self) -> U32:
        pass
    @ApiSpecification.method(80)
    def Messenger_GetConnected(self, MesID: U8) -> Bool:
        pass
    @ApiSpecification.method(81)
    def Messenger_SetConnected(self, MesID: U8, Value: Bool) -> None:
        pass
    @ApiSpecification.method(82)
    def Messenger_GetToken(self, MesID: U8) -> String:
        pass
    @ApiSpecification.method(83)
    def Messenger_SetToken(self, MesID: U8, Value: String) -> None:
        pass
    @ApiSpecification.method(84)
    def Messenger_GetName(self, MesID: U8) -> String:
        pass
    @ApiSpecification.method(85)
    def Messenger_SendMessage(self, MesID: U8, Msg: String, UserID: String) -> None:
        pass
