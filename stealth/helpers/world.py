"""World, map, static, tile, etc helpers."""
from typing import Union, List
from dataclasses import asdict

from py_astealth.stealth import api
from py_astealth.stealth_enums import TileGroup
from py_astealth.stealth_structs import FoundTile, UserStaticItem, StaticItemRealXY


# Tile helpers
def GetTileFlags(tile_group: Union[str, TileGroup], tile: int) -> int:
    """
    Get flags for a tile.

    Args:
        tile_group: TileGroup enum or 'Land'/'Static' string
        tile: Tile ID

    Returns:
        Tile flags
    """
    if isinstance(tile_group, str):
        tile_group = tile_group.lower()
        if tile_group in ('tfland', 'land'):
            tile_group = TileGroup.Land
        elif tile_group in ('tfstatic', 'static'):
            tile_group = TileGroup.Static
        else:
            raise ValueError('GetTileFlags: TileGroup must be "Land" or "Static"')

    return api.GetTileFlags(int(tile_group), tile)


def ConvertIntegerToFlags(group: Union[str, TileGroup], flags: int) -> List[str]:
    """
    Convert integer flags to list of string descriptions.

    Args:
        group: TileGroup enum or 'Land'/'Static' string
        flags: Flags value

    Returns:
        List of flag names
    """
    if isinstance(group, str):
        group = group.lower()
        if group in ('tfland', 'land'):
            group = TileGroup.Land
        elif group in ('tfstatic', 'static'):
            group = TileGroup.Static
        else:
            raise ValueError('ConvertIntegerToFlags: Group must be "Land" or "Static"')

    return api.ConvertIntegerToFlags(int(group), flags)


def GetStaticTiles(xmin: int, ymin: int, xmax: int, ymax: int, world_num: int, tile_types: list[int]) -> list[FoundTile]:
    return api.GetStaticTilesArray(xmin, ymin, xmax, ymax, world_num, tile_types)


def GetStaticTilesArray(
        xmin: int, ymin: int, xmax: int, ymax: int,
        world_num: int,
        tile_types: Union[list[int], int]) -> list[tuple[int, int, int, int]]:
    if isinstance(tile_types, int):
        tile_types = [tile_types]

    return [(tile.tile, tile.x, tile.y, tile.z) for tile in
            GetStaticTiles(xmin, ymin, xmax, ymax, world_num, tile_types)]


def GetLandTiles(xmin: int, ymin: int, xmax: int, ymax: int, world_num: int, tile_types: list[int]) -> list[FoundTile]:
    return api.GetLandTilesArray(xmin, ymin, xmax, ymax, world_num, tile_types)


def GetLandTilesArray(
        xmin: int, ymin: int, xmax: int, ymax: int,
        world_num: int,
        tile_types: Union[list[int], int]) -> list[tuple[int, int, int, int]]:
    if isinstance(tile_types, int):
        tile_types = [tile_types]

    return [(tile.tile, tile.x, tile.y, tile.z) for tile in
            GetLandTiles(xmin, ymin, xmax, ymax, world_num, tile_types)]


def CreateUserStatic(static_item: UserStaticItem, world_num: int) -> int:
    return api.CreateUserStatic(static_item, world_num)


def AddUserStatic(tile: int, x: int, y: int, z: int, color: int, world_num: int) -> int:
    return CreateUserStatic(UserStaticItem(tile, x, y, z, color), world_num)


def AddUserStaticItem(static_item: dict, world_num: int):
    return AddUserStatic(static_item["tile"], static_item["x"], static_item["y"], static_item["z"], static_item["color"], world_num)


def ReadStatics(x: int, y: int, world: int) -> list[StaticItemRealXY]:
    return api.ReadStaticsXY(x, y, world)


def ReadStaticsXY(x: int, y: int, world: int) -> list[dict[str, int]]:
    return [asdict(tile) for tile in api.ReadStaticsXY(x, y, world)]


__all__ = ['GetTileFlags', 'ConvertIntegerToFlags',
           'GetStaticTiles', 'GetStaticTilesArray',
           'GetLandTiles', 'GetLandTilesArray',
           'CreateUserStatic', 'AddUserStatic', 'AddUserStaticItem',
           'ReadStatics', 'ReadStaticsXY']
