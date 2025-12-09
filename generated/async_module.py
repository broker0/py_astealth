###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from py_astealth.stealth_enums import *
from datetime import datetime


async def AddChatUserIgnore(UserName: str) -> None: pass
async def AddFigure(Figure: MapFigure) -> int: pass
async def AddGumpIgnoreByID(GumpID: int) -> None: pass
async def AddGumpIgnoreBySerial(Serial: int) -> None: pass
async def AddJournalIgnore(Str: str) -> None: pass
async def AddToJournal(Text: str) -> None: pass
async def AddToSystemJournal(Text: str) -> None: pass
async def AddToSystemJournalEx(Text: str, TextColor: int, BgColor: int, FontSize: int, FontName: str) -> None: pass
async def Alarm() -> None: pass
async def Armor() -> int: pass
async def Attack(ObjID: int) -> None: pass
async def AutoBuy(ItemType: int, ItemColor: int, Quantity: int) -> None: pass
async def AutoBuyEx(ItemType: int, ItemColor: int, Quantity: int, Price: int, Name: str) -> None: pass
async def AutoMenu(MenuCaption: str, ElementCaption: str) -> None: pass
async def AutoSell(ItemType: int, ItemColor: int, Quantity: int) -> None: pass
async def Backpack() -> int: pass
async def BandageSelf() -> None: pass
async def BookClearText() -> None: pass
async def BookGetPageText(Page: int) -> str: pass
async def BookSetHeader(Title: str, Author: str) -> None: pass
async def BookSetPageText(Page: int, Text: str) -> None: pass
async def BookSetText(Text: str) -> None: pass
async def Bow() -> None: pass
async def CancelMenu() -> None: pass
async def CancelTarget() -> None: pass
async def CancelTrade(TradeNum: int) -> bool: pass
async def CancelWaitTarget() -> None: pass
async def Cast(SpellID: int) -> None: pass
async def ChangeProfile(Name: str) -> int: pass
async def ChangeProfileEx(ProfileName: str, ShardName: str, CharName: str) -> int: pass
async def CharName() -> str: pass
async def CheckLOS(Xfrom: int, Yfrom: int, Zfrom: int, Xto: int, Yto: int, Zto: int, WorldNum: int, CheckType: int, Options: int) -> bool: pass
async def CheckLagBegin() -> None: pass
async def CheckLagEnd() -> None: pass
async def ClearBadLocationList() -> None: pass
async def ClearBadObjectList() -> None: pass
async def ClearChatUserIgnore() -> None: pass
async def ClearContextMenu() -> None: pass
async def ClearEventCallback(EventIndex: int) -> None: pass
async def ClearFigures() -> None: pass
async def ClearGumpsIgnore() -> None: pass
async def ClearInfoWindow() -> None: pass
async def ClearJournal() -> None: pass
async def ClearJournalIgnore() -> None: pass
async def ClearShopList() -> None: pass
async def ClearSystemJournal() -> None: pass
async def ClearUserStatics() -> None: pass
async def ClickOnObject(ObjID: int) -> None: pass
async def ClientHide(ObjID: int) -> bool: pass
async def ClientPrint(Text: str) -> None: pass
async def ClientPrintEx(SenderID: int, Color: int, Font: int, Text: str) -> None: pass
async def ClientRequestObjectTarget() -> None: pass
async def ClientRequestTileTarget() -> None: pass
async def ClientTargetResponse() -> TargetInfo: pass
async def ClientTargetResponsePresent() -> bool: pass
async def CloseClientGump(ID: int) -> None: pass
async def CloseClientUIWindow(UIWindowType: int, ID: int) -> None: pass
async def CloseMenu() -> None: pass
async def CloseSimpleGump(GumpIndex: int) -> None: pass
async def ColdResist() -> int: pass
async def ConfirmTrade(TradeNum: int) -> None: pass
async def Connect() -> None: pass
async def Connected() -> bool: pass
async def ConnectedTime() -> datetime: pass
async def ConsoleEntryReply(Text: str) -> None: pass
async def ConsoleEntryUnicodeReply(Text: str) -> None: pass
async def ConvertIntegerToFlags(Group: int, Flags: int) -> list[str]: pass
async def CreateChar(ProfileName: str, ShardName: str, CharName: str, Gender: bool, Race: int, Strn: int, Dex: int, Int: int, Skill1: str, Skill2: str, Skill3: str, Skill4: str, SkillValue1: int, SkillValue2: int, SkillValue3: int, SkillValue4: int, City: int, Slot: int) -> None: pass
async def CreateUserStatic(StaticItem: UserStaticItem, WorldNum: int) -> int: pass
async def Dead() -> bool: pass
async def Dex() -> int: pass
async def Disconnect() -> None: pass
async def DisconnectedTime() -> datetime: pass
async def DragItem(ObjID: int, Count: int) -> bool: pass
async def DropItem(MoveIntoID: int, X: int, Y: int, Z: int) -> bool: pass
async def EnergyResist() -> int: pass
async def EquipItemsSetMacro() -> None: pass
async def EquipLastWeapon() -> None: pass
async def FillNewWindow(Text: str) -> None: pass
async def FindAtCoord(X: int, Y: int) -> int: pass
async def FindCount() -> int: pass
async def FindFullQuantity() -> int: pass
async def FindItem() -> int: pass
async def FindNotoriety(ObjType: int, Notoriety: int) -> int: pass
async def FindQuantity() -> int: pass
async def FindTypeEx(ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
async def FindTypesArrayEx(ObjTypes: list[int], Colors: list[int], Containers: list[int], InSub: bool) -> int: pass
async def FireResist() -> int: pass
async def FoundedParamID() -> int: pass
async def GameServerIPString() -> str: pass
async def GetARStatus() -> bool: pass
async def GetActiveAbility() -> str: pass
async def GetAltName(ObjID: int) -> str: pass
async def GetAutoBuyDelay() -> int: pass
async def GetAutoSellDelay() -> int: pass
async def GetBuffBarInfo() -> list[BuffBarInfo]: pass
async def GetCell(X: int, Y: int, WorldNum: int) -> MapCell: pass
async def GetCharTitle() -> str: pass
async def GetCharsListForShard() -> list[str]: pass
async def GetClientVersionInt() -> int: pass
async def GetClilocByID(ClilocID: int, Params: list[str]) -> str: pass
async def GetColor(ObjID: int) -> int: pass
async def GetContextMenu() -> list[str]: pass
async def GetContextMenuRec() -> ContextMenuRec: pass
async def GetDex(ObjID: int) -> int: pass
async def GetDirection(ObjID: int) -> int: pass
async def GetDistance(ObjID: int) -> int: pass
async def GetDressSet() -> list[LayerObject]: pass
async def GetDressSpeed() -> int: pass
async def GetDropCheckCoord() -> bool: pass
async def GetDropDelay() -> int: pass
async def GetExtInfo() -> ExtendedInfo: pass
async def GetFindDistance() -> int: pass
async def GetFindInNulPoint() -> bool: pass
async def GetFindVertical() -> int: pass
async def GetFindedList() -> list[int]: pass
async def GetGlobal(GlobalRegion: int, VarName: str) -> str: pass
async def GetGumpButtonsDescription(GumpIndex: int) -> list[str]: pass
async def GetGumpFullLines(GumpIndex: int) -> list[str]: pass
async def GetGumpID(GumpIndex: int) -> int: pass
async def GetGumpInfo(GumpIndex: int) -> GumpInfo: pass
async def GetGumpSerial(GumpIndex: int) -> int: pass
async def GetGumpShortLines(GumpIndex: int) -> list[str]: pass
async def GetGumpTextLines(GumpIndex: int) -> list[str]: pass
async def GetGumpsCount() -> int: pass
async def GetHP(ObjID: int) -> int: pass
async def GetIgnoreList() -> list[int]: pass
async def GetInt(ObjID: int) -> int: pass
async def GetLandTileData(Tile: int) -> LandTileData: pass
async def GetLandTilesArray(Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
async def GetLastMenuItems() -> list[str]: pass
async def GetLastStepQUsedDoor() -> int: pass
async def GetLayer(ObjID: int) -> int: pass
async def GetLayerCount(X: int, Y: int, WorldNum: int) -> int: pass
async def GetMana(ObjID: int) -> int: pass
async def GetMaxHP(ObjID: int) -> int: pass
async def GetMaxMana(ObjID: int) -> int: pass
async def GetMaxStam(ObjID: int) -> int: pass
async def GetMenuItems(Caption: str) -> list[str]: pass
async def GetMenuItemsEx(Caption: str) -> list[MenuItem]: pass
async def GetMoveBetweenTwoCorners() -> bool: pass
async def GetMoveCheckStamina() -> int: pass
async def GetMoveHeuristicMult() -> int: pass
async def GetMoveOpenDoor() -> bool: pass
async def GetMoveThroughCorner() -> bool: pass
async def GetMoveThroughNPC() -> int: pass
async def GetMoveTurnCost() -> int: pass
async def GetMultiAllParts(MultiID: int) -> list[MultiPart]: pass
async def GetMultiPartsAtPosition(X: int, Y: int) -> list[MultiPart]: pass
async def GetMultis() -> list[Multi]: pass
async def GetName(ObjID: int) -> str: pass
async def GetNextStepZ(CurrX: int, CurrY: int, DestX: int, DestY: int, WorldNum: int, CurrZ: int) -> int: pass
async def GetNotoriety(ObjID: int) -> int: pass
async def GetNow() -> datetime: pass
async def GetNowUnix() -> int: pass
async def GetParent(ObjID: int) -> int: pass
async def GetPathArray(Xdst: int, Ydst: int, Optimized: bool, Accuracy: int) -> list[WorldPoint]: pass
async def GetPathArray3D(StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
async def GetPauseScriptOnDisconnectStatus() -> bool: pass
async def GetPickupedItem() -> int: pass
async def GetPlayerStatusText(ObjID: int) -> str: pass
async def GetPrice(ObjID: int) -> int: pass
async def GetQuantity(ObjID: int) -> int: pass
async def GetQuestArrow() -> Point: pass
async def GetRunMountTimer() -> int: pass
async def GetRunUnmountTimer() -> int: pass
async def GetScriptCount() -> int: pass
async def GetScriptName(ScriptIndex: int) -> str: pass
async def GetScriptParams() -> int: pass
async def GetScriptPath(ScriptIndex: int) -> str: pass
async def GetScriptState(ScriptIndex: int) -> int: pass
async def GetScriptsList() -> list[ScriptInfo]: pass
async def GetShardPath() -> str: pass
async def GetShopList() -> list[str]: pass
async def GetShowIPCExceptionWindow() -> bool: pass
async def GetSilentMode() -> bool: pass
async def GetSkillCap(SkillID: int) -> float: pass
async def GetSkillCurrentValue(SkillID: int) -> float: pass
async def GetSkillID(SkillName: str) -> int: pass
async def GetSkillLockState(SkillID: int) -> int: pass
async def GetSkillValue(SkillID: int) -> float: pass
async def GetStam(ObjID: int) -> int: pass
async def GetStatLockState(statNum: int) -> int: pass
async def GetStaticArtBitmap(ObjType: int, Hue: int) -> list[int]: pass
async def GetStaticTileData(Tile: int) -> StaticTileData: pass
async def GetStaticTilesArray(Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
async def GetStealthInfo() -> AboutData: pass
async def GetStealthProfilePath() -> str: pass
async def GetStr(ObjID: int) -> int: pass
async def GetSurfaceZ(X: int, Y: int, WorldNum: int) -> int: pass
async def GetTileFlags(Group: int, Tile: int) -> int: pass
async def GetTitle(ObjID: int) -> str: pass
async def GetTooltip(ObjID: int) -> str: pass
async def GetTooltipRec(ObjID: int) -> list[ClilocRec]: pass
async def GetTradeContainer(TradeNum: int, Num: int) -> int: pass
async def GetTradeOpponent(TradeNum: int) -> int: pass
async def GetTradeOpponentName(TradeNum: int) -> str: pass
async def GetType(ObjID: int) -> int: pass
async def GetWalkMountTimer() -> int: pass
async def GetWalkUnmountTimer() -> int: pass
async def GetX(ObjID: int) -> int: pass
async def GetY(ObjID: int) -> int: pass
async def GetZ(ObjID: int) -> int: pass
async def GlobalChatActiveChannel() -> str: pass
async def GlobalChatChannelsList() -> list[str]: pass
async def GlobalChatJoinChannel(ChName: str) -> None: pass
async def GlobalChatLeaveChannel() -> None: pass
async def GlobalChatSendMsg(MsgText: str) -> None: pass
async def Gold() -> int: pass
async def GumpAutoCheckBox(CheckBoxID: int, Value: int) -> None: pass
async def GumpAutoRadiobutton(RadiobuttonID: int, Value: int) -> None: pass
async def GumpAutoTextEntry(TextEntryID: int, Value: str) -> None: pass
async def HTTP_Body() -> str: pass
async def HTTP_Get(URL: str) -> None: pass
async def HTTP_Header() -> str: pass
async def HTTP_Post(URL: str, PostData: str) -> str: pass
async def HelpRequest() -> None: pass
async def Hidden() -> bool: pass
async def HighJournal() -> int: pass
async def Ignore(ObjID: int) -> None: pass
async def IgnoreOff(ObjID: int) -> None: pass
async def IgnoreReset() -> None: pass
async def InJournal(Str: str) -> int: pass
async def InJournalBetweenTimes(Str: str, TimeBegin: datetime, TimeEnd: datetime) -> int: pass
async def InParty() -> bool: pass
async def Int() -> int: pass
async def InviteToParty(ObjID: int) -> None: pass
async def IsActiveSpellAbility(SpellID: int) -> bool: pass
async def IsCheckLagEnd() -> bool: pass
async def IsContainer(ObjID: int) -> bool: pass
async def IsDead(ObjID: int) -> bool: pass
async def IsFemale(ObjID: int) -> bool: pass
async def IsGumpCanBeClosed(GumpIndex: int) -> bool: pass
async def IsHidden(ObjID: int) -> bool: pass
async def IsHouse(ObjID: int) -> bool: pass
async def IsMovable(ObjID: int) -> bool: pass
async def IsNPC(ObjID: int) -> bool: pass
async def IsObjectExists(ObjID: int) -> bool: pass
async def IsParalyzed(ObjID: int) -> bool: pass
async def IsPoisoned(ObjID: int) -> bool: pass
async def IsRunning(ObjID: int) -> bool: pass
async def IsTrade() -> bool: pass
async def IsWarMode(ObjID: int) -> bool: pass
async def IsWorldCellPassable(CurrX: int, CurrY: int, CurrZ: int, DestX: int, DestY: int, WorldNum: int) -> tuple[bool, int]: pass
async def IsYellowHits(ObjID: int) -> bool: pass
async def Journal(StringIndex: int) -> str: pass
async def LastAttack() -> int: pass
async def LastContainer() -> int: pass
async def LastJournalMessage() -> str: pass
async def LastObject() -> int: pass
async def LastStatus() -> int: pass
async def LastTarget() -> int: pass
async def Life() -> int: pass
async def LineCount() -> int: pass
async def LineID() -> int: pass
async def LineIndex() -> int: pass
async def LineMsgType() -> int: pass
async def LineName() -> str: pass
async def LineTextColor() -> int: pass
async def LineTextFont() -> int: pass
async def LineTime() -> datetime: pass
async def LineType() -> int: pass
async def LowJournal() -> int: pass
async def Luck() -> int: pass
async def Mana() -> int: pass
async def MaxLife() -> int: pass
async def MaxMana() -> int: pass
async def MaxPets() -> int: pass
async def MaxStam() -> int: pass
async def MaxWeight() -> int: pass
async def MenuHookPresent() -> bool: pass
async def MenuPresent() -> bool: pass
async def MessengerGetConnected(MesID: int) -> bool: pass
async def MessengerGetName(MesID: int) -> str: pass
async def MessengerGetToken(MesID: int) -> str: pass
async def MessengerSendMessage(MesID: int, Msg: str, UserID: str) -> None: pass
async def MessengerSetConnected(MesID: int, Value: bool) -> None: pass
async def MessengerSetToken(MesID: int, Value: str) -> None: pass
async def MobileCanBeRenamed(MobID: int) -> bool: pass
async def MoveXY(Xdst: int, Ydst: int, Optimized: bool, Accuracy: int, Running: bool) -> bool: pass
async def MoveXYZ(Xdst: int, Ydst: int, Zdst: int, AccuracyXY: int, AccuracyZ: int, Running: bool) -> bool: pass
async def MoverStop() -> None: pass
async def NumGumpButton(GumpIndex: int, Value: int) -> bool: pass
async def NumGumpCheckBox(GumpIndex: int, CBID: int, Value: int) -> bool: pass
async def NumGumpRadiobutton(GumpIndex: int, RadiobuttonID: int, Value: int) -> bool: pass
async def NumGumpTextEntry(GumpIndex: int, TextEntryID: int, Value: str) -> bool: pass
async def ObjAtLayerEx(LayerType: int, PlayerID: int) -> int: pass
async def OpenDoor() -> None: pass
async def Paralyzed() -> bool: pass
async def PartyAcceptInvite() -> None: pass
async def PartyCanLootMe(Value: bool) -> None: pass
async def PartyDeclineInvite() -> None: pass
async def PartyLeave() -> None: pass
async def PartyMembersList() -> list[int]: pass
async def PartyPrivateMessageTo(ObjID: int, Msg: str) -> None: pass
async def PartySay(Msg: str) -> None: pass
async def PauseResumeSelScript(ScriptIndex: int) -> None: pass
async def PetsCurrent() -> int: pass
async def PoisonResist() -> int: pass
async def Poisoned() -> bool: pass
async def PredictedDirection() -> int: pass
async def PredictedX() -> int: pass
async def PredictedY() -> int: pass
async def PredictedZ() -> int: pass
async def PrintScriptMethodsList(FileName: str, SortedList: bool) -> None: pass
async def ProfileName() -> str: pass
async def ProfileShardName() -> str: pass
async def ProxyIP() -> str: pass
async def ProxyPort() -> int: pass
async def QuestRequest() -> None: pass
async def Race() -> int: pass
async def ReadStaticsXY(X: int, Y: int, WorldNum: int) -> list[StaticItemRealXY]: pass
async def RemoveFigure(FigureID: int) -> bool: pass
async def RemoveFromParty(ObjID: int) -> None: pass
async def RemoveUserStatic(StaticID: int) -> bool: pass
async def RenameMobile(MobID: int, NewName: str) -> None: pass
async def ReqVirtuesGump() -> None: pass
async def RequestContextMenu(ObjID: int) -> None: pass
async def RequestStats(ObjID: int) -> None: pass
async def Salute() -> None: pass
async def Self() -> int: pass
async def SetARExtParams(ShardName: str, CharName: str, UseAtEveryConnect: bool) -> None: pass
async def SetARStatus(Value: bool) -> None: pass
async def SetAutoBuyDelay(Value: int) -> None: pass
async def SetAutoSellDelay(Value: int) -> None: pass
async def SetBadLocation(X: int, Y: int) -> None: pass
async def SetBadObject(ObjType: int, Color: int, Radius: int) -> None: pass
async def SetCatchBag(ObjID: int) -> int: pass
async def SetContextMenuHook(MenuID: int, EntryNumber: int) -> None: pass
async def SetDress() -> None: pass
async def SetDressSpeed(Value: int) -> None: pass
async def SetDropCheckCoord(Value: bool) -> None: pass
async def SetDropDelay(Value: int) -> None: pass
async def SetEventCallback(EventIndex: int) -> None: pass
async def SetFindDistance(Value: int) -> None: pass
async def SetFindInNulPoint(Value: bool) -> None: pass
async def SetFindVertical(Value: int) -> None: pass
async def SetGlobal(GlobalRegion: int, VarName: str, VarValue: str) -> None: pass
async def SetGoodLocation(X: int, Y: int) -> None: pass
async def SetJournalLine(StringIndex: int, Text: str) -> None: pass
async def SetMoveBetweenTwoCorners(Value: bool) -> None: pass
async def SetMoveCheckStamina(Value: int) -> None: pass
async def SetMoveHeuristicMult(Value: int) -> None: pass
async def SetMoveOpenDoor(Value: bool) -> None: pass
async def SetMoveThroughCorner(Value: bool) -> None: pass
async def SetMoveThroughNPC(Value: int) -> None: pass
async def SetMoveTurnCost(Value: int) -> None: pass
async def SetPauseScriptOnDisconnectStatus(Value: bool) -> None: pass
async def SetPickupedItem(ObjID: int) -> None: pass
async def SetRunMountTimer(Value: int) -> None: pass
async def SetRunUnmountTimer(Value: int) -> None: pass
async def SetScriptName(ScriptIndex: int, Value: str) -> None: pass
async def SetShowIPCExceptionWindow(Value: bool) -> None: pass
async def SetSilentMode(Value: bool) -> None: pass
async def SetSkillLockState(SkillID: int, skillState: int) -> None: pass
async def SetStatState(statNum: int, statState: int) -> None: pass
async def SetWalkMountTimer(Value: int) -> None: pass
async def SetWalkUnmountTimer(Value: int) -> None: pass
async def SetWarMode(Value: bool) -> None: pass
async def Sex() -> int: pass
async def ShardName() -> str: pass
async def Stam() -> int: pass
async def StartScript(ScriptPath: str) -> int: pass
async def StealthPath() -> str: pass
async def Step(Direction: int, Running: bool) -> int: pass
async def StepQ(Direction: int, Running: bool) -> int: pass
async def StopAllScripts() -> None: pass
async def StopScript(ScriptIndex: int) -> None: pass
async def Str() -> int: pass
async def TargetByResource(ObjID: int, Resource: int) -> None: pass
async def TargetID() -> int: pass
async def TargetToObject(ObjID: int) -> None: pass
async def TargetToTile(Tile: int, X: int, Y: int, Z: int) -> None: pass
async def TargetToXYZ(X: int, Y: int, Z: int) -> None: pass
async def ToggleFly() -> None: pass
async def TradeCheck(TradeNum: int, Num: int) -> bool: pass
async def TradeCount() -> int: pass
async def UOSay(Text: str) -> None: pass
async def UOSayColor(Text: str, Color: int) -> None: pass
async def UnequipItemsSetMacro() -> None: pass
async def UnsetCatchBag() -> None: pass
async def UpdateFigure(FigureID: int, Figure: MapFigure) -> bool: pass
async def UseFromGround(ObjType: int, Color: int) -> int: pass
async def UseItemOnMobile(ItemSerial: int, TargetSerial: int) -> None: pass
async def UseObject(ObjID: int) -> None: pass
async def UseOtherPaperdollScroll(ObjID: int) -> None: pass
async def UsePrimaryAbility() -> None: pass
async def UseProxy() -> bool: pass
async def UseSecondaryAbility() -> None: pass
async def UseSelfPaperdollScroll() -> None: pass
async def UseSkill(SkillID: int) -> None: pass
async def UseType(ObjType: int, Color: int) -> int: pass
async def UseVirtue(VirtueID: int) -> None: pass
async def WaitGump(Value: int) -> None: pass
async def WaitMenu(MenuCaption: str, ElementCaption: str) -> None: pass
async def WaitTargetGround(ObjType: int) -> None: pass
async def WaitTargetLast() -> None: pass
async def WaitTargetObject(ObjID: int) -> None: pass
async def WaitTargetSelf() -> None: pass
async def WaitTargetTile(Tile: int, X: int, Y: int, Z: int) -> None: pass
async def WaitTargetType(ObjType: int) -> None: pass
async def WaitTargetXYZ(X: int, Y: int, Z: int) -> None: pass
async def WaitTextEntry(Value: str) -> None: pass
async def WarTargetID() -> int: pass
async def WearItem(Layer: int, ObjID: int) -> bool: pass
async def Weight() -> int: pass
async def WorldNum() -> int: pass
async def _ErrorReportCallback(Error: str) -> None: pass
async def _EventCallback(EventId: int, Arguments: tuple) -> None: pass
async def _FunctionResultCallback(CallId: int, Result: bytes) -> None: pass
async def _LangVersion(Lang: int, Major: int, Minor: int, Revision: int, Build: int) -> None: pass
async def _RequestPort(GroupId: int, ProfileName: str) -> tuple[int, int]: pass
async def _ScriptPath(ScriptName: str) -> None: pass
async def _ScriptPathCallback() -> None: pass
async def _ScriptTogglePauseCallback() -> None: pass
async def _SelectProfile(ProfileName: str) -> None: pass
async def _StopScriptCallback() -> None: pass


__all__ = [
    "AddChatUserIgnore",
    "AddFigure",
    "AddGumpIgnoreByID",
    "AddGumpIgnoreBySerial",
    "AddJournalIgnore",
    "AddToJournal",
    "AddToSystemJournal",
    "AddToSystemJournalEx",
    "Alarm",
    "Armor",
    "Attack",
    "AutoBuy",
    "AutoBuyEx",
    "AutoMenu",
    "AutoSell",
    "Backpack",
    "BandageSelf",
    "BookClearText",
    "BookGetPageText",
    "BookSetHeader",
    "BookSetPageText",
    "BookSetText",
    "Bow",
    "CancelMenu",
    "CancelTarget",
    "CancelTrade",
    "CancelWaitTarget",
    "Cast",
    "ChangeProfile",
    "ChangeProfileEx",
    "CharName",
    "CheckLOS",
    "CheckLagBegin",
    "CheckLagEnd",
    "ClearBadLocationList",
    "ClearBadObjectList",
    "ClearChatUserIgnore",
    "ClearContextMenu",
    "ClearEventCallback",
    "ClearFigures",
    "ClearGumpsIgnore",
    "ClearInfoWindow",
    "ClearJournal",
    "ClearJournalIgnore",
    "ClearShopList",
    "ClearSystemJournal",
    "ClearUserStatics",
    "ClickOnObject",
    "ClientHide",
    "ClientPrint",
    "ClientPrintEx",
    "ClientRequestObjectTarget",
    "ClientRequestTileTarget",
    "ClientTargetResponse",
    "ClientTargetResponsePresent",
    "CloseClientGump",
    "CloseClientUIWindow",
    "CloseMenu",
    "CloseSimpleGump",
    "ColdResist",
    "ConfirmTrade",
    "Connect",
    "Connected",
    "ConnectedTime",
    "ConsoleEntryReply",
    "ConsoleEntryUnicodeReply",
    "ConvertIntegerToFlags",
    "CreateChar",
    "CreateUserStatic",
    "Dead",
    "Dex",
    "Disconnect",
    "DisconnectedTime",
    "DragItem",
    "DropItem",
    "EnergyResist",
    "EquipItemsSetMacro",
    "EquipLastWeapon",
    "FillNewWindow",
    "FindAtCoord",
    "FindCount",
    "FindFullQuantity",
    "FindItem",
    "FindNotoriety",
    "FindQuantity",
    "FindTypeEx",
    "FindTypesArrayEx",
    "FireResist",
    "FoundedParamID",
    "GameServerIPString",
    "GetARStatus",
    "GetActiveAbility",
    "GetAltName",
    "GetAutoBuyDelay",
    "GetAutoSellDelay",
    "GetBuffBarInfo",
    "GetCell",
    "GetCharTitle",
    "GetCharsListForShard",
    "GetClientVersionInt",
    "GetClilocByID",
    "GetColor",
    "GetContextMenu",
    "GetContextMenuRec",
    "GetDex",
    "GetDirection",
    "GetDistance",
    "GetDressSet",
    "GetDressSpeed",
    "GetDropCheckCoord",
    "GetDropDelay",
    "GetExtInfo",
    "GetFindDistance",
    "GetFindInNulPoint",
    "GetFindVertical",
    "GetFindedList",
    "GetGlobal",
    "GetGumpButtonsDescription",
    "GetGumpFullLines",
    "GetGumpID",
    "GetGumpInfo",
    "GetGumpSerial",
    "GetGumpShortLines",
    "GetGumpTextLines",
    "GetGumpsCount",
    "GetHP",
    "GetIgnoreList",
    "GetInt",
    "GetLandTileData",
    "GetLandTilesArray",
    "GetLastMenuItems",
    "GetLastStepQUsedDoor",
    "GetLayer",
    "GetLayerCount",
    "GetMana",
    "GetMaxHP",
    "GetMaxMana",
    "GetMaxStam",
    "GetMenuItems",
    "GetMenuItemsEx",
    "GetMoveBetweenTwoCorners",
    "GetMoveCheckStamina",
    "GetMoveHeuristicMult",
    "GetMoveOpenDoor",
    "GetMoveThroughCorner",
    "GetMoveThroughNPC",
    "GetMoveTurnCost",
    "GetMultiAllParts",
    "GetMultiPartsAtPosition",
    "GetMultis",
    "GetName",
    "GetNextStepZ",
    "GetNotoriety",
    "GetNow",
    "GetNowUnix",
    "GetParent",
    "GetPathArray",
    "GetPathArray3D",
    "GetPauseScriptOnDisconnectStatus",
    "GetPickupedItem",
    "GetPlayerStatusText",
    "GetPrice",
    "GetQuantity",
    "GetQuestArrow",
    "GetRunMountTimer",
    "GetRunUnmountTimer",
    "GetScriptCount",
    "GetScriptName",
    "GetScriptParams",
    "GetScriptPath",
    "GetScriptState",
    "GetScriptsList",
    "GetShardPath",
    "GetShopList",
    "GetShowIPCExceptionWindow",
    "GetSilentMode",
    "GetSkillCap",
    "GetSkillCurrentValue",
    "GetSkillID",
    "GetSkillLockState",
    "GetSkillValue",
    "GetStam",
    "GetStatLockState",
    "GetStaticArtBitmap",
    "GetStaticTileData",
    "GetStaticTilesArray",
    "GetStealthInfo",
    "GetStealthProfilePath",
    "GetStr",
    "GetSurfaceZ",
    "GetTileFlags",
    "GetTitle",
    "GetTooltip",
    "GetTooltipRec",
    "GetTradeContainer",
    "GetTradeOpponent",
    "GetTradeOpponentName",
    "GetType",
    "GetWalkMountTimer",
    "GetWalkUnmountTimer",
    "GetX",
    "GetY",
    "GetZ",
    "GlobalChatActiveChannel",
    "GlobalChatChannelsList",
    "GlobalChatJoinChannel",
    "GlobalChatLeaveChannel",
    "GlobalChatSendMsg",
    "Gold",
    "GumpAutoCheckBox",
    "GumpAutoRadiobutton",
    "GumpAutoTextEntry",
    "HTTP_Body",
    "HTTP_Get",
    "HTTP_Header",
    "HTTP_Post",
    "HelpRequest",
    "Hidden",
    "HighJournal",
    "Ignore",
    "IgnoreOff",
    "IgnoreReset",
    "InJournal",
    "InJournalBetweenTimes",
    "InParty",
    "Int",
    "InviteToParty",
    "IsActiveSpellAbility",
    "IsCheckLagEnd",
    "IsContainer",
    "IsDead",
    "IsFemale",
    "IsGumpCanBeClosed",
    "IsHidden",
    "IsHouse",
    "IsMovable",
    "IsNPC",
    "IsObjectExists",
    "IsParalyzed",
    "IsPoisoned",
    "IsRunning",
    "IsTrade",
    "IsWarMode",
    "IsWorldCellPassable",
    "IsYellowHits",
    "Journal",
    "LastAttack",
    "LastContainer",
    "LastJournalMessage",
    "LastObject",
    "LastStatus",
    "LastTarget",
    "Life",
    "LineCount",
    "LineID",
    "LineIndex",
    "LineMsgType",
    "LineName",
    "LineTextColor",
    "LineTextFont",
    "LineTime",
    "LineType",
    "LowJournal",
    "Luck",
    "Mana",
    "MaxLife",
    "MaxMana",
    "MaxPets",
    "MaxStam",
    "MaxWeight",
    "MenuHookPresent",
    "MenuPresent",
    "MessengerGetConnected",
    "MessengerGetName",
    "MessengerGetToken",
    "MessengerSendMessage",
    "MessengerSetConnected",
    "MessengerSetToken",
    "MobileCanBeRenamed",
    "MoveXY",
    "MoveXYZ",
    "MoverStop",
    "NumGumpButton",
    "NumGumpCheckBox",
    "NumGumpRadiobutton",
    "NumGumpTextEntry",
    "ObjAtLayerEx",
    "OpenDoor",
    "Paralyzed",
    "PartyAcceptInvite",
    "PartyCanLootMe",
    "PartyDeclineInvite",
    "PartyLeave",
    "PartyMembersList",
    "PartyPrivateMessageTo",
    "PartySay",
    "PauseResumeSelScript",
    "PetsCurrent",
    "PoisonResist",
    "Poisoned",
    "PredictedDirection",
    "PredictedX",
    "PredictedY",
    "PredictedZ",
    "PrintScriptMethodsList",
    "ProfileName",
    "ProfileShardName",
    "ProxyIP",
    "ProxyPort",
    "QuestRequest",
    "Race",
    "ReadStaticsXY",
    "RemoveFigure",
    "RemoveFromParty",
    "RemoveUserStatic",
    "RenameMobile",
    "ReqVirtuesGump",
    "RequestContextMenu",
    "RequestStats",
    "Salute",
    "Self",
    "SetARExtParams",
    "SetARStatus",
    "SetAutoBuyDelay",
    "SetAutoSellDelay",
    "SetBadLocation",
    "SetBadObject",
    "SetCatchBag",
    "SetContextMenuHook",
    "SetDress",
    "SetDressSpeed",
    "SetDropCheckCoord",
    "SetDropDelay",
    "SetEventCallback",
    "SetFindDistance",
    "SetFindInNulPoint",
    "SetFindVertical",
    "SetGlobal",
    "SetGoodLocation",
    "SetJournalLine",
    "SetMoveBetweenTwoCorners",
    "SetMoveCheckStamina",
    "SetMoveHeuristicMult",
    "SetMoveOpenDoor",
    "SetMoveThroughCorner",
    "SetMoveThroughNPC",
    "SetMoveTurnCost",
    "SetPauseScriptOnDisconnectStatus",
    "SetPickupedItem",
    "SetRunMountTimer",
    "SetRunUnmountTimer",
    "SetScriptName",
    "SetShowIPCExceptionWindow",
    "SetSilentMode",
    "SetSkillLockState",
    "SetStatState",
    "SetWalkMountTimer",
    "SetWalkUnmountTimer",
    "SetWarMode",
    "Sex",
    "ShardName",
    "Stam",
    "StartScript",
    "StealthPath",
    "Step",
    "StepQ",
    "StopAllScripts",
    "StopScript",
    "Str",
    "TargetByResource",
    "TargetID",
    "TargetToObject",
    "TargetToTile",
    "TargetToXYZ",
    "ToggleFly",
    "TradeCheck",
    "TradeCount",
    "UOSay",
    "UOSayColor",
    "UnequipItemsSetMacro",
    "UnsetCatchBag",
    "UpdateFigure",
    "UseFromGround",
    "UseItemOnMobile",
    "UseObject",
    "UseOtherPaperdollScroll",
    "UsePrimaryAbility",
    "UseProxy",
    "UseSecondaryAbility",
    "UseSelfPaperdollScroll",
    "UseSkill",
    "UseType",
    "UseVirtue",
    "WaitGump",
    "WaitMenu",
    "WaitTargetGround",
    "WaitTargetLast",
    "WaitTargetObject",
    "WaitTargetSelf",
    "WaitTargetTile",
    "WaitTargetType",
    "WaitTargetXYZ",
    "WaitTextEntry",
    "WarTargetID",
    "WearItem",
    "Weight",
    "WorldNum",
    "_ErrorReportCallback",
    "_EventCallback",
    "_FunctionResultCallback",
    "_LangVersion",
    "_RequestPort",
    "_ScriptPath",
    "_ScriptPathCallback",
    "_ScriptTogglePauseCallback",
    "_SelectProfile",
    "_StopScriptCallback",
]
