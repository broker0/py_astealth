###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from py_astealth.stealth_enums import *
from datetime import datetime


class SyncInterface:
    """Base class defining the interface of StealthApi."""

    def AddChatUserIgnore(self, UserName: str) -> None: pass
    def AddFigure(self, Figure: MapFigure) -> int: pass
    def AddGumpIgnoreByID(self, GumpID: int) -> None: pass
    def AddGumpIgnoreBySerial(self, Serial: int) -> None: pass
    def AddJournalIgnore(self, Str: str) -> None: pass
    def AddToJournal(self, Text: str) -> None: pass
    def AddToSystemJournal(self, Text: str) -> None: pass
    def AddToSystemJournalEx(self, Text: str, TextColor: int, BgColor: int, FontSize: int, FontName: str) -> None: pass
    def Alarm(self) -> None: pass
    def Armor(self) -> int: pass
    def Attack(self, ObjID: int) -> None: pass
    def AutoBuy(self, ItemType: int, ItemColor: int, Quantity: int) -> None: pass
    def AutoBuyEx(self, ItemType: int, ItemColor: int, Quantity: int, Price: int, Name: str) -> None: pass
    def AutoMenu(self, MenuCaption: str, ElementCaption: str) -> None: pass
    def AutoSell(self, ItemType: int, ItemColor: int, Quantity: int) -> None: pass
    def Backpack(self) -> int: pass
    def BandageSelf(self) -> None: pass
    def BookClearText(self) -> None: pass
    def BookGetPageText(self, Page: int) -> str: pass
    def BookSetHeader(self, Title: str, Author: str) -> None: pass
    def BookSetPageText(self, Page: int, Text: str) -> None: pass
    def BookSetText(self, Text: str) -> None: pass
    def Bow(self) -> None: pass
    def CancelMenu(self) -> None: pass
    def CancelTarget(self) -> None: pass
    def CancelTrade(self, TradeNum: int) -> bool: pass
    def CancelWaitTarget(self) -> None: pass
    def Cast(self, SpellID: int) -> None: pass
    def ChangeProfile(self, Name: str) -> int: pass
    def ChangeProfileEx(self, ProfileName: str, ShardName: str, CharName: str) -> int: pass
    def CharName(self) -> str: pass
    def CheckLOS(self, Xfrom: int, Yfrom: int, Zfrom: int, Xto: int, Yto: int, Zto: int, WorldNum: int, CheckType: int, Options: int) -> bool: pass
    def CheckLagBegin(self) -> None: pass
    def CheckLagEnd(self) -> None: pass
    def ClearBadLocationList(self) -> None: pass
    def ClearBadObjectList(self) -> None: pass
    def ClearChatUserIgnore(self) -> None: pass
    def ClearContextMenu(self) -> None: pass
    def ClearEventCallback(self, EventIndex: int) -> None: pass
    def ClearFigures(self) -> None: pass
    def ClearGumpsIgnore(self) -> None: pass
    def ClearInfoWindow(self) -> None: pass
    def ClearJournal(self) -> None: pass
    def ClearJournalIgnore(self) -> None: pass
    def ClearShopList(self) -> None: pass
    def ClearSystemJournal(self) -> None: pass
    def ClearUserStatics(self) -> None: pass
    def ClickOnObject(self, ObjID: int) -> None: pass
    def ClientHide(self, ObjID: int) -> bool: pass
    def ClientPrint(self, Text: str) -> None: pass
    def ClientPrintEx(self, SenderID: int, Color: int, Font: int, Text: str) -> None: pass
    def ClientRequestObjectTarget(self) -> None: pass
    def ClientRequestTileTarget(self) -> None: pass
    def ClientTargetResponse(self) -> TargetInfo: pass
    def ClientTargetResponsePresent(self) -> bool: pass
    def CloseClientGump(self, ID: int) -> None: pass
    def CloseClientUIWindow(self, UIWindowType: int, ID: int) -> None: pass
    def CloseMenu(self) -> None: pass
    def CloseSimpleGump(self, GumpIndex: int) -> None: pass
    def ColdResist(self) -> int: pass
    def ConfirmTrade(self, TradeNum: int) -> None: pass
    def Connect(self) -> None: pass
    def Connected(self) -> bool: pass
    def ConnectedTime(self) -> datetime: pass
    def ConsoleEntryReply(self, Text: str) -> None: pass
    def ConsoleEntryUnicodeReply(self, Text: str) -> None: pass
    def ConvertIntegerToFlags(self, Group: int, Flags: int) -> list[str]: pass
    def CreateChar(self, ProfileName: str, ShardName: str, CharName: str, Gender: bool, Race: int, Strn: int, Dex: int, Int: int, Skill1: str, Skill2: str, Skill3: str, Skill4: str, SkillValue1: int, SkillValue2: int, SkillValue3: int, SkillValue4: int, City: int, Slot: int) -> None: pass
    def CreateUserStatic(self, StaticItem: UserStaticItem, WorldNum: int) -> int: pass
    def Dead(self) -> bool: pass
    def Dex(self) -> int: pass
    def Disconnect(self) -> None: pass
    def DisconnectedTime(self) -> datetime: pass
    def DragItem(self, ObjID: int, Count: int) -> bool: pass
    def DropItem(self, MoveIntoID: int, X: int, Y: int, Z: int) -> bool: pass
    def EnergyResist(self) -> int: pass
    def EquipItemsSetMacro(self) -> None: pass
    def EquipLastWeapon(self) -> None: pass
    def FillNewWindow(self, Text: str) -> None: pass
    def FindAtCoord(self, X: int, Y: int) -> int: pass
    def FindCount(self) -> int: pass
    def FindFullQuantity(self) -> int: pass
    def FindItem(self) -> int: pass
    def FindNotoriety(self, ObjType: int, Notoriety: int) -> int: pass
    def FindQuantity(self) -> int: pass
    def FindTypeEx(self, ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
    def FindTypesArrayEx(self, ObjTypes: list[int], Colors: list[int], Containers: list[int], InSub: bool) -> int: pass
    def FireResist(self) -> int: pass
    def FoundedParamID(self) -> int: pass
    def GameServerIPString(self) -> str: pass
    def GetARStatus(self) -> bool: pass
    def GetActiveAbility(self) -> str: pass
    def GetAltName(self, ObjID: int) -> str: pass
    def GetAutoBuyDelay(self) -> int: pass
    def GetAutoSellDelay(self) -> int: pass
    def GetBuffBarInfo(self) -> list[BuffBarInfo]: pass
    def GetCell(self, X: int, Y: int, WorldNum: int) -> MapCell: pass
    def GetCharTitle(self) -> str: pass
    def GetCharsListForShard(self) -> list[str]: pass
    def GetClientVersionInt(self) -> int: pass
    def GetClilocByID(self, ClilocID: int, Params: list[str]) -> str: pass
    def GetColor(self, ObjID: int) -> int: pass
    def GetContextMenu(self) -> list[str]: pass
    def GetContextMenuRec(self) -> ContextMenuRec: pass
    def GetDex(self, ObjID: int) -> int: pass
    def GetDirection(self, ObjID: int) -> int: pass
    def GetDistance(self, ObjID: int) -> int: pass
    def GetDressSet(self) -> list[LayerObject]: pass
    def GetDressSpeed(self) -> int: pass
    def GetDropCheckCoord(self) -> bool: pass
    def GetDropDelay(self) -> int: pass
    def GetExtInfo(self) -> ExtendedInfo: pass
    def GetFindDistance(self) -> int: pass
    def GetFindInNulPoint(self) -> bool: pass
    def GetFindVertical(self) -> int: pass
    def GetFindedList(self) -> list[int]: pass
    def GetGlobal(self, GlobalRegion: int, VarName: str) -> str: pass
    def GetGumpButtonsDescription(self, GumpIndex: int) -> list[str]: pass
    def GetGumpFullLines(self, GumpIndex: int) -> list[str]: pass
    def GetGumpID(self, GumpIndex: int) -> int: pass
    def GetGumpInfo(self, GumpIndex: int) -> GumpInfo: pass
    def GetGumpSerial(self, GumpIndex: int) -> int: pass
    def GetGumpShortLines(self, GumpIndex: int) -> list[str]: pass
    def GetGumpTextLines(self, GumpIndex: int) -> list[str]: pass
    def GetGumpsCount(self) -> int: pass
    def GetHP(self, ObjID: int) -> int: pass
    def GetIgnoreList(self) -> list[int]: pass
    def GetInt(self, ObjID: int) -> int: pass
    def GetLandTileData(self, Tile: int) -> LandTileData: pass
    def GetLandTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
    def GetLastMenuItems(self) -> list[str]: pass
    def GetLastStepQUsedDoor(self) -> int: pass
    def GetLayer(self, ObjID: int) -> int: pass
    def GetLayerCount(self, X: int, Y: int, WorldNum: int) -> int: pass
    def GetMana(self, ObjID: int) -> int: pass
    def GetMaxHP(self, ObjID: int) -> int: pass
    def GetMaxMana(self, ObjID: int) -> int: pass
    def GetMaxStam(self, ObjID: int) -> int: pass
    def GetMenuItems(self, Caption: str) -> list[str]: pass
    def GetMenuItemsEx(self, Caption: str) -> list[MenuItem]: pass
    def GetMoveBetweenTwoCorners(self) -> bool: pass
    def GetMoveCheckStamina(self) -> int: pass
    def GetMoveHeuristicMult(self) -> int: pass
    def GetMoveOpenDoor(self) -> bool: pass
    def GetMoveThroughCorner(self) -> bool: pass
    def GetMoveThroughNPC(self) -> int: pass
    def GetMoveTurnCost(self) -> int: pass
    def GetMultiAllParts(self, MultiID: int) -> list[MultiPart]: pass
    def GetMultiPartsAtPosition(self, X: int, Y: int) -> list[MultiPart]: pass
    def GetMultis(self) -> list[Multi]: pass
    def GetName(self, ObjID: int) -> str: pass
    def GetNextStepZ(self, CurrX: int, CurrY: int, DestX: int, DestY: int, WorldNum: int, CurrZ: int) -> int: pass
    def GetNotoriety(self, ObjID: int) -> int: pass
    def GetNow(self) -> datetime: pass
    def GetNowUnix(self) -> int: pass
    def GetParent(self, ObjID: int) -> int: pass
    def GetPathArray(self, Xdst: int, Ydst: int, Optimized: bool, Accuracy: int) -> list[WorldPoint]: pass
    def GetPathArray3D(self, StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
    def GetPauseScriptOnDisconnectStatus(self) -> bool: pass
    def GetPickupedItem(self) -> int: pass
    def GetPlayerStatusText(self, ObjID: int) -> str: pass
    def GetPrice(self, ObjID: int) -> int: pass
    def GetQuantity(self, ObjID: int) -> int: pass
    def GetQuestArrow(self) -> Point: pass
    def GetRunMountTimer(self) -> int: pass
    def GetRunUnmountTimer(self) -> int: pass
    def GetScriptCount(self) -> int: pass
    def GetScriptName(self, ScriptIndex: int) -> str: pass
    def GetScriptParams(self) -> int: pass
    def GetScriptPath(self, ScriptIndex: int) -> str: pass
    def GetScriptState(self, ScriptIndex: int) -> int: pass
    def GetScriptsList(self) -> list[ScriptInfo]: pass
    def GetShardPath(self) -> str: pass
    def GetShopList(self) -> list[str]: pass
    def GetShowIPCExceptionWindow(self) -> bool: pass
    def GetSilentMode(self) -> bool: pass
    def GetSkillCap(self, SkillID: int) -> float: pass
    def GetSkillCurrentValue(self, SkillID: int) -> float: pass
    def GetSkillID(self, SkillName: str) -> int: pass
    def GetSkillLockState(self, SkillID: int) -> int: pass
    def GetSkillValue(self, SkillID: int) -> float: pass
    def GetStam(self, ObjID: int) -> int: pass
    def GetStatLockState(self, statNum: int) -> int: pass
    def GetStaticArtBitmap(self, ObjType: int, Hue: int) -> list[int]: pass
    def GetStaticTileData(self, Tile: int) -> StaticTileData: pass
    def GetStaticTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
    def GetStealthInfo(self) -> AboutData: pass
    def GetStealthProfilePath(self) -> str: pass
    def GetStr(self, ObjID: int) -> int: pass
    def GetSurfaceZ(self, X: int, Y: int, WorldNum: int) -> int: pass
    def GetTileFlags(self, Group: int, Tile: int) -> int: pass
    def GetTitle(self, ObjID: int) -> str: pass
    def GetTooltip(self, ObjID: int) -> str: pass
    def GetTooltipRec(self, ObjID: int) -> list[ClilocRec]: pass
    def GetTradeContainer(self, TradeNum: int, Num: int) -> int: pass
    def GetTradeOpponent(self, TradeNum: int) -> int: pass
    def GetTradeOpponentName(self, TradeNum: int) -> str: pass
    def GetType(self, ObjID: int) -> int: pass
    def GetWalkMountTimer(self) -> int: pass
    def GetWalkUnmountTimer(self) -> int: pass
    def GetX(self, ObjID: int) -> int: pass
    def GetY(self, ObjID: int) -> int: pass
    def GetZ(self, ObjID: int) -> int: pass
    def GlobalChatActiveChannel(self) -> str: pass
    def GlobalChatChannelsList(self) -> list[str]: pass
    def GlobalChatJoinChannel(self, ChName: str) -> None: pass
    def GlobalChatLeaveChannel(self) -> None: pass
    def GlobalChatSendMsg(self, MsgText: str) -> None: pass
    def Gold(self) -> int: pass
    def GumpAutoCheckBox(self, CheckBoxID: int, Value: int) -> None: pass
    def GumpAutoRadiobutton(self, RadiobuttonID: int, Value: int) -> None: pass
    def GumpAutoTextEntry(self, TextEntryID: int, Value: str) -> None: pass
    def HTTP_Body(self) -> str: pass
    def HTTP_Get(self, URL: str) -> None: pass
    def HTTP_Header(self) -> str: pass
    def HTTP_Post(self, URL: str, PostData: str) -> str: pass
    def HelpRequest(self) -> None: pass
    def Hidden(self) -> bool: pass
    def HighJournal(self) -> int: pass
    def Ignore(self, ObjID: int) -> None: pass
    def IgnoreOff(self, ObjID: int) -> None: pass
    def IgnoreReset(self) -> None: pass
    def InJournal(self, Str: str) -> int: pass
    def InJournalBetweenTimes(self, Str: str, TimeBegin: datetime, TimeEnd: datetime) -> int: pass
    def InParty(self) -> bool: pass
    def Int(self) -> int: pass
    def InviteToParty(self, ObjID: int) -> None: pass
    def IsActiveSpellAbility(self, SpellID: int) -> bool: pass
    def IsCheckLagEnd(self) -> bool: pass
    def IsContainer(self, ObjID: int) -> bool: pass
    def IsDead(self, ObjID: int) -> bool: pass
    def IsFemale(self, ObjID: int) -> bool: pass
    def IsGumpCanBeClosed(self, GumpIndex: int) -> bool: pass
    def IsHidden(self, ObjID: int) -> bool: pass
    def IsHouse(self, ObjID: int) -> bool: pass
    def IsMovable(self, ObjID: int) -> bool: pass
    def IsNPC(self, ObjID: int) -> bool: pass
    def IsObjectExists(self, ObjID: int) -> bool: pass
    def IsParalyzed(self, ObjID: int) -> bool: pass
    def IsPoisoned(self, ObjID: int) -> bool: pass
    def IsRunning(self, ObjID: int) -> bool: pass
    def IsTrade(self) -> bool: pass
    def IsWarMode(self, ObjID: int) -> bool: pass
    def IsWorldCellPassable(self, CurrX: int, CurrY: int, CurrZ: int, DestX: int, DestY: int, WorldNum: int) -> tuple[bool, int]: pass
    def IsYellowHits(self, ObjID: int) -> bool: pass
    def Journal(self, StringIndex: int) -> str: pass
    def LastAttack(self) -> int: pass
    def LastContainer(self) -> int: pass
    def LastJournalMessage(self) -> str: pass
    def LastObject(self) -> int: pass
    def LastStatus(self) -> int: pass
    def LastTarget(self) -> int: pass
    def Life(self) -> int: pass
    def LineCount(self) -> int: pass
    def LineID(self) -> int: pass
    def LineIndex(self) -> int: pass
    def LineMsgType(self) -> int: pass
    def LineName(self) -> str: pass
    def LineTextColor(self) -> int: pass
    def LineTextFont(self) -> int: pass
    def LineTime(self) -> datetime: pass
    def LineType(self) -> int: pass
    def LowJournal(self) -> int: pass
    def Luck(self) -> int: pass
    def Mana(self) -> int: pass
    def MaxLife(self) -> int: pass
    def MaxMana(self) -> int: pass
    def MaxPets(self) -> int: pass
    def MaxStam(self) -> int: pass
    def MaxWeight(self) -> int: pass
    def MenuHookPresent(self) -> bool: pass
    def MenuPresent(self) -> bool: pass
    def MessengerGetConnected(self, MesID: int) -> bool: pass
    def MessengerGetName(self, MesID: int) -> str: pass
    def MessengerGetToken(self, MesID: int) -> str: pass
    def MessengerSendMessage(self, MesID: int, Msg: str, UserID: str) -> None: pass
    def MessengerSetConnected(self, MesID: int, Value: bool) -> None: pass
    def MessengerSetToken(self, MesID: int, Value: str) -> None: pass
    def MobileCanBeRenamed(self, MobID: int) -> bool: pass
    def MoveXY(self, Xdst: int, Ydst: int, Optimized: bool, Accuracy: int, Running: bool) -> bool: pass
    def MoveXYZ(self, Xdst: int, Ydst: int, Zdst: int, AccuracyXY: int, AccuracyZ: int, Running: bool) -> bool: pass
    def MoverStop(self) -> None: pass
    def NumGumpButton(self, GumpIndex: int, Value: int) -> bool: pass
    def NumGumpCheckBox(self, GumpIndex: int, CBID: int, Value: int) -> bool: pass
    def NumGumpRadiobutton(self, GumpIndex: int, RadiobuttonID: int, Value: int) -> bool: pass
    def NumGumpTextEntry(self, GumpIndex: int, TextEntryID: int, Value: str) -> bool: pass
    def ObjAtLayerEx(self, LayerType: int, PlayerID: int) -> int: pass
    def OpenDoor(self) -> None: pass
    def Paralyzed(self) -> bool: pass
    def PartyAcceptInvite(self) -> None: pass
    def PartyCanLootMe(self, Value: bool) -> None: pass
    def PartyDeclineInvite(self) -> None: pass
    def PartyLeave(self) -> None: pass
    def PartyMembersList(self) -> list[int]: pass
    def PartyPrivateMessageTo(self, ObjID: int, Msg: str) -> None: pass
    def PartySay(self, Msg: str) -> None: pass
    def PauseResumeSelScript(self, ScriptIndex: int) -> None: pass
    def PetsCurrent(self) -> int: pass
    def PoisonResist(self) -> int: pass
    def Poisoned(self) -> bool: pass
    def PredictedDirection(self) -> int: pass
    def PredictedX(self) -> int: pass
    def PredictedY(self) -> int: pass
    def PredictedZ(self) -> int: pass
    def PrintScriptMethodsList(self, FileName: str, SortedList: bool) -> None: pass
    def ProfileName(self) -> str: pass
    def ProfileShardName(self) -> str: pass
    def ProxyIP(self) -> str: pass
    def ProxyPort(self) -> int: pass
    def QuestRequest(self) -> None: pass
    def Race(self) -> int: pass
    def ReadStaticsXY(self, X: int, Y: int, WorldNum: int) -> list[StaticItemRealXY]: pass
    def RemoveFigure(self, FigureID: int) -> bool: pass
    def RemoveFromParty(self, ObjID: int) -> None: pass
    def RemoveUserStatic(self, StaticID: int) -> bool: pass
    def RenameMobile(self, MobID: int, NewName: str) -> None: pass
    def ReqVirtuesGump(self) -> None: pass
    def RequestContextMenu(self, ObjID: int) -> None: pass
    def RequestStats(self, ObjID: int) -> None: pass
    def Salute(self) -> None: pass
    def Self(self) -> int: pass
    def SetARExtParams(self, ShardName: str, CharName: str, UseAtEveryConnect: bool) -> None: pass
    def SetARStatus(self, Value: bool) -> None: pass
    def SetAutoBuyDelay(self, Value: int) -> None: pass
    def SetAutoSellDelay(self, Value: int) -> None: pass
    def SetBadLocation(self, X: int, Y: int) -> None: pass
    def SetBadObject(self, ObjType: int, Color: int, Radius: int) -> None: pass
    def SetCatchBag(self, ObjID: int) -> int: pass
    def SetContextMenuHook(self, MenuID: int, EntryNumber: int) -> None: pass
    def SetDress(self) -> None: pass
    def SetDressSpeed(self, Value: int) -> None: pass
    def SetDropCheckCoord(self, Value: bool) -> None: pass
    def SetDropDelay(self, Value: int) -> None: pass
    def SetEventCallback(self, EventIndex: int) -> None: pass
    def SetFindDistance(self, Value: int) -> None: pass
    def SetFindInNulPoint(self, Value: bool) -> None: pass
    def SetFindVertical(self, Value: int) -> None: pass
    def SetGlobal(self, GlobalRegion: int, VarName: str, VarValue: str) -> None: pass
    def SetGoodLocation(self, X: int, Y: int) -> None: pass
    def SetJournalLine(self, StringIndex: int, Text: str) -> None: pass
    def SetMoveBetweenTwoCorners(self, Value: bool) -> None: pass
    def SetMoveCheckStamina(self, Value: int) -> None: pass
    def SetMoveHeuristicMult(self, Value: int) -> None: pass
    def SetMoveOpenDoor(self, Value: bool) -> None: pass
    def SetMoveThroughCorner(self, Value: bool) -> None: pass
    def SetMoveThroughNPC(self, Value: int) -> None: pass
    def SetMoveTurnCost(self, Value: int) -> None: pass
    def SetPauseScriptOnDisconnectStatus(self, Value: bool) -> None: pass
    def SetPickupedItem(self, ObjID: int) -> None: pass
    def SetRunMountTimer(self, Value: int) -> None: pass
    def SetRunUnmountTimer(self, Value: int) -> None: pass
    def SetScriptName(self, ScriptIndex: int, Value: str) -> None: pass
    def SetShowIPCExceptionWindow(self, Value: bool) -> None: pass
    def SetSilentMode(self, Value: bool) -> None: pass
    def SetSkillLockState(self, SkillID: int, skillState: int) -> None: pass
    def SetStatState(self, statNum: int, statState: int) -> None: pass
    def SetWalkMountTimer(self, Value: int) -> None: pass
    def SetWalkUnmountTimer(self, Value: int) -> None: pass
    def SetWarMode(self, Value: bool) -> None: pass
    def Sex(self) -> int: pass
    def ShardName(self) -> str: pass
    def Stam(self) -> int: pass
    def StartScript(self, ScriptPath: str) -> int: pass
    def StealthPath(self) -> str: pass
    def Step(self, Direction: int, Running: bool) -> int: pass
    def StepQ(self, Direction: int, Running: bool) -> int: pass
    def StopAllScripts(self) -> None: pass
    def StopScript(self, ScriptIndex: int) -> None: pass
    def Str(self) -> int: pass
    def TargetByResource(self, ObjID: int, Resource: int) -> None: pass
    def TargetID(self) -> int: pass
    def TargetToObject(self, ObjID: int) -> None: pass
    def TargetToTile(self, Tile: int, X: int, Y: int, Z: int) -> None: pass
    def TargetToXYZ(self, X: int, Y: int, Z: int) -> None: pass
    def ToggleFly(self) -> None: pass
    def TradeCheck(self, TradeNum: int, Num: int) -> bool: pass
    def TradeCount(self) -> int: pass
    def UOSay(self, Text: str) -> None: pass
    def UOSayColor(self, Text: str, Color: int) -> None: pass
    def UnequipItemsSetMacro(self) -> None: pass
    def UnsetCatchBag(self) -> None: pass
    def UpdateFigure(self, FigureID: int, Figure: MapFigure) -> bool: pass
    def UseFromGround(self, ObjType: int, Color: int) -> int: pass
    def UseItemOnMobile(self, ItemSerial: int, TargetSerial: int) -> None: pass
    def UseObject(self, ObjID: int) -> None: pass
    def UseOtherPaperdollScroll(self, ObjID: int) -> None: pass
    def UsePrimaryAbility(self) -> None: pass
    def UseProxy(self) -> bool: pass
    def UseSecondaryAbility(self) -> None: pass
    def UseSelfPaperdollScroll(self) -> None: pass
    def UseSkill(self, SkillID: int) -> None: pass
    def UseType(self, ObjType: int, Color: int) -> int: pass
    def UseVirtue(self, VirtueID: int) -> None: pass
    def WaitGump(self, Value: int) -> None: pass
    def WaitMenu(self, MenuCaption: str, ElementCaption: str) -> None: pass
    def WaitTargetGround(self, ObjType: int) -> None: pass
    def WaitTargetLast(self) -> None: pass
    def WaitTargetObject(self, ObjID: int) -> None: pass
    def WaitTargetSelf(self) -> None: pass
    def WaitTargetTile(self, Tile: int, X: int, Y: int, Z: int) -> None: pass
    def WaitTargetType(self, ObjType: int) -> None: pass
    def WaitTargetXYZ(self, X: int, Y: int, Z: int) -> None: pass
    def WaitTextEntry(self, Value: str) -> None: pass
    def WarTargetID(self) -> int: pass
    def WearItem(self, Layer: int, ObjID: int) -> bool: pass
    def Weight(self) -> int: pass
    def WorldNum(self) -> int: pass
    def _EventCallback(self, EventId: int, Arguments: tuple) -> None: pass
    def _FunctionResultCallback(self, CallId: int, Result: bytes) -> None: pass
    def _LangVersion(self, Lang: int, Major: int, Minor: int, Revision: int, Build: int) -> None: pass
    def _ScriptPath(self, ScriptName: str) -> None: pass
    def _ScriptPathCallback(self) -> None: pass
    def _ScriptTogglePauseCallback(self) -> None: pass
    def _SelectProfile(self, ProfileName: str) -> None: pass
    def _StopScriptCallback(self) -> None: pass