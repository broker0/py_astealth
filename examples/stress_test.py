import asyncio
from datetime import datetime, timedelta
import inspect

from py_astealth.api_client import AsyncStealthApiClient, SyncStealthApiClient
from py_astealth.stealth_types import *
from py_astealth.stealth_structs import *
from py_astealth.stealth_enums import *


async def call_method(method):
    # await asyncio.sleep(1/10000)

    result = method()
    if inspect.isawaitable(result):
        return await result

    return result


async def method_generator(stealth):
    methods = {
        "Self": lambda: stealth.Self(),
        "Backpack": lambda: stealth.Backpack(),
        "WorldNum": lambda: stealth.WorldNum(),
        "PredictedX": lambda: stealth.PredictedX(),
        "PredictedY": lambda: stealth.PredictedY(),
        "PredictedZ": lambda: stealth.PredictedZ()
    }

    # --- Context Initialization ---
    SelfID = await call_method(methods["Self"])
    BackpackID = await call_method(methods["Backpack"])
    WorldNum = await call_method(methods["WorldNum"])
    CurrX = await call_method(methods["PredictedX"])
    CurrY = await call_method(methods["PredictedY"])
    CurrZ = await call_method(methods["PredictedZ"])

    # -- Variables for arguments --
    ID = SelfID
    ObjID = SelfID
    Serial = SelfID
    ItemSerial = BackpackID
    TargetSerial = SelfID
    MobID = SelfID
    Container = BackpackID
    ContainerID = BackpackID
    MultiID = 0
    Parent = BackpackID

    X = CurrX
    Y = CurrY
    Z = CurrZ
    Xdst = CurrX
    Ydst = CurrY
    Zdst = CurrZ
    Xfrom = CurrX
    Yfrom = CurrY
    Zfrom = CurrZ
    Xto = CurrX + 5
    Yto = CurrY + 5
    Zto = CurrZ
    StartX = CurrX
    StartY = CurrY
    StartZ = CurrZ
    FinishX = CurrX
    FinishY = CurrY
    FinishZ = CurrZ
    Xmin = CurrX
    Ymin = CurrY
    Xmax = CurrX
    Ymax = CurrY
    DestX = CurrX
    DestY = CurrY
    DestZ = CurrZ
    
    Text = "Test Text"
    Str = "Test String"
    Name = "Test Name"
    ProfileName = "Test Profile"
    ShardName = "Test Shard"
    CharName = "Test Char"
    ScriptName = "Test Script"
    ScriptPath = "Test Path"
    MenuCaption = "Menu"
    ElementCaption = "Element"
    NewName = "New Name"
    Mobile = "Mobile Name"
    
    Color = 0
    ObjType = 0
    Type = 0
    Tile = 0
    GumpIndex = 0
    GumpID = 0
    MenuID = 0
    SkillID = 1
    SpellID = 17
    Layer = 1
    Hue = 0
    Count = 1
    Quantity = 1
    Price = 100
    Weight = 10
    Amount = 1
    Radius = 10
    Direction = 0
    Running = False
    Optimized = True
    InSub = False
    UseAtEveryConnect = False
    Accuracy = 0
    AccuracyXY = 0
    AccuracyZ = 0
    WaitMs = 100
    Lang = 0
    Major = 0
    Minor = 0
    Revision = 0
    Build = 0
    EventId = 0
    EventIndex = 0
    CallId = 0
    Result = b''
    StringIndex = 0
    LineIndex = 0
    Group = 0
    Notoriety = 1
    RadiobuttonID = 0
    CheckBoxID = 0
    TextEntryID = 0
    CBID = 0
    EntryNumber = 0
    skillState = 0
    
    # Typed Values
    ValueInt = 0
    ValueStr = "Value"
    ValueBool = False
    
    # Aliases
    ScriptIndex = 0
    Run = Running
    Caption = "Caption"
    Page = 0
    Title = "Title"
    Author = "Author"
    TradeNum = 0
    SenderID = 0
    Font = 0
    UIWindowType = 0
    Flags = 0
    Gender = 0
    Race = 0
    Strn = 0
    Dex = 0
    Int = 0
    Skill1 = 0
    Skill2 = 0
    Skill3 = 0
    Skill4 = 0
    SkillValue1 = 0
    SkillValue2 = 0
    SkillValue3 = 0
    SkillValue4 = 0
    City = 0
    Slot = 0
    MoveIntoID = BackpackID
    ClilocID = 0
    GlobalRegion = 0
    VarName = "Var"
    VarValue = "Val"
    SkillName = "Anatomy"
    statNum = 0
    statState = 0
    ChName = "Channel"
    MsgText = "Message"
    URL = "http://google.com"
    PostData = ""
    MesID = 0
    Msg = "Message"
    UserID = "UserID"
    LayerType = 0
    PlayerID = SelfID
    FileName = "File.txt"
    SortedList = False
    FigureID = 0
    StaticID = 0
    Resource = 0
    VirtueID = 0
    ItemType = 0
    ItemColor = 0
    TextColor = 0
    BgColor = 0
    FontSize = 0
    FontName = "Font"
    Num = 0
    
    ObjTypes = [0]
    Colors = [0]
    Containers = [BackpackID]
    TileTypes = [0]
    TileType = [0]
    
    TimeBegin = datetime.now()
    TimeEnd = datetime.now()
    Figure = MapFigure(0, 0, 0, 0, 100, 100, 0x00FF0000, 0, 0x00FF0000, 0, "Hello")
    UserStatic = UserStaticItem(1, 2, 3, 4, 5)
    
    # --- Generated Calls ---
    methods["GetPathArray3D"] = lambda: stealth.GetPathArray3D(StartX, StartY, StartZ, FinishX, FinishY, FinishZ, WorldNum, AccuracyXY, AccuracyZ, Run)
    methods["ExtChangeProfile"] = lambda: stealth.ChangeProfileEx(ProfileName, ShardName, CharName)

    methods["AddChatUserIgnore"] = lambda: stealth.AddChatUserIgnore(Mobile)
    # methods["AddFigure"] = lambda: client.AddFigure(Figure)
    # methods["UpdateFigure"] = lambda: client.UpdateFigure(FigureID, Figure)
    # methods["RemoveFigure"] = lambda: client.RemoveFigure(FigureID)
    # methods["ClearFigures"] = lambda: client.ClearFigures()
    methods["AddGumpIgnoreByID"] = lambda: stealth.AddGumpIgnoreByID(ID)
    methods["AddGumpIgnoreBySerial"] = lambda: stealth.AddGumpIgnoreBySerial(Serial)
    methods["AddJournalIgnore"] = lambda: stealth.AddJournalIgnore(Str)
    methods["AddToJournal"] = lambda: stealth.AddToJournal(Text)
    methods["AddToSystemJournal"] = lambda: stealth.AddToSystemJournal(Text)
    methods["AddToSystemJournalEx"] = lambda: stealth.AddToSystemJournalEx(Text, TextColor, BgColor, FontSize, FontName)
    methods["CreateUserStatic"] = lambda: stealth.CreateUserStatic(UserStatic, WorldNum)
    methods["RemoveUserStatic"] = lambda: stealth.RemoveUserStatic(StaticID)
    methods["ClearUserStatics"] = lambda: stealth.ClearUserStatics()
    methods["Armor"] = lambda: stealth.Armor()
    # methods["Attack"] = lambda: client.Attack(ObjID)
    # methods["AutoBuy"] = lambda: client.AutoBuy(ItemType, ItemColor, Quantity)
    # methods["AutoBuyEx"] = lambda: client.AutoBuyEx(ItemType, ItemColor, Quantity, Price, Name)
    # methods["AutoMenu"] = lambda: client.AutoMenu(MenuCaption, ElementCaption)
    # methods["AutoSell"] = lambda: client.AutoSell(ItemType, ItemColor, Quantity)
    # methods["BandageSelf"] = lambda: client.BandageSelf()
    # methods["BookClearText"] = lambda: client.BookClearText()
    # methods["BookGetPageText"] = lambda: client.BookGetPageText(Page)
    # methods["BookSetHeader"] = lambda: client.BookSetHeader(Title, Author)
    # methods["BookSetPageText"] = lambda: client.BookSetPageText(Page, Text)
    # methods["BookSetText"] = lambda: client.BookSetText(Text)
    # methods["Bow"] = lambda: client.Bow()
    methods["CancelMenu"] = lambda: stealth.CancelMenu()
    methods["CancelTarget"] = lambda: stealth.CancelTarget()
    # methods["CancelTrade"] = lambda: client.CancelTrade(TradeNum)
    methods["CancelWaitTarget"] = lambda: stealth.CancelWaitTarget()
    # methods["Cast"] = lambda: client.Cast(SpellID)
    # methods["ChangeProfile"] = lambda: stealth.ChangeProfile(Name)
    methods["CharName"] = lambda: stealth.CharName()
    methods["CharTitle"] = lambda: stealth.GetCharTitle()
    methods["CheckLOS"] = lambda: stealth.CheckLOS(Xfrom, Yfrom, Zfrom, Xto, Yto, Zto, WorldNum, LOSCheckType.RunUO, LOSCheckOption.NoOptions)
    methods["CheckLagBegin"] = lambda: stealth.CheckLagBegin()
    methods["CheckLagEnd"] = lambda: stealth.CheckLagEnd()
    methods["ClearBadLocationList"] = lambda: stealth.ClearBadLocationList()
    methods["ClearBadObjectList"] = lambda: stealth.ClearBadObjectList()
    methods["ClearChatUserIgnore"] = lambda: stealth.ClearChatUserIgnore()
    methods["ClearContextMenu"] = lambda: stealth.ClearContextMenu()
    methods["ClearEventCallback"] = lambda: stealth.ClearEventCallback(EventIndex)
    methods["ClearGumpsIgnore"] = lambda: stealth.ClearGumpsIgnore()
    methods["ClearInfoWindow"] = lambda: stealth.ClearInfoWindow()
    methods["ClearJournal"] = lambda: stealth.ClearJournal()
    methods["ClearJournalIgnore"] = lambda: stealth.ClearJournalIgnore()
    methods["ClearShopList"] = lambda: stealth.ClearShopList()
    methods["ClearSystemJournal"] = lambda: stealth.ClearSystemJournal()
    # methods["ClickOnObject"] = lambda: client.ClickOnObject(ObjID)
    methods["ClientHide"] = lambda: stealth.ClientHide(0)
    methods["ClientPrint"] = lambda: stealth.ClientPrint(Text)
    methods["ClientPrintEx"] = lambda: stealth.ClientPrintEx(SenderID, Color, Font, Text)
    # methods["ClientRequestObjectTarget"] = lambda: client.ClientRequestObjectTarget()
    # methods["ClientRequestTileTarget"] = lambda: client.ClientRequestTileTarget()
    # methods["ClientTargetResponse"] = lambda: stealth.ClientTargetResponse()
    methods["ClientTargetResponsePresent"] = lambda: stealth.ClientTargetResponsePresent()
    # methods["CloseClientGump"] = lambda: client.CloseClientGump(ID)
    # methods["CloseClientUIWindow"] = lambda: client.CloseClientUIWindow(UIWindowType, ID)
    methods["CloseMenu"] = lambda: stealth.CloseMenu()
    methods["CloseSimpleGump"] = lambda: stealth.CloseSimpleGump(GumpIndex)
    methods["ColdResist"] = lambda: stealth.ColdResist()
    # methods["ConfirmTrade"] = lambda: client.ConfirmTrade(TradeNum)
    # methods["Connect"] = lambda: client.Connect()
    methods["Connected"] = lambda: stealth.Connected()
    methods["ConnectedTime"] = lambda: stealth.ConnectedTime()
    # methods["ConsoleEntryReply"] = lambda: client.ConsoleEntryReply(Text)
    # methods["ConsoleEntryUnicodeReply"] = lambda: client.ConsoleEntryUnicodeReply(Text)
    methods["ConvertIntegerToFlags"] = lambda: stealth.ConvertIntegerToFlags(Group, Flags)
    # methods["CreateChar"] = lambda: client.CreateChar(ProfileName, ShardName, CharName, Gender, Race, Strn, Dex, Int, Skill1, Skill2, Skill3, Skill4, SkillValue1, SkillValue2, SkillValue3, SkillValue4, City, Slot)
    methods["Dead"] = lambda: stealth.Dead()
    # methods["Disconnect"] = lambda: client.Disconnect()
    methods["DisconnectedTime"] = lambda: stealth.DisconnectedTime()
    # methods["DragItem"] = lambda: stealth.DragItem(ObjID, Count)
    # methods["DropItem"] = lambda: client.DropItem(MoveIntoID, X, Y, Z)
    # methods["DumpObjectsCache"] = lambda: stealth.DumpObjectsCache()
    methods["EnergyResist"] = lambda: stealth.EnergyResist()
    # methods["EquipItemsSetMacro"] = lambda: client.EquipItemsSetMacro()
    # methods["EquipLastWeapon"] = lambda: client.EquipLastWeapon()
    methods["FillInfoWindow"] = lambda: stealth.FillNewWindow(Text)
    methods["FindAtCoord"] = lambda: stealth.FindAtCoord(X, Y)
    methods["FindCount"] = lambda: stealth.FindCount()
    methods["FindFullQuantity"] = lambda: stealth.FindFullQuantity()
    methods["FindItem"] = lambda: stealth.FindItem()
    methods["FindNotoriety"] = lambda: stealth.FindNotoriety(ObjType, Notoriety)
    methods["FindQuantity"] = lambda: stealth.FindQuantity()
    methods["FindTypeEx"] = lambda: stealth.FindTypeEx(ObjType, Color, Container, InSub)
    methods["FindTypesArrayEx"] = lambda: stealth.FindTypesArrayEx(ObjTypes, Colors, Containers, InSub)
    methods["FireResist"] = lambda: stealth.FireResist()
    methods["FoundedParamID"] = lambda: stealth.FoundedParamID()
    methods["GameServerIPString"] = lambda: stealth.GameServerIPString()
    methods["GetARStatus"] = lambda: stealth.GetARStatus()
    methods["GetActiveAbility"] = lambda: stealth.GetActiveAbility()
    methods["GetAltName"] = lambda: stealth.GetAltName(ObjID)
    methods["GetAutoBuyDelay"] = lambda: stealth.GetAutoBuyDelay()
    methods["GetAutoSellDelay"] = lambda: stealth.GetAutoSellDelay()
    methods["GetBuffBarInfo"] = lambda: stealth.GetBuffBarInfo()
    methods["GetCell"] = lambda: stealth.GetCell(X, Y, WorldNum)
    methods["GetCharsListForShard"] = lambda: stealth.GetCharsListForShard()
    methods["GetClientVersionInt"] = lambda: stealth.GetClientVersionInt()
    methods["GetClilocByID"] = lambda: stealth.GetClilocByID(ClilocID, [])
    methods["GetColor"] = lambda: stealth.GetColor(ID)
    methods["GetContextMenu"] = lambda: stealth.GetContextMenu()
    methods["GetContextMenuRec"] = lambda: stealth.GetContextMenuRec()
    methods["GetDex"] = lambda: stealth.GetDex(ObjID)
    methods["GetDirection"] = lambda: stealth.GetDirection(ID)
    methods["GetDistance"] = lambda: stealth.GetDistance(ObjID)
    methods["GetDressSet"] = lambda: stealth.GetDressSet()
    methods["GetDressSpeed"] = lambda: stealth.GetDressSpeed()
    methods["GetDropCheckCoord"] = lambda: stealth.GetDropCheckCoord()
    methods["GetDropDelay"] = lambda: stealth.GetDropDelay()
    methods["GetExtInfo"] = lambda: stealth.GetExtInfo()
    methods["GetFindDistance"] = lambda: stealth.GetFindDistance()
    methods["GetFindInNulPoint"] = lambda: stealth.GetFindInNulPoint()
    methods["GetFindVertical"] = lambda: stealth.GetFindVertical()
    methods["GetFindedList"] = lambda: stealth.GetFindedList()
    methods["GetGlobal"] = lambda: stealth.GetGlobal(GlobalRegion, VarName)
    methods["GetGumpButtonsDescription"] = lambda: stealth.GetGumpButtonsDescription(GumpIndex)
    methods["GetGumpFullLines"] = lambda: stealth.GetGumpFullLines(GumpIndex)
    methods["GetGumpID"] = lambda: stealth.GetGumpID(GumpIndex)
    methods["GetGumpInfo"] = lambda: stealth.GetGumpInfo(GumpIndex)
    methods["GetGumpSerial"] = lambda: stealth.GetGumpSerial(GumpIndex)
    methods["GetGumpShortLines"] = lambda: stealth.GetGumpShortLines(GumpIndex)
    methods["GetGumpTextLines"] = lambda: stealth.GetGumpTextLines(GumpIndex)
    methods["GetGumpsCount"] = lambda: stealth.GetGumpsCount()
    methods["GetHP"] = lambda: stealth.GetHP(ObjID)
    methods["GetIgnoreList"] = lambda: stealth.GetIgnoreList()
    methods["GetInt"] = lambda: stealth.GetInt(ObjID)
    methods["GetLandTileData"] = lambda: stealth.GetLandTileData(Tile)
    methods["GetLandTilesArray"] = lambda: stealth.GetLandTilesArray(Xmin, Ymin, Xmax, Ymax, WorldNum, TileType)
    methods["GetLastMenuItems"] = lambda: stealth.GetLastMenuItems()
    methods["GetLastStepQUsedDoor"] = lambda: stealth.GetLastStepQUsedDoor()
    methods["GetLayer"] = lambda: stealth.GetLayer(ObjID)
    methods["GetLayerCount"] = lambda: stealth.GetLayerCount(X, Y, WorldNum)
    methods["LineTime"] = lambda: stealth.LineTime()
    methods["GetMana"] = lambda: stealth.GetMana(ObjID)
    methods["GetMaxHP"] = lambda: stealth.GetMaxHP(ObjID)
    methods["GetMaxMana"] = lambda: stealth.GetMaxMana(ObjID)
    methods["GetMaxStam"] = lambda: stealth.GetMaxStam(ObjID)
    methods["GetMenuItems"] = lambda: stealth.GetMenuItems(Caption)
    methods["GetMenuItemsEx"] = lambda: stealth.GetMenuItemsEx(Caption)
    methods["GetMoveBetweenTwoCorners"] = lambda: stealth.GetMoveBetweenTwoCorners()
    methods["GetMoveCheckStamina"] = lambda: stealth.GetMoveCheckStamina()
    methods["GetMoveHeuristicMult"] = lambda: stealth.GetMoveHeuristicMult()
    methods["GetMoveOpenDoor"] = lambda: stealth.GetMoveOpenDoor()
    methods["GetMoveThroughCorner"] = lambda: stealth.GetMoveThroughCorner()
    methods["GetMoveThroughNPC"] = lambda: stealth.GetMoveThroughNPC()
    methods["GetMoveTurnCost"] = lambda: stealth.GetMoveTurnCost()
    methods["GetMultiAllParts"] = lambda: stealth.GetMultiAllParts(MultiID)
    methods["GetMultiPartsAtPosition"] = lambda: stealth.GetMultiPartsAtPosition(X, Y)
    methods["GetMultis"] = lambda: stealth.GetMultis()
    methods["GetName"] = lambda: stealth.GetName(ObjID)
    methods["GetNextStepZ"] = lambda: stealth.GetNextStepZ(CurrX, CurrY, DestX, DestY, WorldNum, CurrZ)
    methods["GetNotoriety"] = lambda: stealth.GetNotoriety(ID)
    methods["GetNow"] = lambda: stealth.GetNow()
    methods["GetNowUnix"] = lambda: stealth.GetNowUnix()
    methods["GetParent"] = lambda: stealth.GetParent(ObjID)
    methods["GetPathArray"] = lambda: stealth.GetPathArray(Xdst, Ydst, Optimized, Accuracy)
    methods["GetPauseScriptOnDisconnectStatus"] = lambda: stealth.GetPauseScriptOnDisconnectStatus()
    methods["GetPickupedItem"] = lambda: stealth.GetPickupedItem()
    methods["GetPlayerStatusText"] = lambda: stealth.GetPlayerStatusText(ObjID)
    methods["GetPrice"] = lambda: stealth.GetPrice(ObjID)
    methods["GetQuantity"] = lambda: stealth.GetQuantity(ObjID)
    methods["GetQuestArrow"] = lambda: stealth.GetQuestArrow()
    methods["GetRunMountTimer"] = lambda: stealth.GetRunMountTimer()
    methods["GetRunUnmountTimer"] = lambda: stealth.GetRunUnmountTimer()
    methods["GetScriptName"] = lambda: stealth.GetScriptName(ScriptIndex)
    methods["GetScriptParams"] = lambda: stealth.GetScriptParams()
    methods["GetScriptPath"] = lambda: stealth.GetScriptPath(ScriptIndex)
    methods["GetScriptState"] = lambda: stealth.GetScriptState(ScriptIndex)
    methods["GetScriptsCount"] = lambda: stealth.GetScriptCount()
    methods["GetScriptsList"] = lambda: stealth.GetScriptsList()
    methods["Str"] = lambda: stealth.Str()
    methods["Dex"] = lambda: stealth.Dex()
    methods["Int"] = lambda: stealth.Int()
    methods["Life"] = lambda: stealth.Life()
    methods["Stam"] = lambda: stealth.Stam()
    methods["Mana"] = lambda: stealth.Mana()
    methods["MaxLife"] = lambda: stealth.MaxLife()
    methods["MaxStam"] = lambda: stealth.MaxStam()
    methods["MaxMana"] = lambda: stealth.MaxMana()
    methods["GetShopList"] = lambda: stealth.GetShopList()
    methods["GetShowIPCExceptionWindow"] = lambda: stealth.GetShowIPCExceptionWindow()
    methods["GetSilentMode"] = lambda: stealth.GetSilentMode()
    methods["GetSkillID"] = lambda: stealth.GetSkillID(SkillName)
    methods["GetSkillCap"] = lambda: stealth.GetSkillCap(SkillID)
    methods["GetSkillCurrentValue"] = lambda: stealth.GetSkillCurrentValue(SkillID)
    methods["GetSkillLockState"] = lambda: stealth.GetSkillLockState(SkillID)
    methods["GetSkillValue"] = lambda: stealth.GetSkillValue(SkillID)
    methods["GetStam"] = lambda: stealth.GetStam(ObjID)
    methods["GetStatLockState"] = lambda: stealth.GetStatLockState(statNum)
    methods["GetStaticArt"] = lambda: stealth.GetStaticArtBitmap(ObjType, Hue)
    methods["GetStaticTileData"] = lambda: stealth.GetStaticTileData(Tile)
    methods["GetStaticTilesArray"] = lambda: stealth.GetStaticTilesArray(Xmin, Ymin, Xmax, Ymax, WorldNum, TileTypes)
    methods["GetStealthInfo"] = lambda: stealth.GetStealthInfo()
    methods["GetStr"] = lambda: stealth.GetStr(ObjID)
    methods["GetSurfaceZ"] = lambda: stealth.GetSurfaceZ(X, Y, WorldNum)
    methods["GetTileFlags"] = lambda: stealth.GetTileFlags(Group, Tile)
    methods["GetTitle"] = lambda: stealth.GetTitle(ObjID)
    # methods["GetTooltip"] = lambda: client.GetTooltip(ObjID)
    # methods["GetTooltipRec"] = lambda: client.GetTooltipRec(ObjID)
    methods["GetTradeContainer"] = lambda: stealth.GetTradeContainer(TradeNum, Num)
    # methods["GetTradeOpponent"] = lambda: client.GetTradeOpponent(TradeNum)
    # methods["GetTradeOpponentName"] = lambda: client.GetTradeOpponentName(TradeNum)
    methods["GetType"] = lambda: stealth.GetType(ID)
    methods["GetWalkMountTimer"] = lambda: stealth.GetWalkMountTimer()
    methods["GetWalkUnmountTimer"] = lambda: stealth.GetWalkUnmountTimer()
    methods["GetX"] = lambda: stealth.GetX(ID)
    methods["GetY"] = lambda: stealth.GetY(ID)
    methods["GetZ"] = lambda: stealth.GetZ(ID)
    # methods["GlobalChatActiveChannel"] = lambda: client.GlobalChatActiveChannel()
    # methods["GlobalChatChannelsList"] = lambda: client.GlobalChatChannelsList()
    # methods["GlobalChatJoinChannel"] = lambda: client.GlobalChatJoinChannel(ChName)
    # methods["GlobalChatLeaveChannel"] = lambda: client.GlobalChatLeaveChannel()
    # methods["GlobalChatSendMsg"] = lambda: client.GlobalChatSendMsg(MsgText)
    methods["Gold"] = lambda: stealth.Gold()
    # methods["GumpAutoCheckBox"] = lambda: client.GumpAutoCheckBox(CheckBoxID, ValueInt)
    # methods["GumpAutoRadiobutton"] = lambda: client.GumpAutoRadiobutton(RadiobuttonID, ValueInt)
    # methods["GumpAutoTextEntry"] = lambda: client.GumpAutoTextEntry(TextEntryID, ValueStr)
    methods["HTTP_Body"] = lambda: stealth.HTTP_Body()
    # methods["HTTP_Get"] = lambda: client.HTTP_Get(URL)
    methods["HTTP_Header"] = lambda: stealth.HTTP_Header()
    # methods["HTTP_Post"] = lambda: client.HTTP_Post(URL, PostData)
    # methods["HelpRequest"] = lambda: client.HelpRequest()
    methods["Hidden"] = lambda: stealth.Hidden()
    methods["HighJournal"] = lambda: stealth.HighJournal()
    methods["Ignore"] = lambda: stealth.Ignore(ID)
    methods["IgnoreOff"] = lambda: stealth.IgnoreOff(ID)
    methods["IgnoreReset"] = lambda: stealth.IgnoreReset()
    methods["InJournal"] = lambda: stealth.InJournal(Str)
    methods["InJournalBetweenTimes"] = lambda: stealth.InJournalBetweenTimes(Str, TimeBegin, TimeEnd)
    methods["InParty"] = lambda: stealth.InParty()
    methods["IsActiveSpellAbility"] = lambda: stealth.IsActiveSpellAbility(SpellID)
    methods["IsCheckLagEnd"] = lambda: stealth.IsCheckLagEnd()
    methods["IsContainer"] = lambda: stealth.IsContainer(ObjID)
    methods["IsDead"] = lambda: stealth.IsDead(ObjID)
    methods["IsFemale"] = lambda: stealth.IsFemale(ObjID)
    methods["IsGumpCanBeClosed"] = lambda: stealth.IsGumpCanBeClosed(GumpIndex)
    methods["IsHidden"] = lambda: stealth.IsHidden(ObjID)
    methods["IsHouse"] = lambda: stealth.IsHouse(ObjID)
    methods["IsMovable"] = lambda: stealth.IsMovable(ObjID)
    methods["IsNPC"] = lambda: stealth.IsNPC(ObjID)
    methods["IsObjectExists"] = lambda: stealth.IsObjectExists(ID)
    methods["IsParalyzed"] = lambda: stealth.IsParalyzed(ObjID)
    methods["IsPoisoned"] = lambda: stealth.IsPoisoned(ObjID)
    methods["IsRunning"] = lambda: stealth.IsRunning(ObjID)
    methods["IsTrade"] = lambda: stealth.IsTrade()
    methods["IsWarMode"] = lambda: stealth.IsWarMode(ObjID)
    methods["IsWorldCellPassable"] = lambda: stealth.IsWorldCellPassable(CurrX, CurrY, CurrZ, DestX, DestY, WorldNum)
    methods["IsYellowHits"] = lambda: stealth.IsYellowHits(ObjID)
    methods["Journal"] = lambda: stealth.Journal(StringIndex)
    methods["LastAttack"] = lambda: stealth.LastAttack()
    methods["LastContainer"] = lambda: stealth.LastContainer()
    methods["LastJournalMessage"] = lambda: stealth.LastJournalMessage()
    methods["LastObject"] = lambda: stealth.LastObject()
    methods["LastStatus"] = lambda: stealth.LastStatus()
    methods["LastTarget"] = lambda: stealth.LastTarget()
    methods["LineCount"] = lambda: stealth.LineCount()
    methods["LineID"] = lambda: stealth.LineID()
    methods["LineIndex"] = lambda: stealth.LineIndex()
    methods["LineMsgType"] = lambda: stealth.LineMsgType()
    methods["LineName"] = lambda: stealth.LineName()
    methods["LineTextColor"] = lambda: stealth.LineTextColor()
    methods["LineTextFont"] = lambda: stealth.LineTextFont()
    methods["LineTime"] = lambda: stealth.LineTime()
    methods["LineType"] = lambda: stealth.LineType()
    methods["LowJournal"] = lambda: stealth.LowJournal()
    methods["Luck"] = lambda: stealth.Luck()
    methods["MaxWeight"] = lambda: stealth.MaxWeight()
    methods["MenuHookPresent"] = lambda: stealth.MenuHookPresent()
    methods["MenuPresent"] = lambda: stealth.MenuPresent()
    methods["MessengerGetConnected"] = lambda: stealth.MessengerGetConnected(MesID)
    methods["MessengerGetName"] = lambda: stealth.MessengerGetName(MesID)
    methods["MessengerGetToken"] = lambda: stealth.MessengerGetToken(MesID)
    # methods["MessengerSendMessage"] = lambda: client.Messenger_SendMessage(MesID, Msg, UserID)
    # methods["MessengerSetConnected"] = lambda: client.Messenger_SetConnected(MesID, ValueBool)
    # methods["MessengerSetToken"] = lambda: client.Messenger_SetToken(MesID, ValueStr)
    methods["MobileCanBeRenamed"] = lambda: stealth.MobileCanBeRenamed(MobID)
    # methods["MoveXY"] = lambda: client.MoveXY(Xdst, Ydst, Optimized, Accuracy, Running)
    # methods["MoveXYZ"] = lambda: client.MoveXYZ(Xdst, Ydst, Zdst, AccuracyXY, AccuracyZ, Running)
    methods["MoverStop"] = lambda: stealth.MoverStop()
    # methods["NumGumpButton"] = lambda: client.NumGumpButton(GumpIndex, ValueInt)
    # methods["NumGumpCheckBox"] = lambda: client.NumGumpCheckBox(GumpIndex, CBID, ValueInt)
    # methods["NumGumpRadiobutton"] = lambda: client.NumGumpRadiobutton(GumpIndex, RadiobuttonID, ValueInt)
    # methods["NumGumpTextEntry"] = lambda: client.NumGumpTextEntry(GumpIndex, TextEntryID, ValueStr)
    methods["ObjAtLayerEx"] = lambda: stealth.ObjAtLayerEx(LayerType, PlayerID)
    # methods["OpenDoor"] = lambda: client.OpenDoor()
    methods["Paralyzed"] = lambda: stealth.Paralyzed()
    # methods["InviteToParty"] = lambda: client.InviteToParty(ObjID)
    # methods["PartyAcceptInvite"] = lambda: client.PartyAcceptInvite()
    # methods["PartyCanLootMe"] = lambda: client.PartyCanLootMe(ValueBool)
    # methods["PartyDeclineInvite"] = lambda: client.PartyDeclineInvite()
    # methods["PartyLeave"] = lambda: client.PartyLeave()
    methods["PartyMembersList"] = lambda: stealth.PartyMembersList()
    # methods["PartyPrivateMessageTo"] = lambda: client.PartyPrivateMessageTo(ObjID, Msg)
    # methods["PartySay"] = lambda: client.PartySay(Msg)
    # methods["PauseResumeSelScript"] = lambda: client.PauseResumeSelScript(ScriptIndex)
    methods["PetsCurrent"] = lambda: stealth.PetsCurrent()
    methods["PetsMax"] = lambda: stealth.MaxPets()
    methods["PoisonResist"] = lambda: stealth.PoisonResist()
    methods["Poisoned"] = lambda: stealth.Poisoned()
    methods["PredictedDirection"] = lambda: stealth.PredictedDirection()
    # methods["PrintScriptMethodsList"] = lambda: client.PrintScriptMethodsList(FileName, SortedList)
    methods["ProfileName"] = lambda: stealth.ProfileName()
    methods["ProfileShardName"] = lambda: stealth.ProfileShardName()
    methods["ProxyIP"] = lambda: stealth.ProxyIP()
    methods["ProxyPort"] = lambda: stealth.ProxyPort()
    # methods["QuestRequest"] = lambda: client.QuestRequest()
    methods["Race"] = lambda: stealth.Race()
    methods["ReadStaticsXY"] = lambda: stealth.ReadStaticsXY(X, Y, WorldNum)
    # methods["RemoveFromParty"] = lambda: client.RemoveFromParty(ObjID)
    # methods["RenameMobile"] = lambda: client.RenameMobile(MobID, NewName)
    # methods["ReqVirtuesGump"] = lambda: client.ReqVirtuesGump()
    # methods["RequestContextMenu"] = lambda: client.RequestContextMenu(ObjID)
    # methods["RequestStats"] = lambda: client.RequestStats(ObjID)
    # methods["Salute"] = lambda: client.Salute()
    methods["SetARExtParams"] = lambda: stealth.SetARExtParams(ShardName, CharName, UseAtEveryConnect)
    methods["SetARStatus"] = lambda: stealth.SetARStatus(ValueBool)
    methods["SetAlarm"] = lambda: stealth.Alarm()
    methods["SetAutoBuyDelay"] = lambda: stealth.SetAutoBuyDelay(ValueInt)
    methods["SetAutoSellDelay"] = lambda: stealth.SetAutoSellDelay(ValueInt)
    methods["SetBadLocation"] = lambda: stealth.SetBadLocation(X, Y)
    methods["SetBadObject"] = lambda: stealth.SetBadObject(ObjType, Color, Radius)
    methods["SetCatchBag"] = lambda: stealth.SetCatchBag(ObjID)
    methods["SetContextMenuHook"] = lambda: stealth.SetContextMenuHook(MenuID, EntryNumber)
    # methods["SetDress"] = lambda: client.SetDress()
    methods["SetDressSpeed"] = lambda: stealth.SetDressSpeed(ValueInt)
    methods["SetDropCheckCoord"] = lambda: stealth.SetDropCheckCoord(ValueBool)
    methods["SetDropDelay"] = lambda: stealth.SetDropDelay(ValueInt)
    methods["SetEventCallback"] = lambda: stealth.SetEventCallback(EventIndex)
    methods["SetFindDistance"] = lambda: stealth.SetFindDistance(ValueInt)
    methods["SetFindInNulPoint"] = lambda: stealth.SetFindInNulPoint(ValueBool)
    methods["SetFindVertical"] = lambda: stealth.SetFindVertical(ValueInt)
    methods["SetGlobal"] = lambda: stealth.SetGlobal(GlobalRegion, VarName, VarValue)
    methods["SetGoodLocation"] = lambda: stealth.SetGoodLocation(X, Y)
    methods["SetJournalLine"] = lambda: stealth.SetJournalLine(StringIndex, Text)
    methods["SetMoveBetweenTwoCorners"] = lambda: stealth.SetMoveBetweenTwoCorners(ValueBool)
    methods["SetMoveCheckStamina"] = lambda: stealth.SetMoveCheckStamina(ValueInt)
    methods["SetMoveHeuristicMult"] = lambda: stealth.SetMoveHeuristicMult(100)
    methods["SetMoveOpenDoor"] = lambda: stealth.SetMoveOpenDoor(ValueBool)
    methods["SetMoveThroughCorner"] = lambda: stealth.SetMoveThroughCorner(ValueBool)
    methods["SetMoveThroughNPC"] = lambda: stealth.SetMoveThroughNPC(ValueInt)
    methods["SetMoveTurnCost"] = lambda: stealth.SetMoveTurnCost(5)
    methods["SetPauseScriptOnDisconnectStatus"] = lambda: stealth.SetPauseScriptOnDisconnectStatus(ValueBool)
    # methods["SetPickupedItem"] = lambda: client.SetPickupedItem(ID)
    methods["SetScriptName"] = lambda: stealth.SetScriptName(ScriptIndex, ValueStr)
    methods["SetShowIPCExceptionWindow"] = lambda: stealth.SetShowIPCExceptionWindow(ValueBool)
    methods["SetSilentMode"] = lambda: stealth.SetSilentMode(ValueBool)
    # methods["SetSkillLockState"] = lambda: client.SetSkillLockState(SkillID, skillState)
    # methods["SetStatState"] = lambda: client.SetStatState(statNum, statState)
    # methods["SetRunMountTimer"] = lambda: client.SetRunMountTimer(105)
    methods["SetRunUnmountTimer"] = lambda: stealth.SetRunUnmountTimer(205)
    methods["SetWalkMountTimer"] = lambda: stealth.SetWalkMountTimer(205)
    methods["SetWalkUnmountTimer"] = lambda: stealth.SetWalkUnmountTimer(405)
    # methods["SetWarMode"] = lambda: client.SetWarMode(ValueBool)
    methods["Sex"] = lambda: stealth.Sex()
    methods["ShardName"] = lambda: stealth.ShardName()
    methods["ShardPath"] = lambda: stealth.GetShardPath()
    # methods["StartScript"] = lambda: stealth.StartScript(ScriptPath)
    methods["StealthPath"] = lambda: stealth.StealthPath()
    methods["StealthProfilePath"] = lambda: stealth.GetStealthProfilePath()
    # methods["Step"] = lambda: client.Step(Direction, Running)
    # methods["StepQ"] = lambda: client.StepQ(Direction, Running)
    # methods["StopAllScripts"] = lambda: client.StopAllScripts()
    # methods["StopScript"] = lambda: client.StopScript(ScriptIndex)
    # methods["TargetByResource"] = lambda: client.TargetByResource(ObjID, Resource)
    methods["TargetID"] = lambda: stealth.TargetID()
    # methods["TargetToObject"] = lambda: client.TargetToObject(ObjID)
    # methods["TargetToTile"] = lambda: client.TargetToTile(Tile, X, Y, Z)
    # methods["TargetToXYZ"] = lambda: client.TargetToXYZ(X, Y, Z)
    # methods["ToggleFly"] = lambda: client.ToggleFly()
    # methods["TradeCheck"] = lambda: client.TradeCheck(TradeNum, Num)
    methods["TradeCount"] = lambda: stealth.TradeCount()
    # methods["UOSay"] = lambda: client.UOSay(Text)
    # methods["UOSayColor"] = lambda: client.UOSayColor(Text, Color)
    # methods["UnequipItemsSetMacro"] = lambda: client.UnequipItemsSetMacro()
    methods["UnsetCatchBag"] = lambda: stealth.UnsetCatchBag()
    # methods["UseFromGround"] = lambda: client.UseFromGround(ObjType, Color)
    # methods["UseItemOnMobile"] = lambda: client.UseItemOnMobile(ItemSerial, TargetSerial)
    # methods["UseObject"] = lambda: client.UseObject(ObjID)
    methods["UseProxy"] = lambda: stealth.UseProxy()
    # methods["UsePrimaryAbility"] = lambda: client.UsePrimaryAbility()
    # methods["UseSecondaryAbility"] = lambda: client.UseSecondaryAbility()
    # methods["UseSelfPaperdollScroll"] = lambda: client.UseSelfPaperdollScroll()
    # methods["UseOtherPaperdollScroll"] = lambda: client.UseOtherPaperdollScroll(ObjID)
    # methods["UseSkill"] = lambda: client.UseSkill(SkillID)
    # methods["UseType"] = lambda: client.UseType(ObjType, Color)
    # methods["UseVirtue"] = lambda: client.UseVirtue(VirtueID)
    # methods["WaitGump"] = lambda: client.WaitGump(ValueInt)
    # methods["WaitMenu"] = lambda: client.WaitMenu(MenuCaption, ElementCaption)
    # methods["WaitTargetGround"] = lambda: client.WaitTargetGround(ObjType)
    # methods["WaitTargetLast"] = lambda: client.WaitTargetLast()
    # methods["WaitTargetObject"] = lambda: client.WaitTargetObject(ObjID)
    # methods["WaitTargetSelf"] = lambda: client.WaitTargetSelf()
    # methods["WaitTargetTile"] = lambda: client.WaitTargetTile(Tile, X, Y, Z)
    # methods["WaitTargetType"] = lambda: client.WaitTargetType(ObjType)
    # methods["WaitTargetXYZ"] = lambda: client.WaitTargetXYZ(X, Y, Z)
    # methods["WaitTextEntry"] = lambda: client.WaitTextEntry(ValueStr)
    methods["WarTargetID"] = lambda: stealth.WarTargetID()
    # methods["WearItem"] = lambda: client.WearItem(Layer, ObjID)
    methods["Weight"] = lambda: stealth.Weight()

    return methods


async def stress_test(methods, call_count=1, print_pass=True, print_fails=False, print_result=False, test_random=False, print_batch_time=False):
    if call_count < 1:
        return

    print(f"Testing {len(methods)} methods closures, batch {call_count} call per closure")
    successes = 0
    fails = 0

    methods_names = list(methods.keys())

    for i, (method_name, method) in enumerate(methods.items()):
        try:
            if not print_fails:
                print(f"testing \"{method_name}\"...")

            time = datetime.now()

            for _ in range(call_count):
                result = await call_method(method)

            successes += 1

            time = datetime.now() - time
            if print_batch_time:
                time_ms = time.total_seconds() * 1000
                if time_ms > call_count:    # ! threshold
                    print(f"total batch time: {time_ms:>8.1f}, avg {time_ms/call_count:>8.4f} {method_name}")

            if print_pass:
                print(f"\"{method_name}\" test pass" + f", result = {result}" if print_result else "")

        except Exception as e:
            fails += 1

            if print_fails:
                print(f"test failed, \"{method_name}\" caused an error: {e}")

    print(f"success {successes} / total {len(methods)} / failed {fails}")


async def main():
    print("Connecting to Stealth...")
    stealth = AsyncStealthApiClient()
    await stealth.connect()

    # stealth = SyncStealthApiClient()
    # stealth.connect()

    # import py_stealth as stealth
    # import py_astealth.stealth as stealth

    print("Connected.")

    time = datetime.now()
    batch_size = 1000

    methods = await method_generator(stealth)
    await stress_test(methods, batch_size, print_pass=False, print_fails=True, print_result=True, print_batch_time=False)

    time = datetime.now() - time
    time_ms = time.total_seconds() * 1000

    print(f"total time, milliseconds: {time_ms:>8.1f}, avg per method batch {time_ms / len(methods):>8.4f}, avg per method {time_ms / len(methods) / batch_size:>8.4f}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
