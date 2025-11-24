###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from datetime import datetime


class AsyncInterface:
    """base class defining the interface of StealthApi."""

    async def AddChatUserIgnore(self, Mobile: str) -> None: pass
    async def AddFigure(self, Figure: MapFigure) -> int: pass
    async def AddGumpIgnoreByID(self, ID: int) -> None: pass
    async def AddGumpIgnoreBySerial(self, Serial: int) -> None: pass
    async def AddJournalIgnore(self, Str: str) -> None: pass
    async def AddToJournal(self, Text: str) -> None: pass
    async def AddToSystemJournal(self, Text: str) -> None: pass
    async def AddToSystemJournalEx(self, Text: str, TextColor: int, BgColor: int, FontSize: int, FontName: str) -> None: pass
    async def AddUserStatic(self, StaticItem: UserStaticItem, WorldNum: int) -> int: pass
    async def Armor(self) -> int: pass
    async def Attack(self, ObjID: int) -> None: pass
    async def AutoBuy(self, ItemType: int, ItemColor: int, Quantity: int) -> None: pass
    async def AutoBuyEx(self, ItemType: int, ItemColor: int, Quantity: int, Price: int, Name: str) -> None: pass
    async def AutoMenu(self, MenuCaption: str, ElementCaption: str) -> None: pass
    async def AutoSell(self, ItemType: int, ItemColor: int, Quantity: int) -> None: pass
    async def Backpack(self) -> int: pass
    async def BandageSelf(self) -> None: pass
    async def BookClearText(self) -> None: pass
    async def BookGetPageText(self, Page: int) -> str: pass
    async def BookSetHeader(self, Title: str, Author: str) -> None: pass
    async def BookSetPageText(self, Page: int, Text: str) -> None: pass
    async def BookSetText(self, Text: str) -> None: pass
    async def Bow(self) -> None: pass
    async def CancelMenu(self) -> None: pass
    async def CancelTarget(self) -> None: pass
    async def CancelTrade(self, TradeNum: int) -> bool: pass
    async def CancelWaitTarget(self) -> None: pass
    async def Cast(self, SpellID: int) -> None: pass
    async def ChangeProfile(self, Name: str) -> int: pass
    async def CharName(self) -> str: pass
    async def CharTitle(self) -> str: pass
    async def CheckLOS(self, Xfrom: int, Yfrom: int, Zfrom: int, Xto: int, Yto: int, Zto: int, WorldNum: int, CheckType: int, Options: int) -> bool: pass
    async def CheckLagBegin(self) -> None: pass
    async def CheckLagEnd(self) -> None: pass
    async def ClearBadLocationList(self) -> None: pass
    async def ClearBadObjectList(self) -> None: pass
    async def ClearChatUserIgnore(self) -> None: pass
    async def ClearContextMenu(self) -> None: pass
    async def ClearEventCallback(self, EventIndex: int) -> None: pass
    async def ClearFigures(self) -> None: pass
    async def ClearGumpsIgnore(self) -> None: pass
    async def ClearInfoWindow(self) -> None: pass
    async def ClearJournal(self) -> None: pass
    async def ClearJournalIgnore(self) -> None: pass
    async def ClearShopList(self) -> None: pass
    async def ClearSystemJournal(self) -> None: pass
    async def ClearUserStatics(self) -> None: pass
    async def ClickOnObject(self, ObjID: int) -> None: pass
    async def ClientHide(self, ObjID: int) -> bool: pass
    async def ClientPrint(self, Text: str) -> None: pass
    async def ClientPrintEx(self, SenderID: int, Color: int, Font: int, Text: str) -> None: pass
    async def ClientRequestObjectTarget(self) -> None: pass
    async def ClientRequestTileTarget(self) -> None: pass
    async def ClientTargetResponse(self) -> TargetInfo: pass
    async def ClientTargetResponsePresent(self) -> bool: pass
    async def CloseClientGump(self, ID: int) -> None: pass
    async def CloseClientUIWindow(self, UIWindowType: int, ID: int) -> None: pass
    async def CloseMenu(self) -> None: pass
    async def CloseSimpleGump(self, GumpIndex: int) -> None: pass
    async def ColdResist(self) -> int: pass
    async def ConfirmTrade(self, TradeNum: int) -> None: pass
    async def Connect(self) -> None: pass
    async def Connected(self) -> bool: pass
    async def ConnectedTime(self) -> datetime: pass
    async def ConsoleEntryReply(self, Text: str) -> None: pass
    async def ConsoleEntryUnicodeReply(self, Text: str) -> None: pass
    async def ConvertIntegerToFlags(self, Group: int, Flags: int) -> list[str]: pass
    async def CreateChar(self, ProfileName: str, ShardName: str, CharName: str, Gender: bool, Race: int, Strn: int, Dex: int, Int: int, Skill1: str, Skill2: str, Skill3: str, Skill4: str, SkillValue1: int, SkillValue2: int, SkillValue3: int, SkillValue4: int, City: int, Slot: int) -> None: pass
    async def Dead(self) -> bool: pass
    async def Disconnect(self) -> None: pass
    async def DisconnectedTime(self) -> datetime: pass
    async def DragItem(self, ObjID: int, Count: int) -> bool: pass
    async def DropItem(self, MoveIntoID: int, X: int, Y: int, Z: int) -> bool: pass
    async def DumpObjectsCache(self) -> None: pass
    async def EnergyResist(self) -> int: pass
    async def EquipItemsSetMacro(self) -> None: pass
    async def EquipLastWeapon(self) -> None: pass
    async def ExtChangeProfile(self, ProfileName: str, ShardName: str, CharName: str) -> int: pass
    async def FillInfoWindow(self, Text: str) -> None: pass
    async def FindAtCoord(self, X: int, Y: int) -> int: pass
    async def FindCount(self) -> int: pass
    async def FindFullQuantity(self) -> int: pass
    async def FindItem(self) -> int: pass
    async def FindNotoriety(self, ObjType: int, Notoriety: int) -> int: pass
    async def FindQuantity(self) -> int: pass
    async def FindTypeEx(self, ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
    async def FindTypesArrayEx(self, ObjTypes: list[int], Colors: list[int], Containers: list[int], InSub: bool) -> int: pass
    async def FireResist(self) -> int: pass
    async def FoundedParamID(self) -> int: pass
    async def GameServerIPString(self) -> str: pass
    async def GetARStatus(self) -> bool: pass
    async def GetActiveAbility(self) -> str: pass
    async def GetAltName(self, ObjID: int) -> str: pass
    async def GetAutoBuyDelay(self) -> int: pass
    async def GetAutoSellDelay(self) -> int: pass
    async def GetBuffBarInfo(self) -> list[BuffBarInfo]: pass
    async def GetCell(self, X: int, Y: int, WorldNum: int) -> MapCell: pass
    async def GetCharsListForShard(self) -> list[str]: pass
    async def GetClientVersionInt(self) -> int: pass
    async def GetClilocByID(self, ClilocID: int) -> str: pass
    async def GetColor(self, ID: int) -> int: pass
    async def GetContextMenu(self) -> list[str]: pass
    async def GetContextMenuRec(self) -> ContextMenuRec: pass
    async def GetDex(self, ObjID: int) -> int: pass
    async def GetDirection(self, ID: int) -> int: pass
    async def GetDistance(self, ObjID: int) -> int: pass
    async def GetDressSet(self) -> list[LayerObject]: pass
    async def GetDressSpeed(self) -> int: pass
    async def GetDropCheckCoord(self) -> bool: pass
    async def GetDropDelay(self) -> int: pass
    async def GetExtInfo(self) -> ExtendedInfo: pass
    async def GetFindDistance(self) -> int: pass
    async def GetFindInNulPoint(self) -> bool: pass
    async def GetFindVertical(self) -> int: pass
    async def GetFindedList(self) -> list[int]: pass
    async def GetGlobal(self, GlobalRegion: int, VarName: str) -> str: pass
    async def GetGumpButtonsDescription(self, GumpIndex: int) -> list[str]: pass
    async def GetGumpFullLines(self, GumpIndex: int) -> list[str]: pass
    async def GetGumpID(self, GumpIndex: int) -> int: pass
    async def GetGumpInfo(self, GumpIndex: int) -> GumpInfo: pass
    async def GetGumpSerial(self, GumpIndex: int) -> int: pass
    async def GetGumpShortLines(self, GumpIndex: int) -> list[str]: pass
    async def GetGumpTextLines(self, GumpIndex: int) -> list[str]: pass
    async def GetGumpsCount(self) -> int: pass
    async def GetHP(self, ObjID: int) -> int: pass
    async def GetIgnoreList(self) -> list[int]: pass
    async def GetInt(self, ObjID: int) -> int: pass
    async def GetLandTileData(self, Tile: int) -> LandTileData: pass
    async def GetLandTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileType: list[int]) -> list[FoundTile]: pass
    async def GetLastMenuItems(self) -> list[str]: pass
    async def GetLastStepQUsedDoor(self) -> int: pass
    async def GetLayer(self, ObjID: int) -> int: pass
    async def GetLayerCount(self, X: int, Y: int, WorldNum: int) -> int: pass
    async def GetLineTime(self) -> datetime: pass
    async def GetMana(self, ObjID: int) -> int: pass
    async def GetMaxHP(self, ObjID: int) -> int: pass
    async def GetMaxMana(self, ObjID: int) -> int: pass
    async def GetMaxStam(self, ObjID: int) -> int: pass
    async def GetMenuItems(self, Caption: str) -> list[str]: pass
    async def GetMenuItemsEx(self, Caption: str) -> list[MenuItem]: pass
    async def GetMoveBetweenTwoCorners(self) -> bool: pass
    async def GetMoveCheckStamina(self) -> int: pass
    async def GetMoveHeuristicMult(self) -> int: pass
    async def GetMoveOpenDoor(self) -> bool: pass
    async def GetMoveThroughCorner(self) -> bool: pass
    async def GetMoveThroughNPC(self) -> int: pass
    async def GetMoveTurnCost(self) -> int: pass
    async def GetMultiAllParts(self, MultiID: int) -> list[MultiPart]: pass
    async def GetMultiPartsAtPosition(self, X: int, Y: int) -> list[MultiPart]: pass
    async def GetMultis(self) -> list[Multi]: pass
    async def GetName(self, ObjID: int) -> str: pass
    async def GetNextStepZ(self, CurrX: int, CurrY: int, DestX: int, DestY: int, WorldNum: int, CurrZ: int) -> int: pass
    async def GetNotoriety(self, ID: int) -> int: pass
    async def GetNow(self) -> datetime: pass
    async def GetNowUnix(self) -> int: pass
    async def GetParent(self, ObjID: int) -> int: pass
    async def GetPathArray(self, Xdst: int, Ydst: int, Optimized: bool, Accuracy: int) -> list[WorldPoint]: pass
    async def GetPathArray3D(self, StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
    async def GetPauseScriptOnDisconnectStatus(self) -> bool: pass
    async def GetPickupedItem(self) -> int: pass
    async def GetPlayerStatusText(self, ObjID: int) -> str: pass
    async def GetPrice(self, ObjID: int) -> int: pass
    async def GetQuantity(self, ObjID: int) -> int: pass
    async def GetQuestArrow(self) -> Point: pass
    async def GetRunMountTimer(self) -> int: pass
    async def GetRunUnmountTimer(self) -> int: pass
    async def GetScriptName(self, ScriptIndex: int) -> str: pass
    async def GetScriptParams(self) -> int: pass
    async def GetScriptPath(self, ScriptIndex: int) -> str: pass
    async def GetScriptState(self, ScriptIndex: int) -> int: pass
    async def GetScriptsCount(self) -> int: pass
    async def GetScriptsList(self) -> list[ScriptInfo]: pass
    async def GetSelfDex(self) -> int: pass
    async def GetSelfInt(self) -> int: pass
    async def GetSelfLife(self) -> int: pass
    async def GetSelfMana(self) -> int: pass
    async def GetSelfMaxLife(self) -> int: pass
    async def GetSelfMaxMana(self) -> int: pass
    async def GetSelfMaxStam(self) -> int: pass
    async def GetSelfStam(self) -> int: pass
    async def GetSelfStr(self) -> int: pass
    async def GetShopList(self) -> list[str]: pass
    async def GetShowIPCExceptionWindow(self) -> bool: pass
    async def GetSilentMode(self) -> bool: pass
    async def GetSkillCap(self, SkillID: int) -> float: pass
    async def GetSkillCurrentValue(self, SkillID: int) -> float: pass
    async def GetSkillID(self, SkillName: str) -> int: pass
    async def GetSkillLockState(self, SkillID: int) -> int: pass
    async def GetSkillValue(self, SkillID: int) -> float: pass
    async def GetStam(self, ObjID: int) -> int: pass
    async def GetStatLockState(self, statNum: int) -> int: pass
    async def GetStaticArt(self, ObjType: int, Hue: int) -> list[int]: pass
    async def GetStaticTileData(self, Tile: int) -> StaticTileData: pass
    async def GetStaticTilesArray(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
    async def GetStealthInfo(self) -> AboutData: pass
    async def GetStr(self, ObjID: int) -> int: pass
    async def GetSurfaceZ(self, X: int, Y: int, WorldNum: int) -> int: pass
    async def GetTileFlags(self, Group: int, Tile: int) -> int: pass
    async def GetTitle(self, ObjID: int) -> str: pass
    async def GetTooltip(self, ObjID: int) -> str: pass
    async def GetTooltipRec(self, ObjID: int) -> list[ClilocRec]: pass
    async def GetTradeContainer(self, TradeNum: int, Num: int) -> int: pass
    async def GetTradeOpponent(self, TradeNum: int) -> int: pass
    async def GetTradeOpponentName(self, TradeNum: int) -> str: pass
    async def GetType(self, ID: int) -> int: pass
    async def GetWalkMountTimer(self) -> int: pass
    async def GetWalkUnmountTimer(self) -> int: pass
    async def GetX(self, ID: int) -> int: pass
    async def GetY(self, ID: int) -> int: pass
    async def GetZ(self, ID: int) -> int: pass
    async def GlobalChatActiveChannel(self) -> str: pass
    async def GlobalChatChannelsList(self) -> list[str]: pass
    async def GlobalChatJoinChannel(self, ChName: str) -> None: pass
    async def GlobalChatLeaveChannel(self) -> None: pass
    async def GlobalChatSendMsg(self, MsgText: str) -> None: pass
    async def Gold(self) -> int: pass
    async def GumpAutoCheckBox(self, CheckBoxID: int, Value: int) -> None: pass
    async def GumpAutoRadiobutton(self, RadiobuttonID: int, Value: int) -> None: pass
    async def GumpAutoTextEntry(self, TextEntryID: int, Value: str) -> None: pass
    async def HTTP_Body(self) -> str: pass
    async def HTTP_Get(self, URL: str) -> None: pass
    async def HTTP_Header(self) -> str: pass
    async def HTTP_Post(self, URL: str, PostData: str) -> str: pass
    async def HelpRequest(self) -> None: pass
    async def Hidden(self) -> bool: pass
    async def HighJournal(self) -> int: pass
    async def Ignore(self, ID: int) -> None: pass
    async def IgnoreOff(self, ID: int) -> None: pass
    async def IgnoreReset(self) -> None: pass
    async def InJournal(self, Str: str) -> int: pass
    async def InJournalBetweenTimes(self, Str: str, TimeBegin: datetime, TimeEnd: datetime) -> int: pass
    async def InParty(self) -> bool: pass
    async def InviteToParty(self, ObjID: int) -> None: pass
    async def IsActiveSpellAbility(self, SpellID: int) -> bool: pass
    async def IsCheckLagEnd(self) -> bool: pass
    async def IsContainer(self, ObjID: int) -> bool: pass
    async def IsDead(self, ObjID: int) -> bool: pass
    async def IsFemale(self, ObjID: int) -> bool: pass
    async def IsGumpCanBeClosed(self, GumpIndex: int) -> bool: pass
    async def IsHidden(self, ObjID: int) -> bool: pass
    async def IsHouse(self, ObjID: int) -> bool: pass
    async def IsMovable(self, ObjID: int) -> bool: pass
    async def IsNPC(self, ObjID: int) -> bool: pass
    async def IsObjectExists(self, ID: int) -> bool: pass
    async def IsParalyzed(self, ObjID: int) -> bool: pass
    async def IsPoisoned(self, ObjID: int) -> bool: pass
    async def IsRunning(self, ObjID: int) -> bool: pass
    async def IsTrade(self) -> bool: pass
    async def IsWarMode(self, ObjID: int) -> bool: pass
    async def IsWorldCellPassable(self, CurrX: int, CurrY: int, CurrZ: int, DestX: int, DestY: int, DestZ: int, WorldNum: int) -> bool: pass
    async def IsYellowHits(self, ObjID: int) -> bool: pass
    async def Journal(self, StringIndex: int) -> str: pass
    async def LastAttack(self) -> int: pass
    async def LastContainer(self) -> int: pass
    async def LastJournalMessage(self) -> str: pass
    async def LastObject(self) -> int: pass
    async def LastStatus(self) -> int: pass
    async def LastTarget(self) -> int: pass
    async def LineCount(self) -> int: pass
    async def LineID(self) -> int: pass
    async def LineIndex(self) -> int: pass
    async def LineMsgType(self) -> int: pass
    async def LineName(self) -> str: pass
    async def LineTextColor(self) -> int: pass
    async def LineTextFont(self) -> int: pass
    async def LineTime(self) -> datetime: pass
    async def LineType(self) -> int: pass
    async def LowJournal(self) -> int: pass
    async def Luck(self) -> int: pass
    async def MaxWeight(self) -> int: pass
    async def MenuHookPresent(self) -> bool: pass
    async def MenuPresent(self) -> bool: pass
    async def Messenger_GetConnected(self, MesID: int) -> bool: pass
    async def Messenger_GetName(self, MesID: int) -> str: pass
    async def Messenger_GetToken(self, MesID: int) -> str: pass
    async def Messenger_SendMessage(self, MesID: int, Msg: str, UserID: str) -> None: pass
    async def Messenger_SetConnected(self, MesID: int, Value: bool) -> None: pass
    async def Messenger_SetToken(self, MesID: int, Value: str) -> None: pass
    async def MobileCanBeRenamed(self, MobID: int) -> bool: pass
    async def MoveXY(self, Xdst: int, Ydst: int, Optimized: bool, Accuracy: int, Running: bool) -> bool: pass
    async def MoveXYZ(self, Xdst: int, Ydst: int, Zdst: int, AccuracyXY: int, AccuracyZ: int, Running: bool) -> bool: pass
    async def MoverStop(self) -> None: pass
    async def NumGumpButton(self, GumpIndex: int, Value: int) -> bool: pass
    async def NumGumpCheckBox(self, GumpIndex: int, CBID: int, Value: int) -> bool: pass
    async def NumGumpRadiobutton(self, GumpIndex: int, RadiobuttonID: int, Value: int) -> bool: pass
    async def NumGumpTextEntry(self, GumpIndex: int, TextEntryID: int, Value: str) -> bool: pass
    async def ObjAtLayerEx(self, LayerType: int, PlayerID: int) -> int: pass
    async def OpenDoor(self) -> None: pass
    async def Paralyzed(self) -> bool: pass
    async def PartyAcceptInvite(self) -> None: pass
    async def PartyCanLootMe(self, Value: bool) -> None: pass
    async def PartyDeclineInvite(self) -> None: pass
    async def PartyLeave(self) -> None: pass
    async def PartyMembersList(self) -> list[int]: pass
    async def PartyPrivateMessageTo(self, ObjID: int, Msg: str) -> None: pass
    async def PartySay(self, Msg: str) -> None: pass
    async def PauseResumeSelScript(self, ScriptIndex: int) -> None: pass
    async def PetsCurrent(self) -> int: pass
    async def PetsMax(self) -> int: pass
    async def PoisonResist(self) -> int: pass
    async def Poisoned(self) -> bool: pass
    async def PredictedDirection(self) -> int: pass
    async def PredictedX(self) -> int: pass
    async def PredictedY(self) -> int: pass
    async def PredictedZ(self) -> int: pass
    async def PrintScriptMethodsList(self, FileName: str, SortedList: bool) -> None: pass
    async def ProfileName(self) -> str: pass
    async def ProfileShardName(self) -> str: pass
    async def ProxyIP(self) -> str: pass
    async def ProxyPort(self) -> int: pass
    async def QuestRequest(self) -> None: pass
    async def Race(self) -> int: pass
    async def ReadStaticsXY(self, X: int, Y: int, WorldNum: int) -> list[StaticItemRealXY]: pass
    async def RemoveFigure(self, FigureID: int) -> bool: pass
    async def RemoveFromParty(self, ObjID: int) -> None: pass
    async def RemoveUserStatic(self, StaticID: int) -> bool: pass
    async def RenameMobile(self, MobID: int, NewName: str) -> None: pass
    async def ReqVirtuesGump(self) -> None: pass
    async def RequestContextMenu(self, ObjID: int) -> None: pass
    async def RequestStats(self, ObjID: int) -> None: pass
    async def Salute(self) -> None: pass
    async def Self(self) -> int: pass
    async def SetARExtParams(self, ShardName: str, CharName: str, UseAtEveryConnect: bool) -> None: pass
    async def SetARStatus(self, Value: bool) -> None: pass
    async def SetAlarm(self) -> None: pass
    async def SetAutoBuyDelay(self, Value: int) -> None: pass
    async def SetAutoSellDelay(self, Value: int) -> None: pass
    async def SetBadLocation(self, X: int, Y: int) -> None: pass
    async def SetBadObject(self, ObjType: int, Color: int, Radius: int) -> None: pass
    async def SetCatchBag(self, ObjID: int) -> int: pass
    async def SetContextMenuHook(self, MenuID: int, EntryNumber: int) -> None: pass
    async def SetDress(self) -> None: pass
    async def SetDressSpeed(self, Value: int) -> None: pass
    async def SetDropCheckCoord(self, Value: bool) -> None: pass
    async def SetDropDelay(self, Value: int) -> None: pass
    async def SetEventCallback(self, EventIndex: int) -> None: pass
    async def SetFindDistance(self, Value: int) -> None: pass
    async def SetFindInNulPoint(self, Value: bool) -> None: pass
    async def SetFindVertical(self, Value: int) -> None: pass
    async def SetGlobal(self, GlobalRegion: int, VarName: str, VarValue: str) -> None: pass
    async def SetGoodLocation(self, X: int, Y: int) -> None: pass
    async def SetJournalLine(self, StringIndex: int, Text: str) -> None: pass
    async def SetMoveBetweenTwoCorners(self, Value: bool) -> None: pass
    async def SetMoveCheckStamina(self, Value: int) -> None: pass
    async def SetMoveHeuristicMult(self, Value: int) -> None: pass
    async def SetMoveOpenDoor(self, Value: bool) -> None: pass
    async def SetMoveThroughCorner(self, Value: bool) -> None: pass
    async def SetMoveThroughNPC(self, Value: int) -> None: pass
    async def SetMoveTurnCost(self, Value: int) -> None: pass
    async def SetPauseScriptOnDisconnectStatus(self, Value: bool) -> None: pass
    async def SetPickupedItem(self, ID: int) -> None: pass
    async def SetRunMountTimer(self, Value: int) -> None: pass
    async def SetRunUnmountTimer(self, Value: int) -> None: pass
    async def SetScriptName(self, ScriptIndex: int, Value: str) -> None: pass
    async def SetShowIPCExceptionWindow(self, Value: bool) -> None: pass
    async def SetSilentMode(self, Value: bool) -> None: pass
    async def SetSkillLockState(self, SkillID: int, skillState: int) -> None: pass
    async def SetStatState(self, statNum: int, statState: int) -> None: pass
    async def SetWalkMountTimer(self, Value: int) -> None: pass
    async def SetWalkUnmountTimer(self, Value: int) -> None: pass
    async def SetWarMode(self, Value: bool) -> None: pass
    async def Sex(self) -> int: pass
    async def ShardName(self) -> str: pass
    async def ShardPath(self) -> str: pass
    async def StartScript(self, ScriptPath: str) -> int: pass
    async def StealthPath(self) -> str: pass
    async def StealthProfilePath(self) -> str: pass
    async def Step(self, Direction: int, Running: bool) -> int: pass
    async def StepQ(self, Direction: int, Running: bool) -> int: pass
    async def StopAllScripts(self) -> None: pass
    async def StopScript(self, ScriptIndex: int) -> None: pass
    async def TargetByResource(self, ObjID: int, Resource: int) -> None: pass
    async def TargetID(self) -> int: pass
    async def TargetToObject(self, ObjID: int) -> None: pass
    async def TargetToTile(self, Tile: int, X: int, Y: int, Z: int) -> None: pass
    async def TargetToXYZ(self, X: int, Y: int, Z: int) -> None: pass
    async def ToggleFly(self) -> None: pass
    async def TradeCheck(self, TradeNum: int, Num: int) -> bool: pass
    async def TradeCount(self) -> int: pass
    async def UOSay(self, Text: str) -> None: pass
    async def UOSayColor(self, Text: str, Color: int) -> None: pass
    async def UnequipItemsSetMacro(self) -> None: pass
    async def UnsetCatchBag(self) -> None: pass
    async def UpdateFigure(self, FigureID: int, Figure: MapFigure) -> bool: pass
    async def UseFromGround(self, ObjType: int, Color: int) -> int: pass
    async def UseItemOnMobile(self, ItemSerial: int, TargetSerial: int) -> None: pass
    async def UseObject(self, ObjID: int) -> None: pass
    async def UseOtherPaperdollScroll(self, ObjID: int) -> None: pass
    async def UsePrimaryAbility(self) -> None: pass
    async def UseProxy(self) -> bool: pass
    async def UseSecondaryAbility(self) -> None: pass
    async def UseSelfPaperdollScroll(self) -> None: pass
    async def UseSkill(self, SkillID: int) -> None: pass
    async def UseType(self, ObjType: int, Color: int) -> int: pass
    async def UseVirtue(self, VirtueID: int) -> None: pass
    async def WaitGump(self, Value: int) -> None: pass
    async def WaitMenu(self, MenuCaption: str, ElementCaption: str) -> None: pass
    async def WaitTargetGround(self, ObjType: int) -> None: pass
    async def WaitTargetLast(self) -> None: pass
    async def WaitTargetObject(self, ObjID: int) -> None: pass
    async def WaitTargetSelf(self) -> None: pass
    async def WaitTargetTile(self, Tile: int, X: int, Y: int, Z: int) -> None: pass
    async def WaitTargetType(self, ObjType: int) -> None: pass
    async def WaitTargetXYZ(self, X: int, Y: int, Z: int) -> None: pass
    async def WaitTextEntry(self, Value: str) -> None: pass
    async def WarTargetID(self) -> int: pass
    async def WearItem(self, Layer: int, ObjID: int) -> bool: pass
    async def Weight(self) -> int: pass
    async def WorldNum(self) -> int: pass
    async def _EventCallback(self, EventId: int, Arguments: tuple) -> None: pass
    async def _FunctionResult(self, CallId: int, Result: bytes) -> None: pass
    async def _LangVersion(self, Lang: int, Major: int, Minor: int, Revision: int, Build: int) -> None: pass
    async def _ScriptPath(self, ScriptName: str) -> None: pass
    async def _ScriptPathRequest(self) -> None: pass
    async def _SelectProfile(self, ProfileName: str) -> None: pass
    async def _StopScriptRequest(self) -> None: pass