###################################################################
# This file was generated automatically. Do not edit it manually! #
###################################################################


from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from datetime import datetime



def AddChatUserIgnore(Mobile: str) -> None: pass
def AddFigure(figure: MapFigure) -> int: pass
def AddGumpIgnoreByID(ID: int) -> None: pass
def AddGumpIgnoreBySerial(Serial: int) -> None: pass
def AddJournalIgnore(Str: str) -> None: pass
def AddToJournal(Text: str) -> None: pass
def AddToSystemJournal(Text: str) -> None: pass
def AddToSystemJournalEx(value: str, textcolor: int, bgcolor: int, fontsize: int, fontname: str) -> None: pass
def AddUserStatic(StaticItem: UserStaticItem, WorldNum: int) -> int: pass
def Armor() -> int: pass
def Attack(ObjID: int) -> None: pass
def AutoBuy(ItemType: int, ItemColor: int, Quantity: int) -> None: pass
def AutoBuyEx(ItemType: int, ItemColor: int, Quantity: int, Price: int, Name: str) -> None: pass
def AutoMenu(MenuCaption: str, ElementCaption: str) -> None: pass
def AutoSell(ItemType: int, ItemColor: int, Quantity: int) -> None: pass
def Backpack() -> int: pass
def BandageSelf() -> None: pass
def BookClearText() -> None: pass
def BookGetPageText(Page: int) -> str: pass
def BookSetHeader(Title: str, Author: str) -> None: pass
def BookSetPageText(Page: int, Text: str) -> None: pass
def BookSetText(Text: str) -> None: pass
def Bow() -> None: pass
def CancelMenu() -> None: pass
def CancelTarget() -> None: pass
def CancelTrade(TradeNum: int) -> bool: pass
def CancelWaitTarget() -> None: pass
def Cast(SpellID: int) -> None: pass
def ChangeProfile(Name: str) -> int: pass
def CharName() -> str: pass
def CharTitle() -> str: pass
def CheckLOS(Xfrom: int, Yfrom: int, Zfrom: int, Xto: int, Yto: int, Zto: int, WorldNum: int) -> bool: pass
def CheckLagBegin() -> None: pass
def CheckLagEnd() -> None: pass
def ClearBadLocationList() -> None: pass
def ClearBadObjectList() -> None: pass
def ClearChatUserIgnore() -> None: pass
def ClearContextMenu() -> None: pass
def ClearEventCallback(EventIndex: int) -> None: pass
def ClearFigures() -> None: pass
def ClearGumpsIgnore() -> None: pass
def ClearInfoWindow() -> None: pass
def ClearJournal() -> None: pass
def ClearJournalIgnore() -> None: pass
def ClearShopList() -> None: pass
def ClearSystemJournal() -> None: pass
def ClearUserStatics() -> None: pass
def ClickOnObject(ObjID: int) -> None: pass
def ClientHide(ObjID: int) -> bool: pass
def ClientPrint(Text: str) -> None: pass
def ClientPrintEx(SenderID: int, Color: int, Font: int, Text: str) -> None: pass
def ClientRequestObjectTarget() -> None: pass
def ClientRequestTileTarget() -> None: pass
def ClientTargetResponse() -> TargetInfo: pass
def ClientTargetResponsePresent() -> bool: pass
def CloseClientGump(ID: int) -> None: pass
def CloseClientUIWindow(UIWindowType: int, ID: int) -> None: pass
def CloseMenu() -> None: pass
def CloseSimpleGump(GumpIndex: int) -> None: pass
def ColdResist() -> int: pass
def ConfirmTrade(TradeNum: int) -> None: pass
def Connect() -> None: pass
def Connected() -> bool: pass
def ConnectedTime() -> datetime: pass
def ConsoleEntryReply(Text: str) -> None: pass
def ConsoleEntryUnicodeReply(Text: str) -> None: pass
def ConvertIntegerToFlags(Group: int, Flags: int) -> list[str]: pass
def CreateChar(ProfileName: str, ShardName: str, CharName: str, Gender: bool, Race: int, Strn: int, Dex: int, Int: int, Skill1: str, Skill2: str, Skill3: str, Skill4: str, SkillValue1: int, SkillValue2: int, SkillValue3: int, SkillValue4: int, City: int, Slot: int) -> None: pass
def Dead() -> bool: pass
def Disconnect() -> None: pass
def DisconnectedTime() -> datetime: pass
def DragItem(ObjID: int, Count: int) -> bool: pass
def DropItem(MoveIntoID: int, X: int, Y: int, Z: int) -> bool: pass
def DumpObjectsCache() -> None: pass
def EnergyResist() -> int: pass
def EquipItemsSetMacro() -> None: pass
def EquipLastWeapon() -> None: pass
def ExtChangeProfile(ProfileName: str, ShardName: str, CharName: str) -> int: pass
def FillInfoWindow(s: str) -> None: pass
def FindAtCoord(X: int, Y: int) -> int: pass
def FindCount() -> int: pass
def FindFullQuantity() -> int: pass
def FindItem() -> int: pass
def FindNotoriety(ObjType: int, Notoriety: int) -> int: pass
def FindQuantity() -> int: pass
def FindTypeEx(ObjType: int, Color: int, Container: int, InSub: bool) -> int: pass
def FindTypesArrayEx(ObjTypes: list[int], Colors: list[int], Containers: list[int], InSub: bool) -> int: pass
def FireResist() -> int: pass
def FoundedParamID() -> int: pass
def GameServerIPString() -> str: pass
def GetARStatus() -> bool: pass
def GetActiveAbility() -> str: pass
def GetAltName(ObjID: int) -> str: pass
def GetAutoBuyDelay() -> int: pass
def GetAutoSellDelay() -> int: pass
def GetBuffBarInfo() -> list[BuffBarInfo]: pass
def GetCell(X: int, Y: int, WorldNum: int) -> MapCell: pass
def GetCharsListForShard() -> list[str]: pass
def GetClientVersionInt() -> int: pass
def GetClilocByID(ClilocID: int) -> str: pass
def GetColor(ID: int) -> int: pass
def GetContextMenu() -> list[str]: pass
def GetContextMenuRec() -> ContextMenuRec: pass
def GetDex(ObjID: int) -> int: pass
def GetDirection(ID: int) -> int: pass
def GetDistance(ObjID: int) -> int: pass
def GetDressSet() -> list[LayerObject]: pass
def GetDressSpeed() -> int: pass
def GetDropCheckCoord() -> bool: pass
def GetDropDelay() -> int: pass
def GetExtInfo() -> ExtendedInfo: pass
def GetFindDistance() -> int: pass
def GetFindInNulPoint() -> bool: pass
def GetFindVertical() -> int: pass
def GetFindedList() -> list[int]: pass
def GetGlobal(GlobalRegion: int, VarName: str) -> str: pass
def GetGumpButtonsDescription(GumpIndex: int) -> list[str]: pass
def GetGumpFullLines(GumpIndex: int) -> list[str]: pass
def GetGumpID(GumpIndex: int) -> int: pass
def GetGumpInfo(GumpIndex: int) -> GumpInfo: pass
def GetGumpSerial(GumpIndex: int) -> int: pass
def GetGumpShortLines(GumpIndex: int) -> list[str]: pass
def GetGumpTextLines(GumpIndex: int) -> list[str]: pass
def GetGumpsCount() -> int: pass
def GetHP(ObjID: int) -> int: pass
def GetIgnoreList() -> list[int]: pass
def GetInt(ObjID: int) -> int: pass
def GetLandTileData(Tile: int) -> LandTileData: pass
def GetLandTilesArray(Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileType: list[int]) -> list[FoundTile]: pass
def GetLastMenuItems() -> list[str]: pass
def GetLastStepQUsedDoor() -> int: pass
def GetLayer(ObjID: int) -> int: pass
def GetLayerCount(x: int, y: int, WorldNum: int) -> int: pass
def GetLineTime() -> datetime: pass
def GetMana(ObjID: int) -> int: pass
def GetMaxHP(ObjID: int) -> int: pass
def GetMaxMana(ObjID: int) -> int: pass
def GetMaxStam(ObjID: int) -> int: pass
def GetMenuItems(Caption: str) -> list[str]: pass
def GetMenuItemsEx(Caption: str) -> list[MenuItem]: pass
def GetMoveBetweenTwoCorners() -> bool: pass
def GetMoveCheckStamina() -> int: pass
def GetMoveHeuristicMult() -> int: pass
def GetMoveOpenDoor() -> bool: pass
def GetMoveThroughCorner() -> bool: pass
def GetMoveThroughNPC() -> int: pass
def GetMoveTurnCost() -> int: pass
def GetMultiAllParts(MultiID: int) -> list[MultiPart]: pass
def GetMultiPartsAtPosition(X: int, Y: int) -> list[MultiPart]: pass
def GetMultis() -> list[Multi]: pass
def GetName(ObjID: int) -> str: pass
def GetNextStepZ(CurrX: int, CurrY: int, DestX: int, DestY: int, WorldNum: int, CurrZ: int) -> int: pass
def GetNotoriety(ID: int) -> int: pass
def GetNow() -> datetime: pass
def GetNowUnix() -> int: pass
def GetParent(ObjID: int) -> int: pass
def GetPathArray(Xdst: int, Ydst: int, Optimized: bool, Accuracy: int) -> list[WorldPoint]: pass
def GetPathArray3D(StartX: int, StartY: int, StartZ: int, FinishX: int, FinishY: int, FinishZ: int, WorldNum: int, AccuracyXY: int, AccuracyZ: int, Run: bool) -> list[WorldPoint]: pass
def GetPauseScriptOnDisconnectStatus() -> bool: pass
def GetPickupedItem() -> int: pass
def GetPlayerStatusText(ObjID: int) -> str: pass
def GetPrice(ObjID: int) -> int: pass
def GetQuantity(ObjID: int) -> int: pass
def GetQuestArrow() -> Point: pass
def GetRunMountTimer() -> int: pass
def GetRunUnmountTimer() -> int: pass
def GetScriptName(ScriptIndex: int) -> str: pass
def GetScriptParams() -> int: pass
def GetScriptPath(ScriptIndex: int) -> str: pass
def GetScriptState(ScriptIndex: int) -> int: pass
def GetScriptsCount() -> int: pass
def GetScriptsList() -> list[ScriptInfo]: pass
def GetSelfDex() -> int: pass
def GetSelfInt() -> int: pass
def GetSelfLife() -> int: pass
def GetSelfMana() -> int: pass
def GetSelfMaxLife() -> int: pass
def GetSelfMaxMana() -> int: pass
def GetSelfMaxStam() -> int: pass
def GetSelfStam() -> int: pass
def GetSelfStr() -> int: pass
def GetShopList() -> list[str]: pass
def GetShowIPCExceptionWindow() -> bool: pass
def GetSilentMode() -> bool: pass
def GetSkillCap(SkillID: int) -> float: pass
def GetSkillCurrentValue(SkillID: int) -> float: pass
def GetSkillID(SkillName: str) -> int: pass
def GetSkillLockState(SkillID: int) -> int: pass
def GetSkillValue(SkillID: int) -> float: pass
def GetStam(ObjID: int) -> int: pass
def GetStatLockState(statNum: int) -> int: pass
def GetStaticArt(ObjType: int, Hue: int) -> list[int]: pass
def GetStaticTileData(Tile: int) -> StaticTileData: pass
def GetStaticTilesArray(Xmin: int, Ymin: int, Xmax: int, Ymax: int, WorldNum: int, TileTypes: list[int]) -> list[FoundTile]: pass
def GetStealthInfo() -> AboutData: pass
def GetStr(ObjID: int) -> int: pass
def GetSurfaceZ(X: int, Y: int, WorldNum: int) -> int: pass
def GetTileFlags(Group: int, Tile: int) -> int: pass
def GetTitle(ObjID: int) -> str: pass
def GetTooltip(ObjID: int) -> str: pass
def GetTooltipRec(ObjID: int) -> list[ClilocRec]: pass
def GetTradeContainer(TradeNum: int, Num: int) -> int: pass
def GetTradeOpponent(TradeNum: int) -> int: pass
def GetTradeOpponentName(TradeNum: int) -> str: pass
def GetType(ID: int) -> int: pass
def GetWalkMountTimer() -> int: pass
def GetWalkUnmountTimer() -> int: pass
def GetX(ID: int) -> int: pass
def GetY(ID: int) -> int: pass
def GetZ(ID: int) -> int: pass
def GlobalChatActiveChannel() -> str: pass
def GlobalChatChannelsList() -> list[str]: pass
def GlobalChatJoinChannel(ChName: str) -> None: pass
def GlobalChatLeaveChannel() -> None: pass
def GlobalChatSendMsg(MsgText: str) -> None: pass
def Gold() -> int: pass
def GumpAutoCheckBox(CheckBoxID: int, Value: int) -> None: pass
def GumpAutoRadiobutton(RadiobuttonID: int, Value: int) -> None: pass
def GumpAutoTextEntry(TextEntryID: int, Value: str) -> None: pass
def HTTP_Body() -> str: pass
def HTTP_Get(URL: str) -> None: pass
def HTTP_Header() -> str: pass
def HTTP_Post(URL: str, PostData: str) -> str: pass
def HelpRequest() -> None: pass
def Hidden() -> bool: pass
def HighJournal() -> int: pass
def Ignore(ID: int) -> None: pass
def IgnoreOff(ID: int) -> None: pass
def IgnoreReset() -> None: pass
def InJournal(Str: str) -> int: pass
def InJournalBetweenTimes(Str: str, TimeBegin: datetime, TimeEnd: datetime) -> int: pass
def InParty() -> bool: pass
def InviteToParty(ObjID: int) -> None: pass
def IsActiveSpellAbility(SpellID: int) -> bool: pass
def IsCheckLagEnd() -> bool: pass
def IsContainer(ObjID: int) -> bool: pass
def IsDead(ObjID: int) -> bool: pass
def IsFemale(ObjID: int) -> bool: pass
def IsGumpCanBeClosed(GumpIndex: int) -> bool: pass
def IsHidden(ObjID: int) -> bool: pass
def IsHouse(ObjID: int) -> bool: pass
def IsMovable(ObjID: int) -> bool: pass
def IsNPC(ObjID: int) -> bool: pass
def IsObjectExists(ID: int) -> bool: pass
def IsParalyzed(ObjID: int) -> bool: pass
def IsPoisoned(ObjID: int) -> bool: pass
def IsRunning(ObjID: int) -> bool: pass
def IsTrade() -> bool: pass
def IsWarMode(ObjID: int) -> bool: pass
def IsWorldCellPassable(CurrX: int, CurrY: int, CurrZ: int, DestX: int, DestY: int, DestZ: int, WorldNum: int) -> bool: pass
def IsYellowHits(ObjID: int) -> bool: pass
def Journal(StringIndex: int) -> str: pass
def LastAttack() -> int: pass
def LastContainer() -> int: pass
def LastJournalMessage() -> str: pass
def LastObject() -> int: pass
def LastStatus() -> int: pass
def LastTarget() -> int: pass
def LineCount() -> int: pass
def LineID() -> int: pass
def LineIndex() -> int: pass
def LineMsgType() -> int: pass
def LineName() -> str: pass
def LineTextColor() -> int: pass
def LineTextFont() -> int: pass
def LineTime() -> datetime: pass
def LineType() -> int: pass
def LowJournal() -> int: pass
def Luck() -> int: pass
def MaxWeight() -> int: pass
def MenuHookPresent() -> bool: pass
def MenuPresent() -> bool: pass
def Messenger_GetConnected(MesID: int) -> bool: pass
def Messenger_GetName(MesID: int) -> str: pass
def Messenger_GetToken(MesID: int) -> str: pass
def Messenger_SendMessage(MesID: int, Msg: str, UserID: str) -> None: pass
def Messenger_SetConnected(MesID: int, Value: bool) -> None: pass
def Messenger_SetToken(MesID: int, Value: str) -> None: pass
def MobileCanBeRenamed(MobID: int) -> bool: pass
def MoveXY(Xdst: int, Ydst: int, Optimized: bool, Accuracy: int, Running: bool) -> bool: pass
def MoveXYZ(Xdst: int, Ydst: int, Zdst: int, AccuracyXY: int, AccuracyZ: int, Running: bool) -> bool: pass
def MoverStop() -> None: pass
def NumGumpButton(GumpIndex: int, Value: int) -> bool: pass
def NumGumpCheckBox(GumpIndex: int, CBID: int, Value: int) -> bool: pass
def NumGumpRadiobutton(GumpIndex: int, RadiobuttonID: int, Value: int) -> bool: pass
def NumGumpTextEntry(GumpIndex: int, TextEntryID: int, Value: str) -> bool: pass
def ObjAtLayerEx(LayerType: int, PlayerID: int) -> int: pass
def OpenDoor() -> None: pass
def Paralyzed() -> bool: pass
def PartyAcceptInvite() -> None: pass
def PartyCanLootMe(Value: bool) -> None: pass
def PartyDeclineInvite() -> None: pass
def PartyLeave() -> None: pass
def PartyMembersList() -> list[int]: pass
def PartyPrivateMessageTo(ObjID: int, Msg: str) -> None: pass
def PartySay(Msg: str) -> None: pass
def PauseResumeSelScript(ScriptIndex: int) -> None: pass
def PetsCurrent() -> int: pass
def PetsMax() -> int: pass
def PoisonResist() -> int: pass
def Poisoned() -> bool: pass
def PredictedDirection() -> int: pass
def PredictedX() -> int: pass
def PredictedY() -> int: pass
def PredictedZ() -> int: pass
def PrintScriptMethodsList(FileName: str, SortedList: bool) -> None: pass
def ProfileName() -> str: pass
def ProfileShardName() -> str: pass
def ProxyIP() -> str: pass
def ProxyPort() -> int: pass
def QuestRequest() -> None: pass
def Race() -> int: pass
def ReadStaticsXY(X: int, Y: int, WorldNum: int) -> list[StaticItemRealXY]: pass
def RemoveFigure(FigureID: int) -> bool: pass
def RemoveFromParty(ObjID: int) -> None: pass
def RemoveUserStatic(StaticID: int) -> bool: pass
def RenameMobile(MobID: int, NewName: str) -> None: pass
def ReqVirtuesGump() -> None: pass
def RequestContextMenu(ObjID: int) -> None: pass
def RequestStats(ObjID: int) -> None: pass
def Salute() -> None: pass
def Self() -> int: pass
def SetARExtParams(ShardName: str, CharName: str, UseAtEveryConnect: bool) -> None: pass
def SetARStatus(Value: bool) -> None: pass
def SetAlarm() -> None: pass
def SetAutoBuyDelay(Value: int) -> None: pass
def SetAutoSellDelay(Value: int) -> None: pass
def SetBadLocation(X: int, Y: int) -> None: pass
def SetBadObject(ObjType: int, Color: int, Radius: int) -> None: pass
def SetCatchBag(ObjID: int) -> int: pass
def SetContextMenuHook(MenuID: int, EntryNumber: int) -> None: pass
def SetDress() -> None: pass
def SetDressSpeed(Value: int) -> None: pass
def SetDropCheckCoord(Value: bool) -> None: pass
def SetDropDelay(Value: int) -> None: pass
def SetEventCallback(EventIndex: int) -> None: pass
def SetFindDistance(Value: int) -> None: pass
def SetFindInNulPoint(Value: bool) -> None: pass
def SetFindVertical(Value: int) -> None: pass
def SetGlobal(GlobalRegion: int, VarName: str, VarValue: str) -> None: pass
def SetGoodLocation(X: int, Y: int) -> None: pass
def SetJournalLine(StringIndex: int, Text: str) -> None: pass
def SetMoveBetweenTwoCorners(Value: bool) -> None: pass
def SetMoveCheckStamina(Value: int) -> None: pass
def SetMoveHeuristicMult(Value: int) -> None: pass
def SetMoveOpenDoor(Value: bool) -> None: pass
def SetMoveThroughCorner(Value: bool) -> None: pass
def SetMoveThroughNPC(Value: int) -> None: pass
def SetMoveTurnCost(Value: int) -> None: pass
def SetPauseScriptOnDisconnectStatus(Value: bool) -> None: pass
def SetPickupedItem(ID: int) -> None: pass
def SetRunMountTimer(Value: int) -> None: pass
def SetRunUnmountTimer(Value: int) -> None: pass
def SetScriptName(ScriptIndex: int, Value: str) -> None: pass
def SetShowIPCExceptionWindow(Value: bool) -> None: pass
def SetSilentMode(Value: bool) -> None: pass
def SetSkillLockState(SkillID: int, skillState: int) -> None: pass
def SetStatState(statNum: int, statState: int) -> None: pass
def SetWalkMountTimer(Value: int) -> None: pass
def SetWalkUnmountTimer(Value: int) -> None: pass
def SetWarMode(Value: bool) -> None: pass
def Sex() -> int: pass
def ShardName() -> str: pass
def ShardPath() -> str: pass
def StartScript(ScriptPath: str) -> int: pass
def StealthPath() -> str: pass
def StealthProfilePath() -> str: pass
def Step(Direction: int, Running: bool) -> int: pass
def StepQ(Direction: int, Running: bool) -> int: pass
def StopAllScripts() -> None: pass
def TargetByResource(ObjID: int, Resource: int) -> None: pass
def TargetID() -> int: pass
def TargetToObject(ObjID: int) -> None: pass
def TargetToTile(Tile: int, X: int, Y: int, Z: int) -> None: pass
def TargetToXYZ(X: int, Y: int, Z: int) -> None: pass
def ToggleFly() -> None: pass
def TradeCheck(TradeNum: int, Num: int) -> bool: pass
def TradeCount() -> int: pass
def UOSay(Text: str) -> None: pass
def UOSayColor(Text: str, Color: int) -> None: pass
def UnequipItemsSetMacro() -> None: pass
def UnsetCatchBag() -> None: pass
def UpdateFigure(FigureID: int, figure: MapFigure) -> bool: pass
def UseFromGround(ObjType: int, Color: int) -> int: pass
def UseItemOnMobile(ItemSerial: int, TargetSerial: int) -> None: pass
def UseObject(ObjID: int) -> None: pass
def UseOtherPaperdollScroll(ObjID: int) -> None: pass
def UsePrimaryAbility() -> None: pass
def UseProxy() -> bool: pass
def UseSecondaryAbility() -> None: pass
def UseSelfPaperdollScroll() -> None: pass
def UseSkill(SkillID: int) -> None: pass
def UseType(ObjType: int, Color: int) -> int: pass
def UseVirtue(VirtueID: int) -> None: pass
def WaitGump(Value: int) -> None: pass
def WaitMenu(MenuCaption: str, ElementCaption: str) -> None: pass
def WaitTargetGround(ObjType: int) -> None: pass
def WaitTargetLast() -> None: pass
def WaitTargetObject(ObjID: int) -> None: pass
def WaitTargetSelf() -> None: pass
def WaitTargetTile(Tile: int, X: int, Y: int, Z: int) -> None: pass
def WaitTargetType(ObjType: int) -> None: pass
def WaitTargetXYZ(X: int, Y: int, Z: int) -> None: pass
def WaitTextEntry(Value: str) -> None: pass
def WarTargetID() -> int: pass
def WearItem(Layer: int, ObjID: int) -> bool: pass
def Weight() -> int: pass
def WorldNum() -> int: pass
def _EventCallback(EventId: int, Arguments: tuple) -> None: pass
def _FunctionResult(CallId: int, Result: bytes) -> None: pass
def _LangVersion(Lang: int, Major: int, Minor: int, Revision: int, Build: int) -> None: pass
def _ScriptPath(ScriptName: str) -> None: pass
def _ScriptPathRequest() -> None: pass
def _SelectProfile(ProfileName: str) -> None: pass
def _StopScript(ScriptIndex: int) -> None: pass