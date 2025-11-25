from datetime import datetime, timedelta
from time import sleep

from py_astealth.stealth_api import StealthApi
from ._internals import _manager, _create_global_proxy

# Create internal proxies for API methods used by helpers
_AddToSystemJournal = _create_global_proxy(StealthApi.AddToSystemJournal.method_spec)
_SetEventCallback = _create_global_proxy(StealthApi.SetEventCallback.method_spec)
_ClearEventCallback = _create_global_proxy(StealthApi.ClearEventCallback.method_spec)


def AddToSystemJournal(*args, **kwargs):
    sep = kwargs.pop('sep', ', ')
    end = kwargs.pop('end', '')
    s_args = sep.join((str(arg) for arg in args))
    s_kwargs = sep.join((str(k) + '=' + str(v) for k, v in kwargs.items()))
    text = s_args + (sep if s_args and s_kwargs else '') + s_kwargs + end
    _AddToSystemJournal(text)


def GetEvent():
    return _manager.get_event_for_thread()


def SetEventProc(event_type, handler):
    if handler:
        _SetEventCallback(event_type)
    else:
        _ClearEventCallback(event_type)

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


from py_astealth.stealth_enums import Layer

# Layer constants/functions
def RhandLayer(): return Layer.RhandLayer
def LhandLayer(): return Layer.LhandLayer
def ShoesLayer(): return Layer.ShoesLayer
def PantsLayer(): return Layer.PantsLayer
def ShirtLayer(): return Layer.ShirtLayer
def HatLayer(): return Layer.HatLayer
def GlovesLayer(): return Layer.GlovesLayer
def RingLayer(): return Layer.RingLayer
def TalismanLayer(): return Layer.TalismanLayer
def NeckLayer(): return Layer.NeckLayer
def HairLayer(): return Layer.HairLayer
def WaistLayer(): return Layer.WaistLayer
def TorsoLayer(): return Layer.TorsoLayer
def BraceLayer(): return Layer.BraceLayer
def BeardLayer(): return Layer.BeardLayer
def TorsoHLayer(): return Layer.TorsoHLayer
def EarLayer(): return Layer.EarLayer
def ArmsLayer(): return Layer.ArmsLayer
def CloakLayer(): return Layer.CloakLayer
def BpackLayer(): return Layer.BpackLayer
def RobeLayer(): return Layer.RobeLayer
def EggsLayer(): return Layer.EggsLayer
def LegsLayer(): return Layer.LegsLayer
def HorseLayer(): return Layer.HorseLayer
def RstkLayer(): return Layer.RstkLayer
def NRstkLayer(): return Layer.NRstkLayer
def SellLayer(): return Layer.SellLayer
def BankLayer(): return Layer.BankLayer

__all__ = [
    'AddToSystemJournal',
    'GetEvent',
    'SetEventProc',
    'WaitForEvent',
    'Wait',
    'RhandLayer', 'LhandLayer', 'ShoesLayer', 'PantsLayer', 'ShirtLayer', 'HatLayer',
    'GlovesLayer', 'RingLayer', 'TalismanLayer', 'NeckLayer', 'HairLayer', 'WaistLayer',
    'TorsoLayer', 'BraceLayer', 'BeardLayer', 'TorsoHLayer', 'EarLayer', 'ArmsLayer',
    'CloakLayer', 'BpackLayer', 'RobeLayer', 'EggsLayer', 'LegsLayer', 'HorseLayer',
    'RstkLayer', 'NRstkLayer', 'SellLayer', 'BankLayer'
]
