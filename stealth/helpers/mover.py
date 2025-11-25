"""Mover settings and helper functions."""
from py_astealth.stealth import api


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


# LOS helpers
def CheckLOS(xf, yf, zf, xt, yt, zt, world_num, check_type='Sphere', options=None) -> bool:
    """
    Check Line Of Sight between two points.
    
    Args:
        xf, yf, zf: From coordinates
        xt, yt, zt: To coordinates
        world_num: World number
        check_type: 'Sphere', 'SphereAdv', 'Pol', or 'RunUO'
        options: List of options or single option string
                 ('SphereCheckCorners', 'PolUseNoShoot', 'PolLosThroughWindow')
                 
    Returns:
        True if LOS exists, False otherwise
    """
    # Map string types to integers
    los_types = {
        'sphere': 1, 'lossphere': 1,
        'sphereadv': 2, 'lossphereadv': 2,
        'pol': 3, 'lospol': 3,
        'runuo': 4, 'losrunuo': 4, 'servuo': 4
    }
    
    los_options = {
        'spherecheckcorners': 0x100, 'losspherecheckcorners': 0x100,
        'polusenoshoot': 0x200, 'lospolusenoshoot': 0x200,
        'pollosthroughwindow': 0x400, 'lospollosthroughwindow': 0x400
    }

    # Process check_type
    if isinstance(check_type, str):
        check_type = check_type.lower()
    
    type_id = los_types.get(check_type)
    if type_id is None:
        if isinstance(check_type, int) and check_type in los_types.values():
            type_id = check_type
        else:
            raise ValueError('CheckLOS: Invalid check_type')

    # Process options
    opts_mask = 0
    if options:
        if isinstance(options, str):
            options = [options]
        
        for opt in options:
            if isinstance(opt, str):
                opt = opt.lower()
                val = los_options.get(opt)
                if val:
                    opts_mask |= val
            elif isinstance(opt, int):
                opts_mask |= opt

    return api.CheckLOS(xf, yf, zf, xt, yt, zt, world_num, type_id, opts_mask)


# Movement helpers
def MoveXYZ(x_dst: int, y_dst: int, z_dst: int, accuracy_xy: int, accuracy_z: int, running: bool) -> bool:
    """
    Move to specified coordinates using pathfinding.
    
    Args:
        x_dst, y_dst, z_dst: Destination coordinates
        accuracy_xy: XY tolerance
        accuracy_z: Z tolerance
        running: True to run, False to walk
        
    Returns:
        True if reached destination, False otherwise
    """
    from .base import Wait, AddToSystemJournal
    from .utils import CalcDir
    from .character import GetSkillValue
    
    # Simple implementation wrapper around NewMoveXYZ logic
    # Note: Full implementation of NewMoveXYZ is complex and depends on many API calls.
    # For now, we can implement a simplified version or port the full logic.
    # Given the complexity, let's start with a basic pathfinding loop using API.
    
    # Check if we are already there
    curr_x, curr_y = api.PredictedX(), api.PredictedY()
    if abs(curr_x - x_dst) <= accuracy_xy and abs(curr_y - y_dst) <= accuracy_xy:
        return True

    # Find path
    path = api.GetPathArray3D(
        curr_x, curr_y, api.PredictedZ(),
        x_dst, y_dst, z_dst,
        api.WorldNum(), accuracy_xy, accuracy_z, running
    )
    
    if not path:
        return False
        
    # Follow path
    for point in path:

        next_x, next_y, next_z = point.X, point.Y, point.Z
        
        # Move step
        direction = CalcDir(api.PredictedX(), api.PredictedY(), next_x, next_y)
        if direction == 100:
            continue
            
        if not api.StepQ(direction, running):
            # Failed to step, maybe resync or retry
            return False
            
        Wait(100 if running else 200)
        
    return True


__all__ = ['MoverSettings', 'Mover', 'CheckLOS', 'MoveXYZ']
