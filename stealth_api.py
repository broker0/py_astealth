from py_astealth.core.api_specification import ApiSpecification, register_api, method_api
from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *


@register_api
class StealthApi(ApiSpecification):
    """
    Declarative API description using decorators.
    The key is the method signatures with a detailed description of the argument types and the return type.
    Methods do not have to have an implementation, they are just a protocol specification.
    """

    ####################################################################################################################
    # internal service and callback methods
    ####################################################################################################################
    @method_api(1)
    def _FunctionResultCallback(self, CallId: U16, Result: Buffer) -> None: ...

    @method_api(2)
    def _StopScriptCallback(self) -> None: ...

    @method_api(3)
    def _ErrorReportCallback(self, Error: String) -> None: ...

    @method_api(4)
    def _ScriptTogglePauseCallback(self) -> None: ...

    @method_api(6)
    def _EventCallback(self, EventId: U8, Arguments: TypedTuple) -> None: ...

    @method_api(9)
    def _ScriptPathCallback(self) -> None: ...

    @method_api(5)
    def _LangVersion(self, Lang: U8, Major: U8, Minor: U8, Revision: U8, Build: U8) -> None: ...

    @method_api(10)
    def _ScriptPath(self, ScriptName: String) -> None: ...

    @method_api(11)
    def _SelectProfile(self, ProfileName: String) -> None: ...

    @method_api(12)
    def _RequestPort(self, GroupId: U64, ProfileName: String) -> tuple[U16, U64]: ...

    ####################################################################################################################
    # connection management
    ####################################################################################################################
    @method_api(20)
    def Connected(self) -> Bool:
        """
        Returns status of the connection with the UO server: ‘True - connected, ‘False - not connected
        """
        ...

    @method_api(28)
    def GetARStatus(self) -> Bool: ...

    @method_api(29)
    def SetARStatus(self, Value: Bool) -> None: ...

    @method_api(529)
    def SetARExtParams(self, ShardName: String, CharName: String, UseAtEveryConnect: Bool) -> None: ...

    @method_api(21)
    def ConnectedTime(self) -> DateTime: ...

    @method_api(22)
    def DisconnectedTime(self) -> DateTime: ...

    @method_api(23)
    def Connect(self) -> None: ...

    @method_api(24)
    def Disconnect(self) -> None: ...

    ####################################################################################################################
    # events
    ####################################################################################################################
    @method_api(7)
    def SetEventCallback(self, EventIndex: U8) -> None: ...

    @method_api(8)
    def ClearEventCallback(self, EventIndex: U8) -> None: ...

    ####################################################################################################################
    # profile management
    ####################################################################################################################
    @method_api(34)
    def ProfileName(self) -> String: ...

    @method_api(35)
    def ChangeProfile(self, Name: String) -> I32: ...

    @method_api(527)
    def ProfileShardName(self) -> String: ...

    @method_api(528)
    def ChangeProfileEx(self, ProfileName: String, ShardName: String, CharName: String) -> I32: ...

    ####################################################################################################################
    # stealth info
    ####################################################################################################################
    @method_api(86)
    def GetStealthInfo(self) -> AboutData: ...

    @method_api(36)
    def StealthPath(self) -> String: ...

    @method_api(37)
    def GetStealthProfilePath(self) -> String: ...

    ####################################################################################################################
    # main information
    ####################################################################################################################
    @method_api(456)
    def GetQuestArrow(self) -> Point: ...

    @method_api(531)
    def GetCharsListForShard(self) -> list[String]: ...

    @method_api(38)
    def GetShardPath(self) -> String: ...

    @method_api(526)
    def GameServerIPString(self) -> String: ...

    @method_api(200)
    def Self(self) -> U32: ...

    @method_api(204)
    def WorldNum(self) -> U8: ...

    @method_api(32)
    def CharName(self) -> String: ...

    @method_api(218)
    def Str(self) -> I32: ...

    @method_api(219)
    def Int(self) -> I32: ...

    @method_api(220)
    def Dex(self) -> I32: ...

    @method_api(221)
    def Life(self) -> I32: ...

    @method_api(222)
    def Mana(self) -> I32: ...

    @method_api(223)
    def Stam(self) -> I32: ...

    @method_api(224)
    def MaxLife(self) -> I32: ...

    @method_api(225)
    def MaxMana(self) -> I32: ...

    @method_api(226)
    def MaxStam(self) -> I32: ...

    @method_api(227)
    def Luck(self) -> U16: ...

    @method_api(228)
    def Backpack(self) -> U32: ...

    @method_api(229)
    def GetBuffBarInfo(self) -> list[BuffBarInfo]: ...

    @method_api(463)
    def PredictedX(self) -> U16: ...

    @method_api(464)
    def PredictedY(self) -> U16: ...

    @method_api(465)
    def PredictedZ(self) -> I8: ...

    @method_api(466)
    def PredictedDirection(self) -> U8: ...

    @method_api(205)
    def Sex(self) -> U8: ...

    @method_api(206)
    def GetCharTitle(self) -> String: ...

    @method_api(207)
    def Gold(self) -> U32: ...

    @method_api(208)
    def Armor(self) -> U16: ...

    @method_api(209)
    def Weight(self) -> U16: ...

    @method_api(210)
    def MaxWeight(self) -> U16: ...

    @method_api(211)
    def Race(self) -> U8: ...

    @method_api(212)
    def MaxPets(self) -> U8: ...

    @method_api(213)
    def PetsCurrent(self) -> U8: ...

    @method_api(214)
    def FireResist(self) -> U16: ...

    @method_api(215)
    def ColdResist(self) -> U16: ...

    @method_api(216)
    def PoisonResist(self) -> U16: ...

    @method_api(217)
    def EnergyResist(self) -> U16: ...

    @method_api(33)
    def ShardName(self) -> String: ...

    @method_api(317)
    def GetExtInfo(self) -> ExtendedInfo: ...

    @method_api(318)
    def Hidden(self) -> Bool: ...

    @method_api(319)
    def Poisoned(self) -> Bool: ...

    @method_api(320)
    def Paralyzed(self) -> Bool: ...

    @method_api(321)
    def Dead(self) -> Bool: ...

    ####################################################################################################################
    # object information
    ####################################################################################################################
    @method_api(87)
    def IsObjectExists(self, ObjID: U32) -> Bool: ...

    @method_api(201)
    def GetX(self, ObjID: U32) -> U16: ...

    @method_api(202)
    def GetY(self, ObjID: U32) -> U16: ...

    @method_api(203)
    def GetZ(self, ObjID: U32) -> I8: ...

    @method_api(331)
    def GetDirection(self, ObjID: U32) -> U8: ...

    @method_api(332)
    def GetDistance(self, ObjID: U32) -> I32: ...

    @method_api(316)
    def GetPlayerStatusText(self, ObjID: U32) -> String: ...

    @method_api(322)
    def GetName(self, ObjID: U32) -> String: ...

    @method_api(323)
    def GetAltName(self, ObjID: U32) -> String: ...

    @method_api(325)
    def GetTooltip(self, ObjID: U32) -> String: ...

    @method_api(326)
    def GetType(self, ObjID: U32) -> U16: ...

    @method_api(327)
    def GetTooltipRec(self, ObjID: U32) -> list[ClilocRec]: ...

    @method_api(328)
    def GetClilocByID(self, ClilocID: U32, Params: list[String]) -> String: ...

    @method_api(329)
    def GetQuantity(self, ObjID: U32) -> I32: ...

    @method_api(330)
    def GetPrice(self, ObjID: U32) -> U32: ...

    @method_api(333)
    def GetColor(self, ObjID: U32) -> U16: ...

    @method_api(324)
    def GetTitle(self, ObjID: U32) -> String: ...

    @method_api(343)
    def GetNotoriety(self, ObjID: U32) -> U8: ...

    @method_api(334)
    def GetStr(self, ObjID: U32) -> I32: ...

    @method_api(335)
    def GetInt(self, ObjID: U32) -> I32: ...

    @method_api(336)
    def GetDex(self, ObjID: U32) -> I32: ...

    @method_api(337)
    def GetHP(self, ObjID: U32) -> I32: ...

    @method_api(338)
    def GetMaxHP(self, ObjID: U32) -> I32: ...

    @method_api(339)
    def GetMana(self, ObjID: U32) -> I32: ...

    @method_api(340)
    def GetMaxMana(self, ObjID: U32) -> I32: ...

    @method_api(341)
    def GetStam(self, ObjID: U32) -> I32: ...

    @method_api(342)
    def GetMaxStam(self, ObjID: U32) -> I32: ...

    @method_api(344)
    def GetParent(self, ObjID: U32) -> U32: ...

    @method_api(345)
    def IsWarMode(self, ObjID: U32) -> Bool: ...

    @method_api(346)
    def IsNPC(self, ObjID: U32) -> Bool: ...

    @method_api(347)
    def IsDead(self, ObjID: U32) -> Bool: ...

    @method_api(348)
    def IsRunning(self, ObjID: U32) -> Bool: ...

    @method_api(349)
    def IsContainer(self, ObjID: U32) -> Bool: ...

    @method_api(350)
    def IsHidden(self, ObjID: U32) -> Bool: ...

    @method_api(351)
    def IsMovable(self, ObjID: U32) -> Bool: ...

    @method_api(352)
    def IsYellowHits(self, ObjID: U32) -> Bool: ...

    @method_api(353)
    def IsPoisoned(self, ObjID: U32) -> Bool: ...

    @method_api(354)
    def IsParalyzed(self, ObjID: U32) -> Bool: ...

    @method_api(355)
    def IsFemale(self, ObjID: U32) -> Bool: ...

    @method_api(401)
    def ObjAtLayerEx(self, Layer: U8, ObjID: U32) -> U32: ...

    @method_api(402)
    def GetLayer(self, ObjID: U32) -> U8: ...

    @method_api(421)
    def MobileCanBeRenamed(self, MobID: U32) -> Bool: ...

    @method_api(356)
    def IsHouse(self, ObjID: U32) -> Bool: ...

    ####################################################################################################################
    # bulk query
    ####################################################################################################################
    @method_api(533)
    def GetWorldItems(self) -> list[WorldItemData]: ...

    @method_api(534)
    def GetMobiles(self) -> list[MobileData]: ...

    @method_api(535)
    def GetMobile(self, MobID: U32) -> MobileData: ...

    @method_api(536)
    def GetEquipment(self, MobID: U32) -> list[EquippedItemData]: ...

    @method_api(537)
    def GetContent(self, ObjID: U32) -> list[ContentItemData]: ...

    ####################################################################################################################
    # past information
    ####################################################################################################################
    @method_api(230)
    def LastContainer(self) -> U32: ...

    @method_api(231)
    def LastTarget(self) -> U32: ...

    @method_api(232)
    def LastAttack(self) -> U32: ...

    @method_api(233)
    def LastStatus(self) -> U32: ...

    @method_api(234)
    def LastObject(self) -> U32: ...

    ####################################################################################################################
    # journal
    ####################################################################################################################
    @method_api(39)
    def AddToSystemJournal(self, Text: String) -> None: ...

    @method_api(40)
    def AddToSystemJournalEx(self, Text: String, TextColor: I32, BgColor: I32, FontSize: I32, FontName: String) -> None: ...

    @method_api(41)
    def ClearSystemJournal(self) -> None: ...

    @method_api(293)
    def AddJournalIgnore(self, Str: String) -> None: ...

    @method_api(294)
    def ClearJournalIgnore(self) -> None: ...

    @method_api(295)
    def AddChatUserIgnore(self, UserName: String) -> None: ...

    @method_api(296)
    def ClearChatUserIgnore(self) -> None: ...

    @method_api(43)
    def ClearJournal(self) -> None: ...

    @method_api(44)
    def LastJournalMessage(self) -> String: ...

    @method_api(45)
    def InJournal(self, Str: String) -> I32: ...

    @method_api(46)
    def InJournalBetweenTimes(self, Str: String, TimeBegin: DateTime, TimeEnd: DateTime) -> I32: ...

    @method_api(47)
    def Journal(self, StringIndex: I32) -> String: ...

    @method_api(48)
    def SetJournalLine(self, StringIndex: I32, Text: String) -> None: ...

    @method_api(49)
    def LowJournal(self) -> I32: ...

    @method_api(50)
    def HighJournal(self) -> I32: ...

    @method_api(42)
    def AddToJournal(self, Text: String) -> None: ...

    @method_api(51)
    def FoundedParamID(self) -> I32: ...

    @method_api(52)
    def LineID(self) -> U32: ...

    @method_api(53)
    def LineType(self) -> U16: ...

    @method_api(54)
    def LineTime(self) -> DateTime: ...

    @method_api(55)
    def LineMsgType(self) -> U8: ...

    @method_api(56)
    def LineTextColor(self) -> U16: ...

    @method_api(57)
    def LineTextFont(self) -> U16: ...

    @method_api(58)
    def LineIndex(self) -> I32: ...

    @method_api(59)
    def LineCount(self) -> I32: ...

    @method_api(60)
    def LineName(self) -> String: ...

    ####################################################################################################################
    # actions
    ####################################################################################################################
    @method_api(237)
    def Attack(self, ObjID: U32) -> None: ...

    @method_api(238)
    def UseSelfPaperdollScroll(self) -> None: ...

    @method_api(239)
    def UseOtherPaperdollScroll(self, ObjID: U32) -> None: ...

    @method_api(267)
    def RequestStats(self, ObjID: U32) -> None: ...

    @method_api(268)
    def HelpRequest(self) -> None: ...

    @method_api(269)
    def QuestRequest(self) -> None: ...

    @method_api(270)
    def ToggleFly(self) -> None: ...

    @method_api(271)
    def ReqVirtuesGump(self) -> None: ...

    @method_api(272)
    def UseVirtue(self, VirtueID: U32) -> None: ...

    @method_api(273)
    def UseObject(self, ObjID: U32) -> None: ...

    @method_api(274)
    def UseType(self, ObjType: U16, Color: U16) -> U32: ...

    @method_api(275)
    def UseFromGround(self, ObjType: U16, Color: U16) -> U32: ...

    @method_api(276)
    def ClickOnObject(self, ObjID: U32) -> None: ...

    @method_api(262)
    def Cast(self, SpellID: I32) -> None: ...

    @method_api(280)
    def OpenDoor(self) -> None: ...

    @method_api(281)
    def Bow(self) -> None: ...

    @method_api(282)
    def Salute(self) -> None: ...

    @method_api(420)
    def RenameMobile(self, MobID: U32, NewName: String) -> None: ...

    @method_api(459)
    def UOSay(self, Text: String) -> None: ...

    @method_api(460)
    def UOSayColor(self, Text: String, Color: U16) -> None: ...

    @method_api(277)
    def UseItemOnMobile(self, ItemSerial: U32, TargetSerial: U32) -> None: ...

    @method_api(278)
    def BandageSelf(self) -> None: ...

    ####################################################################################################################
    # skills related functions
    ####################################################################################################################
    @method_api(260)
    def GetSkillID(self, SkillName: String) -> I32: ...

    @method_api(261)
    def UseSkill(self, SkillID: I32) -> None: ...

    @method_api(256)
    def SetSkillLockState(self, SkillID: I32, skillState: U8) -> None: ...

    @method_api(258)
    def GetSkillCap(self, SkillID: I32) -> F64: ...

    @method_api(259)
    def GetSkillValue(self, SkillID: I32) -> F64: ...

    @method_api(257)
    def GetSkillCurrentValue(self, SkillID: I32) -> F64: ...

    @method_api(255)
    def GetSkillLockState(self, SkillID: I32) -> I8: ...

    ####################################################################################################################
    # search and all that
    ####################################################################################################################
    @method_api(297)
    def SetFindDistance(self, Value: U32) -> None: ...

    @method_api(298)
    def GetFindDistance(self) -> U32: ...

    @method_api(299)
    def SetFindVertical(self, Value: U32) -> None: ...

    @method_api(300)
    def GetFindVertical(self) -> U32: ...

    @method_api(301)
    def FindTypeEx(self, ObjType: U16, Color: U16, Container: U32, InSub: Bool) -> U32: ...

    @method_api(302)
    def FindTypesArrayEx(self, ObjTypes: list[U16], Colors: list[U16], Containers: list[U32], InSub: Bool) -> U32: ...

    @method_api(303)
    def FindNotoriety(self, ObjType: U16, Notoriety: U8) -> U32: ...

    @method_api(305)
    def Ignore(self, ObjID: U32) -> None: ...

    @method_api(304)
    def FindAtCoord(self, X: U16, Y: U16) -> U32: ...

    @method_api(306)
    def IgnoreOff(self, ObjID: U32) -> None: ...

    @method_api(307)
    def IgnoreReset(self) -> None: ...

    @method_api(308)
    def GetIgnoreList(self) -> list[U32]: ...

    @method_api(309)
    def GetFindedList(self) -> list[U32]: ...

    @method_api(310)
    def FindItem(self) -> U32: ...

    @method_api(311)
    def FindCount(self) -> I32: ...

    @method_api(312)
    def FindQuantity(self) -> I32: ...

    @method_api(313)
    def FindFullQuantity(self) -> I32: ...

    @method_api(314)
    def SetFindInNulPoint(self, Value: Bool) -> None: ...

    @method_api(315)
    def GetFindInNulPoint(self) -> Bool: ...

    ####################################################################################################################
    # multis
    ####################################################################################################################
    @method_api(517)
    def GetMultiPartsAtPosition(self, X: U16, Y: U16) -> list[MultiPart]: ...

    @method_api(518)
    def GetMultiAllParts(self, MultiID: U32) -> list[MultiPart]: ...

    @method_api(516)
    def GetMultis(self) -> list[Multi]: ...

    ####################################################################################################################
    # movement
    ####################################################################################################################
    @method_api(467)
    def SetMoveOpenDoor(self, Value: Bool) -> None: ...

    @method_api(468)
    def GetMoveOpenDoor(self) -> Bool: ...

    @method_api(469)
    def SetMoveThroughNPC(self, Value: U16) -> None: ...

    @method_api(470)
    def GetMoveThroughNPC(self) -> U16: ...

    @method_api(471)
    def SetMoveThroughCorner(self, Value: Bool) -> None: ...

    @method_api(472)
    def GetMoveThroughCorner(self) -> Bool: ...

    @method_api(473)
    def SetMoveHeuristicMult(self, Value: I32) -> None: ...

    @method_api(474)
    def GetMoveHeuristicMult(self) -> I32: ...

    @method_api(475)
    def SetMoveCheckStamina(self, Value: U16) -> None: ...

    @method_api(476)
    def GetMoveCheckStamina(self) -> U16: ...

    @method_api(477)
    def SetMoveTurnCost(self, Value: I32) -> None: ...

    @method_api(478)
    def GetMoveTurnCost(self) -> I32: ...

    @method_api(479)
    def SetMoveBetweenTwoCorners(self, Value: Bool) -> None: ...

    @method_api(480)
    def GetMoveBetweenTwoCorners(self) -> Bool: ...

    @method_api(481)
    def SetRunUnmountTimer(self, Value: U16) -> None: ...

    @method_api(482)
    def SetWalkMountTimer(self, Value: U16) -> None: ...

    @method_api(483)
    def SetRunMountTimer(self, Value: U16) -> None: ...

    @method_api(484)
    def SetWalkUnmountTimer(self, Value: U16) -> None: ...

    @method_api(485)
    def GetRunMountTimer(self) -> U16: ...

    @method_api(486)
    def GetWalkMountTimer(self) -> U16: ...

    @method_api(487)
    def GetRunUnmountTimer(self) -> U16: ...

    @method_api(488)
    def GetWalkUnmountTimer(self) -> U16: ...

    @method_api(490)
    def Step(self, Direction: U8, Running: Bool) -> U8: ...

    @method_api(491)
    def StepQ(self, Direction: U8, Running: Bool) -> I32: ...

    @method_api(492)
    def MoveXYZ(self, Xdst: U16, Ydst: U16, Zdst: I8, AccuracyXY: I32, AccuracyZ: I32, Running: Bool) -> Bool: ...

    @method_api(493)
    def MoveXY(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32, Running: Bool) -> Bool: ...

    @method_api(502)
    def MoverStop(self) -> None: ...

    @method_api(503)
    def GetLastStepQUsedDoor(self) -> U32: ...

    ####################################################################################################################
    # pathfinding, los
    ####################################################################################################################

    @method_api(438)
    def IsWorldCellPassable(self, CurrX: U16, CurrY: U16, CurrZ: I8, DestX: U16, DestY: U16, WorldNum: U8) -> tuple[Bool, I8]: ...

    @method_api(499)
    def CheckLOS(self, Xfrom: U16, Yfrom: U16, Zfrom: I8, Xto: U16, Yto: U16, Zto: I8, WorldNum: U8, CheckType: U8, Options: U32) -> Bool: ...

    @method_api(500)
    def GetPathArray(self, Xdst: U16, Ydst: U16, Optimized: Bool, Accuracy: I32) -> list[WorldPoint]: ...

    @method_api(501)
    def GetPathArray3D(self,
                       StartX: U16, StartY: U16, StartZ: I8,
                       FinishX: U16, FinishY: U16, FinishZ: I8,
                       WorldNum: U8,
                       AccuracyXY: I32, AccuracyZ: I32,
                       Run: Bool) -> list[WorldPoint]: ...


    @method_api(489)
    def GetNextStepZ(self, CurrX: U16, CurrY: U16, DestX: U16, DestY: U16, WorldNum: U8, CurrZ: I8) -> I8: ...

    @method_api(494)
    def SetBadLocation(self, X: U16, Y: U16) -> None: ...

    @method_api(495)
    def SetGoodLocation(self, X: U16, Y: U16) -> None: ...

    @method_api(496)
    def ClearBadLocationList(self) -> None: ...

    @method_api(497)
    def SetBadObject(self, ObjType: U16, Color: U16, Radius: U8) -> None: ...

    @method_api(498)
    def ClearBadObjectList(self) -> None: ...

    ####################################################################################################################
    # map, statics, tile data
    ####################################################################################################################
    @method_api(439)
    def GetStaticTilesArray(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: list[U16]) -> list[FoundTile]: ...

    @method_api(440)
    def GetLandTilesArray(self, Xmin: U16, Ymin: U16, Xmax: U16, Ymax: U16, WorldNum: U8, TileTypes: list[U16]) -> list[FoundTile]: ...

    @method_api(432)
    def GetTileFlags(self, Group: U8, Tile: U16) -> U32: ...

    @method_api(433)
    def GetLandTileData(self, Tile: U16) -> LandTileData: ...

    @method_api(434)
    def GetStaticTileData(self, Tile: U16) -> StaticTileData: ...

    @method_api(435)
    def GetLayerCount(self, X: U16, Y: U16, WorldNum: U8) -> U8: ...

    @method_api(436)
    def ReadStaticsXY(self, X: U16, Y: U16, WorldNum: U8) -> list[StaticItemRealXY]: ...

    @method_api(437)
    def GetSurfaceZ(self, X: U16, Y: U16, WorldNum: U8) -> I8: ...

    @method_api(441)
    def GetCell(self, X: U16, Y: U16, WorldNum: U8) -> MapCell: ...

    @method_api(442)
    def ConvertIntegerToFlags(self, Group: U8, Flags: U32) -> list[String]: ...

    ####################################################################################################################
    # gumps
    ####################################################################################################################
    @method_api(379)
    def WaitGump(self, Value: I32) -> None: ...

    @method_api(380)
    def WaitTextEntry(self, Value: String) -> None: ...

    @method_api(381)
    def GumpAutoTextEntry(self, TextEntryID: I32, Value: String) -> None: ...

    @method_api(382)
    def GumpAutoRadiobutton(self, RadiobuttonID: I32, Value: I32) -> None: ...

    @method_api(383)
    def GumpAutoCheckBox(self, CheckBoxID: I32, Value: I32) -> None: ...

    @method_api(384)
    def NumGumpButton(self, GumpIndex: U16, Value: I32) -> Bool: ...

    @method_api(385)
    def NumGumpTextEntry(self, GumpIndex: U16, TextEntryID: I32, Value: String) -> Bool: ...

    @method_api(386)
    def NumGumpRadiobutton(self, GumpIndex: U16, RadiobuttonID: I32, Value: I32) -> Bool: ...

    @method_api(387)
    def NumGumpCheckBox(self, GumpIndex: U16, CBID: I32, Value: I32) -> Bool: ...

    @method_api(388)
    def GetGumpsCount(self) -> U16: ...

    @method_api(389)
    def CloseSimpleGump(self, GumpIndex: U16) -> None: ...

    @method_api(390)
    def GetGumpSerial(self, GumpIndex: U16) -> U32: ...

    @method_api(391)
    def GetGumpID(self, GumpIndex: U16) -> U32: ...

    @method_api(392)
    def IsGumpCanBeClosed(self, GumpIndex: U16) -> Bool: ...

    @method_api(393)
    def GetGumpTextLines(self, GumpIndex: U16) -> list[String]: ...

    @method_api(394)
    def GetGumpFullLines(self, GumpIndex: U16) -> list[String]: ...

    @method_api(395)
    def GetGumpShortLines(self, GumpIndex: U16) -> list[String]: ...

    @method_api(396)
    def GetGumpButtonsDescription(self, GumpIndex: U16) -> list[String]: ...

    @method_api(397)
    def GetGumpInfo(self, GumpIndex: U16) -> GumpInfo: ...

    @method_api(398)
    def AddGumpIgnoreByID(self, GumpID: U32) -> None: ...

    @method_api(399)
    def AddGumpIgnoreBySerial(self, Serial: U32) -> None: ...

    @method_api(400)
    def ClearGumpsIgnore(self) -> None: ...

    ####################################################################################################################
    # menu
    ####################################################################################################################
    @method_api(370)
    def WaitMenu(self, MenuCaption: String, ElementCaption: String) -> None: ...

    @method_api(371)
    def AutoMenu(self, MenuCaption: String, ElementCaption: String) -> None: ...

    @method_api(372)
    def MenuHookPresent(self) -> Bool: ...

    @method_api(373)
    def MenuPresent(self) -> Bool: ...

    @method_api(374)
    def CancelMenu(self) -> None: ...

    @method_api(375)
    def CloseMenu(self) -> None: ...

    @method_api(376)
    def GetMenuItems(self, Caption: String) -> list[String]: ...

    @method_api(378)
    def GetLastMenuItems(self) -> list[String]: ...

    @method_api(377)
    def GetMenuItemsEx(self, Caption: String) -> list[MenuItem]: ...

    ####################################################################################################################
    # context menu
    ####################################################################################################################
    @method_api(357)
    def RequestContextMenu(self, ObjID: U32) -> None: ...

    @method_api(358)
    def SetContextMenuHook(self, MenuID: U32, EntryNumber: U8) -> None: ...

    @method_api(359)
    def GetContextMenu(self) -> list[String]: ...

    @method_api(360)
    def ClearContextMenu(self) -> None: ...

    @method_api(361)
    def GetContextMenuRec(self) -> ContextMenuRec: ...


    ####################################################################################################################
    # scripts management
    ####################################################################################################################
    @method_api(30)
    def GetPauseScriptOnDisconnectStatus(self) -> Bool: ...

    @method_api(31)
    def SetPauseScriptOnDisconnectStatus(self, Value: Bool) -> None: ...

    @method_api(67)
    def GetScriptCount(self) -> U16: ...

    @method_api(68)
    def GetScriptPath(self, ScriptIndex: U16) -> String: ...

    @method_api(69)
    def GetScriptState(self, ScriptIndex: U16) -> U8: ...

    @method_api(70)
    def StartScript(self, ScriptPath: String) -> U16: ...

    @method_api(71)
    def StopScript(self, ScriptIndex: U16) -> None: ...

    @method_api(72)
    def PauseResumeSelScript (self, ScriptIndex: U16) -> None: ...

    @method_api(73)
    def StopAllScripts(self) -> None: ...

    @method_api(74)
    def SetScriptName(self, ScriptIndex: U16, Value: String) -> None: ...

    @method_api(75)
    def GetScriptName(self, ScriptIndex: U16) -> String: ...

    @method_api(76)
    def GetScriptParams(self) -> U32: ...

    @method_api(77)
    def GetScriptsList(self) -> list[ScriptInfo]: ...

    ####################################################################################################################
    # map drawing
    ####################################################################################################################
    @method_api(522)
    def AddFigure(self, Figure: MapFigure) -> U32: ...

    @method_api(523)
    def RemoveFigure(self, FigureID: U32) -> Bool: ...

    @method_api(524)
    def UpdateFigure(self, FigureID: U32, Figure: MapFigure) -> Bool: ...

    @method_api(525)
    def ClearFigures(self) -> None: ...

    ####################################################################################################################
    # books management
    ####################################################################################################################
    @method_api(504)
    def BookGetPageText(self, Page: U16) -> String: ...

    @method_api(505)
    def BookSetText(self, Text: String) -> None: ...

    @method_api(506)
    def BookSetPageText(self, Page: U16, Text: String) -> None: ...

    @method_api(507)
    def BookClearText(self) -> None: ...

    @method_api(508)
    def BookSetHeader(self, Title: String, Author: String) -> None: ...

    ####################################################################################################################
    # party related functions
    ####################################################################################################################
    @method_api(422)
    def InviteToParty(self, ObjID: U32) -> None: ...

    @method_api(423)
    def RemoveFromParty(self, ObjID: U32) -> None: ...

    @method_api(424)
    def PartyPrivateMessageTo(self, ObjID: U32, Msg: String) -> None: ...

    @method_api(425)
    def PartySay(self, Msg: String) -> None: ...

    @method_api(426)
    def PartyCanLootMe(self, Value: Bool) -> None: ...

    @method_api(427)
    def PartyAcceptInvite(self) -> None: ...

    @method_api(428)
    def PartyDeclineInvite(self) -> None: ...

    @method_api(429)
    def PartyLeave(self) -> None: ...

    @method_api(430)
    def PartyMembersList(self) -> list[U32]: ...

    @method_api(431)
    def InParty(self) -> Bool: ...

    ####################################################################################################################
    # targets
    ####################################################################################################################
    @method_api(240)
    def TargetID(self) -> U32: ...

    @method_api(241)
    def CancelTarget(self) -> None: ...

    @method_api(242)
    def TargetToObject(self, ObjID: U32) -> None: ...

    @method_api(243)
    def TargetToXYZ(self, X: U16, Y: U16, Z: I8) -> None: ...

    @method_api(244)
    def TargetToTile(self, Tile: U16, X: U16, Y: U16, Z: I8) -> None: ...

    @method_api(245)
    def WaitTargetObject(self, ObjID: U32) -> None: ...

    @method_api(246)
    def WaitTargetTile(self, Tile: U16, X: U16, Y: U16, Z: I8) -> None: ...

    @method_api(247)
    def WaitTargetXYZ(self, X: U16, Y: U16, Z: I8) -> None: ...

    @method_api(248)
    def WaitTargetSelf(self) -> None: ...

    @method_api(249)
    def WaitTargetType(self, ObjType: U16) -> None: ...

    @method_api(250)
    def CancelWaitTarget(self) -> None: ...

    @method_api(251)
    def WaitTargetGround(self, ObjType: U16) -> None: ...

    @method_api(252)
    def WaitTargetLast(self) -> None: ...

    @method_api(279)
    def TargetByResource(self, ObjID: U32, Resource: U16) -> None: ...

    ####################################################################################################################
    # item manipulations
    ####################################################################################################################
    @method_api(285)
    def GetPickupedItem(self) -> U32: ...

    @method_api(286)
    def SetPickupedItem(self, ObjID: U32) -> None: ...

    @method_api(287)
    def GetDropCheckCoord(self) -> Bool: ...

    @method_api(288)
    def SetDropCheckCoord(self, Value: Bool) -> None: ...

    @method_api(289)
    def GetDropDelay(self) -> U32: ...

    @method_api(290)
    def SetDropDelay(self, Value: U32) -> None: ...

    @method_api(291)
    def DragItem(self, ObjID: U32, Count: I32) -> Bool: ...

    @method_api(292)
    def DropItem(self, MoveIntoID: U32, X: I32, Y: I32, Z: I8) -> Bool: ...

    @method_api(403)
    def WearItem(self, Layer: U8, ObjID: U32) -> Bool: ...

    @method_api(404)
    def GetDressSpeed(self) -> U16: ...

    @method_api(405)
    def SetDressSpeed(self, Value: U16) -> None: ...

    @method_api(406)
    def SetDress(self) -> None: ...

    @method_api(407)
    def GetDressSet(self) -> list[LayerObject]: ...

    @method_api(408)
    def UnequipItemsSetMacro(self) -> None: ...

    @method_api(409)
    def EquipItemsSetMacro(self) -> None: ...

    @method_api(410)
    def EquipLastWeapon(self) -> None: ...

    @method_api(538)
    def EquipItems(self, Items: list[U32]) -> Bool: ...

    @method_api(539)
    def UnequipItems(self, Items: list[U32]) -> Bool: ...

    ####################################################################################################################
    # trade
    ####################################################################################################################
    @method_api(362)
    def IsTrade(self) -> Bool: ...

    @method_api(363)
    def GetTradeContainer(self, TradeNum: U8, Num: U8) -> U32: ...

    @method_api(364)
    def GetTradeOpponent(self, TradeNum: U8) -> U32: ...

    @method_api(365)
    def TradeCount(self) -> U8: ...

    @method_api(366)
    def GetTradeOpponentName(self, TradeNum: U8) -> String: ...

    @method_api(367)
    def TradeCheck(self, TradeNum: U8, Num: U8) -> Bool: ...

    @method_api(368)
    def ConfirmTrade(self, TradeNum: U8) -> None: ...

    @method_api(369)
    def CancelTrade(self, TradeNum: U8) -> Bool: ...

    ####################################################################################################################
    # buy/sell
    ####################################################################################################################
    @method_api(411)
    def AutoBuy(self, ItemType: U16, ItemColor: U16, Quantity: U16) -> None: ...

    @method_api(412)
    def GetShopList(self) -> list[String]: ...

    @method_api(413)
    def ClearShopList(self) -> None: ...

    @method_api(414)
    def AutoBuyEx(self, ItemType: U16, ItemColor: U16, Quantity: U16, Price: U32, Name: String) -> None: ...

    @method_api(415)
    def GetAutoBuyDelay(self) -> U16: ...

    @method_api(416)
    def SetAutoBuyDelay(self, Value: U16) -> None: ...

    @method_api(417)
    def GetAutoSellDelay(self) -> U16: ...

    @method_api(418)
    def SetAutoSellDelay(self, Value: U16) -> None: ...

    @method_api(419)
    def AutoSell(self, ItemType: U16, ItemColor: U16, Quantity: U16) -> None: ...

    ####################################################################################################################
    # global chat
    ####################################################################################################################
    @method_api(509)
    def GlobalChatJoinChannel(self, ChName: String) -> None: ...

    @method_api(510)
    def GlobalChatLeaveChannel(self) -> None: ...

    @method_api(511)
    def GlobalChatSendMsg(self, MsgText: String) -> None: ...

    @method_api(512)
    def GlobalChatActiveChannel(self) -> String: ...

    @method_api(513)
    def GlobalChatChannelsList(self) -> list[String]: ...

    ####################################################################################################################
    # proxy related
    ####################################################################################################################
    @method_api(25)
    def ProxyIP(self) -> String: ...

    @method_api(26)
    def ProxyPort(self) -> U16: ...

    @method_api(27)
    def UseProxy(self) -> Bool: ...

    ####################################################################################################################
    # client interaction
    ####################################################################################################################
    @method_api(446)
    def ClientPrint(self, Text: String) -> None: ...

    @method_api(447)
    def ClientPrintEx(self, SenderID: U32, Color: U16, Font: U16, Text: String) -> None: ...

    @method_api(448)
    def CloseClientUIWindow(self, UIWindowType: U8, ID: U32) -> None: ...

    @method_api(449)
    def ClientRequestObjectTarget(self) -> None: ...

    @method_api(450)
    def ClientRequestTileTarget(self) -> None: ...

    @method_api(451)
    def ClientTargetResponsePresent(self) -> Bool: ...

    @method_api(452)
    def ClientTargetResponse(self) -> TargetInfo: ...

    @method_api(444)
    def CloseClientGump(self, ID: U32) -> None: ...

    @method_api(445)
    def ClientHide(self, ObjID: U32) -> Bool: ...

    @method_api(532)
    def GetClientVersionInt(self) -> I32: ...

    ####################################################################################################################
    # UserStatic functions
    ####################################################################################################################
    @method_api(519)
    def CreateUserStatic(self, StaticItem: UserStaticItem, WorldNum: U8) -> I32: ...

    @method_api(520)
    def RemoveUserStatic(self, StaticID: I32) -> Bool: ...

    @method_api(521)
    def ClearUserStatics(self) -> None: ...

    ####################################################################################################################
    # abilities functions
    ####################################################################################################################
    @method_api(264)
    def UsePrimaryAbility(self) -> None: ...

    @method_api(265)
    def UseSecondaryAbility(self) -> None: ...

    @method_api(266)
    def GetActiveAbility(self) -> String: ...

    @method_api(263)
    def IsActiveSpellAbility(self, SpellID: I32) -> Bool: ...


    ####################################################################################################################
    # http functions
    ####################################################################################################################
    @method_api(61)
    def HTTP_Get(self, URL: String) -> None: ...

    @method_api(62)
    def HTTP_Post(self, URL: String, PostData: String) -> String: ...

    @method_api(63)
    def HTTP_Body(self) -> String: ...

    @method_api(64)
    def HTTP_Header(self) -> String: ...

    ####################################################################################################################
    # war functions
    ####################################################################################################################
    @method_api(235)
    def WarTargetID(self) -> U32: ...

    @method_api(236)
    def SetWarMode(self, Value: Bool) -> None: ...

    ####################################################################################################################
    # messenger functions
    ####################################################################################################################
    @method_api(80)
    def MessengerGetConnected(self, MesID: U8) -> Bool: ...

    @method_api(81)
    def MessengerSetConnected(self, MesID: U8, Value: Bool) -> None: ...

    @method_api(82)
    def MessengerGetToken(self, MesID: U8) -> String: ...

    @method_api(83)
    def MessengerSetToken(self, MesID: U8, Value: String) -> None: ...

    @method_api(84)
    def MessengerGetName(self, MesID: U8) -> String: ...

    @method_api(85)
    def MessengerSendMessage(self, MesID: U8, Msg: String, UserID: String) -> None: ...

    ####################################################################################################################
    # timestamp functions
    ####################################################################################################################
    @method_api(90)
    def GetNowUnix(self) -> I64: ...

    @method_api(91)
    def GetNow(self) -> DateTime: ...

    ####################################################################################################################
    # global variable functions
    ####################################################################################################################
    @method_api(65)
    def SetGlobal(self, GlobalRegion: U8, VarName: String, VarValue: String) -> None: ...

    @method_api(66)
    def GetGlobal(self, GlobalRegion: U8, VarName: String) -> String: ...

    ####################################################################################################################
    # stats state management functions
    ####################################################################################################################
    @method_api(253)
    def GetStatLockState(self, statNum: U8) -> I8: ...

    @method_api(254)
    def SetStatState(self, statNum: U8, statState: U8) -> None: ...

    ####################################################################################################################
    # console reply functions
    ####################################################################################################################
    @method_api(461)
    def ConsoleEntryReply(self, Text: String) -> None: ...

    @method_api(462)
    def ConsoleEntryUnicodeReply(self, Text: String) -> None: ...

    ####################################################################################################################
    # check-lag functions
    ####################################################################################################################
    @method_api(453)
    def CheckLagBegin(self) -> None: ...

    @method_api(454)
    def CheckLagEnd(self) -> None: ...

    @method_api(455)
    def IsCheckLagEnd(self) -> Bool: ...

    ####################################################################################################################
    # uncategorized functions
    ####################################################################################################################
    @method_api(89)
    def Alarm(self) -> None: ...

    @method_api(78)
    def GetShowIPCExceptionWindow(self) -> Bool: ...

    @method_api(79)
    def SetShowIPCExceptionWindow(self, Value: Bool) -> None: ...

    @method_api(283)
    def SetCatchBag(self, ObjID: U32) -> U8: ...

    @method_api(284)
    def UnsetCatchBag(self) -> None: ...

    @method_api(514)
    def FillNewWindow(self, Text: String) -> None: ...

    @method_api(515)
    def ClearInfoWindow(self) -> None: ...

    @method_api(457)
    def SetSilentMode(self, Value: Bool) -> None: ...

    @method_api(458)
    def GetSilentMode(self) -> Bool: ...

    @method_api(443)
    def GetStaticArtBitmap(self, ObjType: U32, Hue: U16) -> list[U8]: ...

    @method_api(530)
    def CreateChar(self,
                   ProfileName: String,
                   ShardName: String,
                   CharName: String,
                   Gender: Bool,
                   Race: I8,
                   Strn: I8, Dex: I8, Int: I8,
                   Skill1: String, Skill2: String, Skill3: String, Skill4: String,
                   SkillValue1: I32, SkillValue2: I32, SkillValue3: I32, SkillValue4: I32,
                   City: I8, Slot: U32) -> None: ...
