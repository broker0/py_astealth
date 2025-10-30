from dataclasses import dataclass

from py_astealth.stealth_types import *
from py_astealth.core.base_types import StructType

__all__ = ["WorldPoint", "FoundTile"]


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

# TODO other Stealth struct-types
