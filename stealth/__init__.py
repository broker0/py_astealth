# import all methods from generated interface file to help the IDE
from datetime import timedelta
from time import sleep

from py_astealth.generated.sync_module import *

from ._internals import _create_global_proxy, _manager
from py_astealth.stealth_api import StealthApi


__all__ = []


def _populate_module():
    """
    Dynamically creates and adds all API functions to this module.
    """
    current_module = globals()
    specs = StealthApi.get_methods()

    for spec in specs:
        proxy_function = _create_global_proxy(spec)
        current_module[spec.name] = proxy_function
        __all__.append(spec.name)


_populate_module()


def RhandLayer():
    return 0x01


def LhandLayer():
    return 0x02


def ShoesLayer():
    return 0x03


def PantsLayer():
    return 0x04


def ShirtLayer():
    return 0x05


def HatLayer():
    return 0x06


def GlovesLayer():
    return 0x07


def RingLayer():
    return 0x08


def TalismanLayer():
    return 0x09


def NeckLayer():
    return 0x0A


def HairLayer():
    return 0x0B


def WaistLayer():
    return 0x0C


def TorsoLayer():
    return 0x0D


def BraceLayer():
    return 0x0E


def BeardLayer():
    return 0x10


def TorsoHLayer():
    return 0x11


def EarLayer():
    return 0x12


def ArmsLayer():
    return 0x13


def CloakLayer():
    return 0x14


def BpackLayer():
    return 0x15


def RobeLayer():
    return 0x16


def EggsLayer():
    return 0x17


def LegsLayer():
    return 0x18


def HorseLayer():
    return 0x19


def RstkLayer():
    return 0x1A


def NRstkLayer():
    return 0x1B


def SellLayer():
    return 0x1C


def BankLayer():
    return 0x1D


def GetEvent():
    return _manager.get_event_for_thread()


def SetEventProc(event_type, handler):
    if handler:
        SetEventCallback(event_type)
    else:
        ClearEventCallback(event_type)

    _manager.set_handler_for_thread(event_type, handler)


def WaitForEvent(max_wait):
    """
    Waits for an event within the specified time (max_wait), specified in milliseconds.
    If an event occurs, its handler is called, if one exists, and the function returns the event.
    If the event is not received within the max_wait time, None is returned.
    if max_wait==0 | None - wait forever
    """
    end_time = datetime.now() + timedelta(milliseconds=max_wait) if max_wait else datetime.max
    while datetime.now() < end_time:
        event = GetEvent()
        if event:
            handler = _manager.get_handler_for_thread(event.id)
            if handler:
                handler(*event.arguments)

            return event

        sleep(1/1000)

    return None


def Wait(delay):
    """
    Pauses for `delay` milliseconds
    Internally calls WaitForEvent, which allows event handlers to be called
    but the function itself does not return any events
    """
    end_time = datetime.now() + timedelta(milliseconds=delay)
    while datetime.now() < end_time:
        delay = (end_time - datetime.now()).total_seconds()*1000.0
        event = WaitForEvent(delay)
