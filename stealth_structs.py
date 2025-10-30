from dataclasses import dataclass

from py_astealth.stealth_types import *
from py_astealth.core.base_types import StructType

__all__ = ["WorldPoint", "FoundTile", "Multi", "MultiPart", "AboutData"]


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


# TODO other Stealth struct-types
