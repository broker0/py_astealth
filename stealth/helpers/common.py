"""Base helper functions for events, logging, and layer constants."""
from datetime import datetime, timedelta
from time import sleep

from py_astealth.stealth import api
from py_astealth.stealth._internals import _manager
from py_astealth.stealth.helpers._converters import _get_global_region_id


def AddToSystemJournal(*args, **kwargs):
    """Format and add message to system journal."""
    sep = kwargs.pop('sep', ', ')
    end = kwargs.pop('end', '')
    s_args = sep.join((str(arg) for arg in args))
    s_kwargs = sep.join((str(k) + '=' + str(v) for k, v in kwargs.items()))
    text = s_args + (sep if s_args and s_kwargs else '') + s_kwargs + end
    api.AddToSystemJournal(text)


def GetFoundList() -> list[int]:
    return api.GetFindedList()


def GetEvent(event_type: int, delay: int):
    """Get event from client."""
    return _manager.get_event(event_type, delay)


def SetEventProc(event_name: str, handler):
    """Set event processor for specified event."""
    return _manager.set_event_proc(event_name, handler)


def WaitForEvent(delay: int):
    """Wait for any event."""
    return _manager.wait_for_event(delay)


def Wait(delay_ms: int):
    """Sleep for specified milliseconds."""
    if delay_ms > 0:
        sleep(delay_ms / 1000)
    else:
        event = WaitForEvent(delay_ms)


# Global variables
def SetGlobal(region, var_name: str, var_value: str) -> None:
    """
    Set a global variable in specified region.
    
    Args:
        region: Region ('Stealth'/'Char', 0/1, or GlobalRegion enum)
        var_name: Variable name
        var_value: Variable value
    """
    api.SetGlobal(_get_global_region_id(region), var_name, var_value)


def GetGlobal(region, var_name: str) -> str:
    """
    Get a global variable from specified region.
    
    Args:
        region: Region ('Stealth'/'Char', 0/1, or GlobalRegion enum)
        var_name: Variable name
        
    Returns:
        Variable value
    """
    return api.GetGlobal(_get_global_region_id(region), var_name)


def CheckLag(timeout_ms=10000):
    stop_time = datetime.now() + timedelta(milliseconds=timeout_ms)

    api.CheckLagBegin()
    while datetime.now() <= stop_time:
        if api.IsCheckLagEnd():
            return True

        Wait(1)

    api.CheckLagEnd()
    return False


def IsGump() -> bool:
    """Check if any gump is present."""
    return api.GetGumpsCount() > 0


__all__ = [
    'AddToSystemJournal',
    'GetFoundList',
    'GetEvent',
    'SetEventProc',
    'WaitForEvent',
    'Wait',
    'SetGlobal', 'GetGlobal',
    'CheckLag',
    'IsGump'
]
