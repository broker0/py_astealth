from typing import TYPE_CHECKING

from py_astealth.core.base_types import StructType


if TYPE_CHECKING:
    import py_astealth.stealth_types

    #for better IDE support
    Bool = py_astealth.stealth_types.Bool._mapping
    U8 = py_astealth.stealth_types.U8._mapping
    I8 = py_astealth.stealth_types.I8._mapping
    U16 = py_astealth.stealth_types.U16._mapping
    I16 = py_astealth.stealth_types.I16._mapping
    U32 = py_astealth.stealth_types.U32._mapping
    I32 = py_astealth.stealth_types.I32._mapping
    U64 = py_astealth.stealth_types.U64._mapping
    I64 = py_astealth.stealth_types.I64._mapping
    F32 = py_astealth.stealth_types.F32._mapping
    F64 = py_astealth.stealth_types.F64._mapping
    DateTime = py_astealth.stealth_types.DateTime._mapping
    String = py_astealth.stealth_types.String._mapping
else:
    from py_astealth.stealth_types import *


# Using the @StructType.register decorator registers fields (arguments of constructor) for serialization.
# @dataclass decorator will be applied for this class
@StructType.register
class WorldPoint(StructType):
    x: U16
    y: U16
    z: I8


@StructType.register
class FoundTile(StructType):
    tile: U16
    x: U16
    y: U16
    z: I8


@StructType.register
class Multi(StructType):
    id: U32
    x: U16
    y: U16
    z: I8
    xmin: U16
    xmax: U16
    ymin: U16
    ymax: U16
    width: U16
    height: U16


@StructType.register
class MultiPart(StructType):
    graphic: U16
    x: U16
    y: U16
    z: I8
    flag: U32


@StructType.register
class AboutData(StructType):
    version: list[U16]
    build: U16
    build_date: DateTime
    git_rev_num: U16
    git_rev: String


@StructType.register
class ExtendedInfo(StructType):
    MaxWeight: U16
    Race: U8
    StatCap: U16
    PetsCurrent: U8
    PetsMax: U8
    FireResist: U16
    ColdResist: U16
    PoisonResist: U16
    EnergyResist: U16
    Luck: I16
    DamageMin: U16
    DamageMax: U16
    Tithing_points: I32
    ArmorMax: U16
    fireresistMax: U16
    coldresistMax: U16
    poisonresistMax: U16
    energyresistMax: U16
    DefenseChance: U16
    DefenseChanceMax: U16
    Hit_Chance_Incr: U16
    Damage_Incr: U16
    Swing_Speed_Incr: U16
    Lower_Reagent_Cost: U16
    Spell_Damage_Incr: U16
    Faster_Cast_Recovery: U16
    Faster_Casting: U16
    Lower_Mana_Cost: U16
    HP_Regen: U16
    Stam_Regen: U16
    Mana_Regen: U16
    Reflect_Phys_Damage: U16
    Enhance_Potions: U16
    Strength_Incr: U16
    Dex_Incr: U16
    Int_Incr: U16
    HP_Incr: U16
    Stam_Incr: U16
    Mana_Incr: U16


@StructType.register
class LandTileData(StructType):
    Flags: U32
    Flags2: U32
    TextureID: U16
    Name: String


@StructType.register
class StaticTileData(StructType):
    Flags: U64
    Weight: U16
    AnimID: U16
    Height: I32
    R: U8
    G: U8
    B: U8
    A: U8
    Layer: U8
    Name: String


@StructType.register
class StaticItemRealXY(StructType):
    Tile: U16
    X: U16
    Y: U16
    Z: I8
    Color: U16


@StructType.register
class MapCell(StructType):
    Tile: U16
    Z: I8


@StructType.register
class MenuItem(StructType):
    Model: U16
    Color: U16
    Text: String


@StructType.register
class ScriptInfo(StructType):
    Index: U32
    Name: String
    State: U8


@StructType.register
class TargetInfo(StructType):
    ID: U32
    Tile: U16
    X: U16
    Y: U16
    Z: I8


@StructType.register
class UserStaticItem(StructType):
    Tile: U16
    X: U16
    Y: U16
    Z: I8
    Color: U16


@StructType.register
class ClilocRec(StructType):
    Cliloc_ID: U32
    Params: list[String]


@StructType.register
class Point(StructType):
    X: I32
    Y: I32


@StructType.register
class MapFigure(StructType):
    Kind: U8
    Coord: U8
    X1: I32
    Y1: I32
    X2: I32
    Y2: I32
    BrushColor: U32
    BrushStyle: U8
    Color: U32
    WorldNum: U8
    Text: String


@StructType.register
class BuffBarInfo(StructType):
    Attribute_ID: U16
    TimeStart: DateTime
    Seconds: U16
    ClilocID1: U32
    ClilocID2: U32
    ClilocID3: U32
    BuffText: String


@StructType.register
class LayerObject(StructType):
    Layer: U8
    ObjID: U32


@StructType.register
class ContextMenuEntry(StructType):
    Tag: U16
    IntLocID: U32
    Flags: U16
    Color: U16


@StructType.register
class ContextMenuRec(StructType):
    ID: U32
    EntriesNumber: U8
    NewCliloc: Bool
    Entries: list[ContextMenuEntry]


@StructType.register
class WorldItemData(StructType):
    serial: U32
    graphic: U16
    color: U16
    x: U16
    y: U16
    z: I8
    world: U8
    count: U16
    flags: U8


@StructType.register
class MobileData(StructType):
    serial: U32
    graphic: U16
    color: U16
    x: U16
    y: U16
    z: I8
    direction: U8
    world: U8
    flags: U8
    notoriety: U8

    hp: I32
    hp_max: I32
    sp: I32
    sp_max: I32
    mp: I32
    mp_max: I32


@StructType.register
class EquippedItemData(StructType):
    serial: U32
    graphic: U16
    color: U16
    layer: U8
    parent: U32


@StructType.register
class ContentItemData(StructType):
    serial: U32
    graphic: U16
    color: U16
    x: U16
    y: U16
    count: U16
    parent: U32


####################################################################################################################
# gump elements
####################################################################################################################
@StructType.register
class GumpGroup(StructType):
    Number: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpEndGroup(StructType):
    Number: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpButton(StructType):
    X: I32
    Y: I32
    ReleasedID: I32
    PressedID: I32
    Quit: I32
    PageID: I32
    ReturnValue: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpButtonTileArt(StructType):
    X: I32
    Y: I32
    ReleasedID: I32
    PressedID: I32
    Quit: I32
    PageID: I32
    ReturnValue: I32
    ArtID: I32
    Hue: I32
    ArtX: I32
    ArtY: I32
    ElemNum: I32


@StructType.register
class GumpCheckBox(StructType):
    X: I32
    Y: I32
    ReleasedID: I32
    PressedID: I32
    Status: I32
    ReturnValue: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpCheckerTrans(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpCroppedText(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    Color: I32
    TextID: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpPic(StructType):
    X: I32
    Y: I32
    ID: I32
    Hue: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpPicTiled(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    GumpID: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpRadiobutton(StructType):
    X: I32
    Y: I32
    ReleasedID: I32
    PressedID: I32
    Status: I32
    ReturnValue: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpResizePic(StructType):
    X: I32
    Y: I32
    GumpID: I32
    Width: I32
    Height: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpText(StructType):
    X: I32
    Y: I32
    Color: I32
    TextID: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpTextEntry(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    Color: I32
    ReturnValue: I32
    DefaultTextID: I32
    RealValue: String
    Page: I32
    ElemNum: I32


@StructType.register
class Text(StructType):
    Text: String


@StructType.register
class GumpTextEntryLimited(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    Color: I32
    ReturnValue: I32
    Limit: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpTilePic(StructType):
    X: I32
    Y: I32
    ID: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpTilePicHue(StructType):
    X: I32
    Y: I32
    ID: I32
    Color: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpTooltip(StructType):
    ClilocID: I32
    Arguments: String
    Page: I32
    ElemNum: I32


@StructType.register
class GumpHtml(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    TextID: I32
    Background: I32
    Scrollbar: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpXmfHtml(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    ClilocID: U32
    Background: I32
    Scrollbar: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpXmfHTMLColor(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    ClilocID: U32
    Background: I32
    Scrollbar: I32
    Hue: I32
    Page: I32
    ElemNum: I32


@StructType.register
class GumpXmfHTMLTok(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    Background: I32
    Scrollbar: I32
    Color: I32
    ClilocID: U32
    Arguments: String
    Page: I32
    ElemNum: I32


@StructType.register
class GumpItemProperty(StructType):
    Prop: U32
    ElemNum: I32


@StructType.register
class GumpPicInPic(StructType):
    X: I32
    Y: I32
    Graphic: I32
    StartX: I32
    StartY: I32
    Width: I32
    Height: I32
    Hue: I32
    ElemNum: I32


@StructType.register
class GumpTilePicAsGumpPic(StructType):
    X: I32
    Y: I32
    Graphic: I32
    Color: I32
    Race: I32
    BodyID: I32
    ElemNum: I32


@StructType.register
class GumpToggleUpperWordCase(StructType):
    Argument: String
    ElemNum: I32


@StructType.register
class GumpToggleCroppedText(StructType):
    Argument: String
    ElemNum: I32


@StructType.register
class GumpECHandleInput(StructType):
    Argument: String
    ElemNum: I32


@StructType.register
class Gump(StructType):
    Serial: U32
    GumpID: U32
    X: I16
    Y: I16
    Pages: I32
    NoMove: Bool
    NoResize: Bool
    NoDispose: Bool
    NoClose: Bool


@StructType.register
class GumpInfo(StructType):
    gump: Gump
    groups: list[GumpGroup]
    EndGroups: list[GumpEndGroup]
    GumpButtons: list[GumpButton]
    ButtonsTileArt: list[GumpButtonTileArt]
    CheckBoxes: list[GumpCheckBox]
    CheckerTrans: list[GumpCheckerTrans]
    CroppedText: list[GumpCroppedText]
    GumpPics: list[GumpPic]
    GumpPicTiled: list[GumpPicTiled]
    RadioButtons: list[GumpRadiobutton]
    ResizePics: list[GumpResizePic]
    GumpText: list[GumpText]
    TextEntries: list[GumpTextEntry]
    Text: list[Text]
    TextEntriesLimited: list[GumpTextEntryLimited]
    TilePics: list[GumpTilePic]
    TilePicsHued: list[GumpTilePicHue]
    Tooltips: list[GumpTooltip]
    HtmlGump: list[GumpHtml]
    XmfHtmlGump: list[GumpXmfHtml]
    XmfHTMLGumpColor: list[GumpXmfHTMLColor]
    XmfHtmlTok: list[GumpXmfHTMLTok]
    ItemProperties: list[GumpItemProperty]
    PicInPics: list[GumpPicInPic]
    TilePicAsGumpPics: list[GumpTilePicAsGumpPic]
    ToggleUpperWordCases: list[GumpToggleUpperWordCase]
    ToggleCroppedTexts: list[GumpToggleCroppedText]
    ECHandleInputs: list[GumpECHandleInput]


# TODO other Stealth struct-types


__all__ = [
    name for name, obj in globals().copy().items()
    if isinstance(obj, type) and issubclass(obj, StructType) and obj is not StructType
]
