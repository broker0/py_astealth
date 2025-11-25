"""Targeting and catch bag helpers."""
from py_astealth.stealth import api
from .base import Wait, AddToSystemJournal


# Target helpers
def TargetPresent() -> bool:
    """Check if target cursor is present."""
    return bool(api.TargetID())


def WaitForTarget(max_wait_ms: int) -> bool:
    """
    Wait for target cursor to appear.
    
    Args:
        max_wait_ms: Maximum wait time in milliseconds
        
    Returns:
        True if target appeared, False if timeout
    """
    from time import time
    start_time = time()
    end_time = start_time + max_wait_ms / 1000
    
    while not api.TargetID() and time() < end_time:
        Wait(10)
    
    return time() < end_time


def CancelTarget() -> None:
    """Cancel target cursor and wait until it disappears."""
    api.CancelTarget()
    while api.TargetID():
        Wait(10)


# CatchBag helpers
def SetCatchBag(obj_id: int) -> int:
    """
    Set the catch bag for auto-looting with validation.
    
    Args:
        obj_id: Object ID of the bag (0 to clear)
        
    Returns:
        0 if cleared, 1 if object not found, 2 if set successfully
    """
    if obj_id == 0:
        api.UnsetCatchBag()
        return 0
    elif not api.IsObjectExists(obj_id):
        AddToSystemJournal(f'SetCatchBag Error: Object {hex(obj_id)} not found.')
        return 1
    else:
        api.SetCatchBag(obj_id)
        return 2


def UnsetCatchBag() -> None:
    """Clear the catch bag."""
    api.UnsetCatchBag()


# UseType helpers
def UseType2(obj_type: int) -> int:
    """
    Use an item of the specified type (any color).
    
    Args:
        obj_type: Object type to use
        
    Returns:
        Object ID of used item, or 0 if not found
    """
    return api.UseType(obj_type, 0xFFFF)


__all__ = [
    'TargetPresent', 'WaitForTarget', 'CancelTarget',
    'SetCatchBag', 'UnsetCatchBag',
    'UseType2',
]
