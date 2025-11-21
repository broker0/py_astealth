from dataclasses import dataclass
from py_astealth.stealth_types import *
from py_astealth.core.base_types import StructType


# Using the @StructType.register decorator registers fields (arguments of constructor) for serialization.
# When using the @dataclass decorator, you only need to declare the fields, __init__ will be created automatically.
# The order of the decorators is important - @StructType.register comes first, followed by @dataclass.
# Thus, @dataclass is executed first and creates an annotated constructor for the type, and @StructType.register
# parses the constructor arguments and registers them as serializable fields of the given structure.
@StructType.register
@dataclass
class WorldPoint(StructType):
    x: U16
    y: U16
    z: I8


@StructType.register
@dataclass
class FoundTile(StructType):
    tile: U16
    x: U16
    y: U16
    z: I8


@StructType.register
@dataclass
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
@dataclass
class MultiPart(StructType):
    graphic: U16
    x: U16
    y: U16
    z: I8
    flag: U32


@StructType.register
@dataclass
class AboutData(StructType):
    version: list[U16]
    build: U16
    build_date: DateTime
    git_rev_num: U16
    git_rev: String


@StructType.register
@dataclass
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
    TithingPoints: I32
    ArmorMax: U16
    FireResistMax: U16
    ColdResistMax: U16
    PoisonResistMax: U16
    EnergyResistMax: U16
    DefenseChance: U16
    DefenseChanceMax: U16
    HitChanceIncr: U16
    DamageIncr: U16
    SwingSpeedIncr: U16
    LowerReagentCost: U16
    SpellDamageIncr: U16
    FasterCastRecovery: U16
    FasterCasting: U16
    LowerManaCost: U16
    HpRegen: U16
    SpRegen: U16
    MpRegen: U16
    ReflectPhysDamage: U16
    EnhancePotions: U16
    StrIncr: U16
    DexIncr: U16
    IntIncr: U16
    HpIncr: U16
    SpIncr: U16
    MpIncr: U16


@StructType.register
@dataclass
class LandTileData(StructType):
    Flags: U32
    Flags2: U32
    TextureID: U16
    Name: String


@StructType.register
@dataclass
class StaticTileData(StructType):
    Flags: U64
    Weight: U16
    AnimID: U16
    Height: I32
    R: U8
    G: U8
    B: U8
    A: U8
    Name: String


@StructType.register
@dataclass
class StaticItemRealXY(StructType):
    Tile: U16
    X: U16
    Y: U16
    Z: I8
    Color: U16


@StructType.register
@dataclass
class MapCell(StructType):
    Tile: U16
    Z: I8


@StructType.register
@dataclass
class MenuItem(StructType):
    Model: U16
    Color: U16
    Text: String


@StructType.register
@dataclass
class ScriptInfo(StructType):
    Index: U32
    Name: String
    State: U8


@StructType.register
@dataclass
class TargetInfo(StructType):
    ID: U32
    Tile: U16
    X: U16
    Y: U16
    Z: I8


@StructType.register
@dataclass
class UserStaticItem(StructType):
    Tile: U16
    Tile: U16
    X: U16
    Y: U16
    Z: I8
    Color: U16


@StructType.register
@dataclass
class ClilocRec(StructType):
    Cliloc_ID: U32
    Params: list[String]


@StructType.register
@dataclass
class Point(StructType):
    X: I32
    Y: I32


@StructType.register
@dataclass
class MapFigure(StructType):
    Kind: U16
    Coord: U16
    X1: I32
    Y1: I32
    X2: I32
    Y2: U32
    BrushColor: U32
    BrushStyle: U16
    WorldNum: U8
    Text: String


@StructType.register
@dataclass
class BuffBarInfo(StructType):
    Attribute_ID: U16
    TimeStart: F64
    Seconds: U16
    ClilocID1: U32
    ClilocID2: U32
    ClilocID3: U32
    BuffText: String


####################################################################################################################
# gump elements
####################################################################################################################
@StructType.register
@dataclass
class GumpGroup(StructType):
    Number: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
class GumpEndGroup(StructType):
    Number: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
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
@dataclass
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
@dataclass
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
@dataclass
class GumpCheckerTrans(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
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
@dataclass
class GumpPic(StructType):
    X: I32
    Y: I32
    ID: I32
    Hue: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
class GumpPicTiled(StructType):
    X: I32
    Y: I32
    Width: I32
    Height: I32
    GumpID: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
class GumpRadioButton(StructType):
    X: I32
    Y: I32
    ReleasedID: I32
    PressedID: I32
    Status: I32
    ReturnValue: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
class GumpResizePic(StructType):
    X: I32
    Y: I32
    GumpID: I32
    Width: I32
    Height: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
class GumpText(StructType):
    X: I32
    Y: I32
    Color: I32
    TextID: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
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
@dataclass
class GumpSimpleText(StructType):
    Text: String


@StructType.register
@dataclass
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
@dataclass
class GumpTilePic(StructType):
    X: I32
    Y: I32
    ID: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
class GumpTilePicHue(StructType):
    X: I32
    Y: I32
    ID: I32
    Color: I32
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
class GumpTooltip(StructType):
    ClilocID: I32
    Arguments: String
    Page: I32
    ElemNum: I32


@StructType.register
@dataclass
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
@dataclass
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
@dataclass
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
@dataclass
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
@dataclass
class GumpItemProperty(StructType):
    Prop: U32
    ElemNum: I32


@StructType.register
@dataclass
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
@dataclass
class GumpInfo(StructType):
    gump: Gump
    Groups: list[GumpGroup]
    EndGroups: list[GumpEndGroup]
    Buttons: list[GumpButton]
    ButtonsTileArt: list[GumpButtonTileArt]
    CheckBoxes: list[GumpCheckBox]
    Checkers: list[GumpCheckerTrans]
    CroppedText: list[GumpCroppedText]
    Pics: list[GumpPic]
    PicsTiled: list[GumpPicTiled]
    RadioButtons: list[GumpRadioButton]
    ResizePics: list[GumpResizePic]
    Texts: list[GumpText]
    TextEntries: list[GumpTextEntry]
    SimpleTexts: list[GumpSimpleText]
    TextEntriesLimited: list[GumpTextEntryLimited]
    TilePics: list[GumpTilePic]
    TilePicsHued: list[GumpTilePicHue]
    Tooltips: list[GumpTooltip]
    Htmls: list[GumpHtml]
    XmfHtmls: list[GumpXmfHtml]
    XmfHtmlHued: list[GumpXmfHTMLColor]
    XmfHtmlToks: list[GumpXmfHTMLTok]
    Properties: list[GumpItemProperty]



# TODO other Stealth struct-types


__all__ = [
    name for name, obj in globals().copy().items()
    if isinstance(obj, type) and issubclass(obj, StructType) and obj is not StructType
]
