"""Mover settings and helper functions."""
from typing import Union, List, Optional, Callable

from py_astealth.stealth import api
from py_astealth.stealth_enums import TileGroup
from py_astealth.stealth_structs import FoundTile, WorldPoint, UserStaticItem

from .common import Wait, AddToSystemJournal
from .utils import CalcDir


class MoverSettings:
    """Wrapper for mover configuration settings."""
    
    @property
    def OpenDoors(self) -> bool:
        """Get/Set if mover should automatically open doors."""
        return api.GetMoveOpenDoor()
    
    @OpenDoors.setter
    def OpenDoors(self, value: bool):
        api.SetMoveOpenDoor(value)

    @property
    def ThroughNPC(self) -> int:
        """Get/Set if mover should move through NPCs (0=No, 1=Yes)."""
        return api.GetMoveThroughNPC()
    
    @ThroughNPC.setter
    def ThroughNPC(self, value: int):
        api.SetMoveThroughNPC(value)

    @property
    def ThroughCorner(self) -> bool:
        """Get/Set if mover should cut corners."""
        return api.GetMoveThroughCorner()
    
    @ThroughCorner.setter
    def ThroughCorner(self, value: bool):
        api.SetMoveThroughCorner(value)

    @property
    def HeuristicMult(self) -> int:
        """Get/Set heuristic multiplier for pathfinding."""
        return api.GetMoveHeuristicMult()
    
    @HeuristicMult.setter
    def HeuristicMult(self, value: int):
        api.SetMoveHeuristicMult(value)

    @property
    def CheckStamina(self) -> int:
        """Get/Set minimum stamina to move."""
        return api.GetMoveCheckStamina()
    
    @CheckStamina.setter
    def CheckStamina(self, value: int):
        api.SetMoveCheckStamina(value)

    @property
    def TurnCost(self) -> int:
        """Get/Set movement cost for turning."""
        return api.GetMoveTurnCost()
    
    @TurnCost.setter
    def TurnCost(self, value: int):
        api.SetMoveTurnCost(value)

    @property
    def BetweenTwoCorners(self) -> bool:
        """Get/Set if mover can move between two corners."""
        return api.GetMoveBetweenTwoCorners()
    
    @BetweenTwoCorners.setter
    def BetweenTwoCorners(self, value: bool):
        api.SetMoveBetweenTwoCorners(value)

    # Timers
    @property
    def RunUnmountTimer(self) -> int:
        """Get/Set delay between steps when running unmounted."""
        return api.GetRunUnmountTimer()
    
    @RunUnmountTimer.setter
    def RunUnmountTimer(self, value: int):
        api.SetRunUnmountTimer(value)

    @property
    def WalkMountTimer(self) -> int:
        """Get/Set delay between steps when walking mounted."""
        return api.GetWalkMountTimer()
    
    @WalkMountTimer.setter
    def WalkMountTimer(self, value: int):
        api.SetWalkMountTimer(value)

    @property
    def RunMountTimer(self) -> int:
        """Get/Set delay between steps when running mounted."""
        return api.GetRunMountTimer()
    
    @RunMountTimer.setter
    def RunMountTimer(self, value: int):
        api.SetRunMountTimer(value)

    @property
    def WalkUnmountTimer(self) -> int:
        """Get/Set delay between steps when walking unmounted."""
        return api.GetWalkUnmountTimer()
    
    @WalkUnmountTimer.setter
    def WalkUnmountTimer(self, value: int):
        api.SetWalkUnmountTimer(value)


# Global instance
Mover = MoverSettings()


def GetPath3D(StartX: int, StartY: int, StartZ: int,
              FinishX: int, FinishY: int, FinishZ: int,
              WorldNum: int,
              AccuracyXY: int, AccuracyZ: int,
              Run: bool) -> list[WorldPoint]:
    """
    GetPath3D calculates the path from the start point to the end point with the specified accuracy.
    Returns a list of path points.
    If the path is not found, an empty list is returned.
    """

    return api.GetPathArray3D(StartX, StartY, StartZ, FinishX, FinishY, FinishZ, WorldNum, AccuracyXY, AccuracyZ, Run)


def GetPathArray3D(StartX: int, StartY: int, StartZ: int,
                   FinishX: int, FinishY: int, FinishZ: int,
                   WorldNum: int,
                   AccuracyXY: int, AccuracyZ: int,
                   Run: bool) -> list[[tuple[int, int, int]]]:
    """
    GetPathArray3D is a legacy function, use GetPath3D instead
    """

    return [(p.x, p.y, p.z) for p in GetPath3D(StartX, StartY, StartZ,
                                               FinishX, FinishY, FinishZ,
                                               WorldNum,
                                               AccuracyXY, AccuracyZ,
                                               Run)]


# Movement helpers
def NewMoveXYZ(x_dst, y_dst, z_dst, accuracy_xy, accuracy_z, running) -> bool:
    return api.MoveXYZ(x_dst, y_dst, z_dst, accuracy_xy, accuracy_z, running)


def newMoveXYZ(x_dst, y_dst, z_dst, accuracy_xy, accuracy_z, running, callback: Optional[Callable] = None) -> bool:
    """
    Advanced MoveXYZ with callback support.
    """
    def debug(msg):
        if getattr(newMoveXYZ, 'debug', False):
            AddToSystemJournal('MoveXYZ: ' + msg)

    def step(direction, run):
        while True:
            res = api.StepQ(direction, run)
            if res == -2 or res >= 0:
                return res >= 0
            Wait(10)

    if not hasattr(newMoveXYZ, 'debug'):
        newMoveXYZ.debug = False

    find_path = True
    while True:
        # pause while not connected
        while not api.Connected():
            Wait(100)
            
        # try to find a path if required
        if find_path:
            find_path = False
            path = api.GetPathArray3D(
                api.PredictedX(), api.PredictedY(), api.PredictedZ(),
                x_dst, y_dst, z_dst,
                api.WorldNum(), accuracy_xy, accuracy_z, running
            )
            # there is no path to a target location
            if not path:
                debug('There is no path to a target location.')
                return False
            debug('Path found. Length = ' + str(len(path)))
            
        # check path passability for a few steps
        cx, cy, cz = api.PredictedX(), api.PredictedY(), api.PredictedZ()

        for pt in path[:4]:
            if api.IsWorldCellPassable(cx, cy, cz, pt.x, pt.y, api.WorldNum()):
                cx, cy, cz = pt.x, pt.y, pt.z
            else:
                debug(f'Point ({pt.x}, {pt.y}, {pt.z}) is not passable.')
                find_path = True
                break

        if find_path:
            continue
            
        # stamina check
        if not api.Dead() and api.Stam() < api.GetMoveCheckStamina():
            Wait(100)
            
        # lets walk :)
        mx, my = api.PredictedX(), api.PredictedY()
        pt = path.pop(0)
        x, y, z = pt.x, pt.y, pt.z
        
        dx = mx - x
        dy = my - y
        direction = CalcDir(mx, my, x, y)
        
        # if something wrong
        if (dx == 0 and dy == 0) or (abs(dx) > 1 or abs(dy) > 1) or direction == 100:
            debug(f'dx = {dx}, dy = {dy}, dir = {direction}')
            find_path = True
            continue
            
        # try to turn if required
        if api.PredictedDirection() != direction:
            if not step(direction, running):
                find_path = True
                continue
                
        # try to do a step
        if not step(direction, running):
            find_path = True
            continue
            
        # call a callback object if it is not None
        if callback is not None and not callback(x, y, z):
            return False
                
        # looks like it is done
        if not path:
            mx, my = api.PredictedX(), api.PredictedY()
            # ensure this
            if abs(mx - x_dst) <= accuracy_xy and abs(my - y_dst) <= accuracy_xy:
                debug('Location reached!')
                return True
            # nope (
            debug('Wtf? Recompute path.')
            find_path = True


def newMoveXY(x_dst, y_dst, optimized, accuracy, running):
    """Wrapper for newMoveXYZ."""
    return api.MoveXYZ(x_dst, y_dst, 0, accuracy, 255, running)


def NewMoveXY(x_dst, y_dst, optimized, accuracy, running) -> bool:
    """Wrapper for newMoveXYZ."""
    return newMoveXY(x_dst, y_dst, optimized, accuracy, running)


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

    return [(tile.tile, tile.x, tile.y, tile.z) for tile in GetStaticTiles(xmin, ymin, xmax, ymax, world_num, tile_types)]


def CreateUserStatic(static_item: UserStaticItem, world_num: int) -> int:
    return api.CreateUserStatic(static_item, world_num)


def AddUserStatic(tile: int, x: int, y: int, z: int, color: int, world_num: int) -> int:
    return CreateUserStatic(UserStaticItem(tile, x, y, z, color), world_num)


def AddUserStaticItem(static_item: dict, world_num: int):
    return AddUserStatic(static_item["tile"], static_item["x"], static_item["y"], static_item["z"], static_item["color"], world_num)


__all__ = ['MoverSettings', 'Mover',
           'GetPath3D', 'GetPathArray3D',
           'NewMoveXYZ', 'newMoveXYZ', 'NewMoveXY', "newMoveXY",
           'GetTileFlags', 'ConvertIntegerToFlags',
           'GetStaticTiles', 'GetStaticTilesArray',
           'CreateUserStatic', 'AddUserStatic', 'AddUserStaticItem']
