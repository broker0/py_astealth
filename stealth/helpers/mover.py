"""Mover settings and helper functions."""
from typing import Optional, Callable

from py_astealth.stealth import api
from py_astealth.stealth_structs import WorldPoint

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


def newMoveXYZ(x_dst, y_dst, z_dst, accuracy_xy, accuracy_z, running, callback: Optional[Callable] = None, wait_sync = True) -> bool:
    """
    Advanced MoveXYZ with callback support.
    """
    def debug(msg):
        if getattr(newMoveXYZ, 'debug', False):
            AddToSystemJournal(f'MoveXYZ: {msg}')

    def step(direction, run):
        while True:
            res = api.StepQ(direction, run)
            if res == -2 or res >= 0:
                return res >= 0
            Wait(10)

    def is_reached() -> bool:
        return (abs(api.PredictedX() - x_dst) <= accuracy_xy and
                abs(api.PredictedY() - y_dst) <= accuracy_xy and
                abs(api.PredictedZ() - z_dst) <= accuracy_z)

    def is_passable_ahead(lookahead=4):
        cx, cy, cz = api.PredictedX(), api.PredictedY(), api.PredictedZ()
        for pt in path[:lookahead]:
            passable, dest_z = api.IsWorldCellPassable(cx, cy, cz, pt.x, pt.y, api.WorldNum())
            if not passable or dest_z != pt.z:
                debug(f'({pt.x}, {pt.y}, {pt.z}) is not passable')
                return False
            cx, cy, cz = pt.x, pt.y, pt.z

        return True

    if not hasattr(newMoveXYZ, 'debug'):
        newMoveXYZ.debug = False

    path = []
    recompute = True

    while True:
        # pause while not connected
        while not api.Connected():
            Wait(100)

        if is_reached():
            debug('Location reached!')
            if wait_sync:
                self = api.Self()
                for _ in range(10):
                    curr_pos = api.GetX(self), api.GetY(self), api.GetZ(self), api.GetDirection(self)
                    predicted_pos = api.PredictedX(), api.PredictedY(), api.PredictedZ(), api.PredictedDirection()
                    if curr_pos == predicted_pos:
                        break
                    Wait(50)

            return True

        if recompute:
            recompute = False
            path = api.GetPathArray3D(
                api.PredictedX(), api.PredictedY(), api.PredictedZ(),
                x_dst, y_dst, z_dst,
                api.WorldNum(), accuracy_xy, accuracy_z, running
            )

            if not path:
                debug('No path found')
                return False

            debug(f'Path found, {len(path)} steps')

        if not is_passable_ahead():
            recompute = True
            continue

        # prepare next step
        pt = path[0]
        mx, my = api.PredictedX(), api.PredictedY()
        direction = CalcDir(mx, my, pt.x, pt.y)

        if direction == 100 or abs(mx - pt.x) > 1 or abs(my - pt.y) > 1:
            debug(f'Desync: dx={mx - pt.x}, dy={my - pt.y}, dir={direction}')
            recompute = True
            continue

        if api.PredictedDirection() != direction:
            if not step(direction, running):
                debug(f'Failed to turn to direction {direction}')
                recompute = True
                continue

        if not step(direction, running):
            debug(f'Failed to step to {pt.x}, {pt.y}')
            recompute = True
            continue

        # step complete
        path.pop(0)

        if callback is not None and not callback(pt.x, pt.y, pt.z):
            return False

        if not path:
            recompute = True


def newMoveXY(x_dst, y_dst, optimized, accuracy, running):
    """Wrapper for newMoveXYZ."""
    return api.MoveXYZ(x_dst, y_dst, 0, accuracy, 255, running)


def NewMoveXY(x_dst, y_dst, optimized, accuracy, running) -> bool:
    """Wrapper for newMoveXYZ."""
    return newMoveXY(x_dst, y_dst, optimized, accuracy, running)




__all__ = ['MoverSettings', 'Mover',
           'GetPath3D', 'GetPathArray3D',
           'NewMoveXYZ', 'newMoveXYZ', 'NewMoveXY', "newMoveXY",
]
