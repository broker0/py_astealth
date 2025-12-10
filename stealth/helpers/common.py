"""Base helper functions for events, logging, and layer constants."""
import threading
import dataclasses
from collections import deque
from dataclasses import asdict
from datetime import datetime, timedelta
from time import sleep

from py_astealth.stealth_structs import GumpInfo
from py_astealth.stealth import api
from py_astealth.stealth._internals import _manager

from ._converters import _get_global_region_id, _get_event_type_id


def AddToSystemJournal(*args, **kwargs):
    """Format and add message to system journal."""
    sep = kwargs.pop('sep', ', ')
    end = kwargs.pop('end', '')
    s_args = sep.join((str(arg) for arg in args))
    s_kwargs = sep.join((str(k) + '=' + str(v) for k, v in kwargs.items()))
    text = s_args + (sep if s_args and s_kwargs else '') + s_kwargs + end
    api.AddToSystemJournal(text)


# Event related
class ThreadContext(threading.local):
    """
    A data store unique to each thread.
    __init__ will be called the first time it is accessed in a new thread.
    """
    def __init__(self):
        super().__init__()
        self.event_buffer = deque()


_context = ThreadContext()


def GetEvent():
    return _manager.get_event_for_thread()


def SetEventProc(event_type, handler):
    event_type = _get_event_type_id(event_type)
    _manager.set_handler_for_thread(event_type, handler)

    if handler:
        api.SetEventCallback(event_type)
    else:
        api.ClearEventCallback(event_type)


def WaitForEvent(delay_ms: int = 0):
    """
    Waits for an event within the specified time (max_wait), specified in milliseconds.
    If an event occurs, its handler is called, if one exists, and the function returns the event.
    If the event is not received within the max_wait time, None is returned.
    if max_wait==0 | None - wait forever
    """
    end_time = datetime.now() + timedelta(milliseconds=delay_ms) if delay_ms else datetime.max

    while datetime.now() < end_time:
        if _context.event_buffer:
            return _context.event_buffer.popleft()

        event = _manager.get_event_for_thread()
        if event:
            handler = _manager.get_handler_for_thread(event.id)
            if handler:
                handler(*event.arguments)
                return event
            else:
                return event

        sleep(1/1000)

    return None


def Wait(delay_ms: int):
    """Sleep for specified milliseconds."""
    end_time = datetime.now() + timedelta(milliseconds=delay_ms)

    while datetime.now() <= end_time:
        event = _manager.get_event_for_thread()

        if event:
            handler = _manager.get_handler_for_thread(event.id)

            if handler:
                handler(*event.arguments)
            else:
                _context.event_buffer.append(event)

        sleep(1/1000)


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


def GetGump(gump_index: int) -> GumpInfo:
    """Returns a structured gump object"""
    return api.GetGumpInfo(gump_index)


def GetGumpInfo(GumpIndex: int) -> dict:
    """Deprecated: use GetGump instead"""
    info_obj = GetGump(GumpIndex)
    if not info_obj:
        return {}

    result = asdict(info_obj.gump)

    for field in dataclasses.fields(info_obj):
        if field.name == 'gump':
            continue

        field_value = getattr(info_obj, field.name)
        if not field_value:
            result[field.name] = []
            continue

        if field.name == 'Text':
            result['Text'] = [[item.Text] for item in field_value]
            continue

        processed_list = []
        for item in field_value:
            element_dict = asdict(item)

            if 'ClilocID' in element_dict and 'Arguments' in element_dict:
                _apply_cliloc_logic(element_dict)

            processed_list.append(element_dict)

        result[field.name] = processed_list

    result['ChekerTrans'] = result['CheckerTrans']

    return result


def _apply_cliloc_logic(element: dict):
    text = api.GetClilocByID(element['ClilocID'])
    raw_args = element.get('Arguments', '')

    args_list = raw_args.split('@')[1:] if raw_args else []

    for arg in args_list:
        if '~' in text and arg:
            if arg.startswith('#'):
                try:
                    arg_id = int(arg.strip('#'))
                    arg = GetClilocByID(arg_id)
                except ValueError:
                    pass

            try:
                s = text.index('~')
                e = text.index('~', s + 1)
                to_replace = text[s: e + 1]
                text = text.replace(to_replace, arg, 1)
            except ValueError:
                pass

    element['ClilocText'] = text


def GetClilocByID(cliloc_id, params: list[str] = None):
    """Deprecated: emulate old behavior, use GetCliloc instead"""
    if params is None:
        params = []

    return api.GetClilocByID(cliloc_id, params)


__all__ = [
    'AddToSystemJournal',
    'GetEvent',
    'SetEventProc',
    'WaitForEvent',
    'Wait',
    'SetGlobal', 'GetGlobal',
    'CheckLag',
    'IsGump', 'GetGump', 'GetGumpInfo',
    'GetClilocByID',
]
