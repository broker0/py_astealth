"""Base helper functions for events, logging, and layer constants."""
from datetime import datetime, timedelta
from time import sleep

from py_astealth.stealth import api
from py_astealth.stealth._internals import _manager
from py_astealth.stealth_enums import Layer


def AddToSystemJournal(*args, **kwargs):
    """Format and add message to system journal."""
    sep = kwargs.pop('sep', ', ')
    end = kwargs.pop('end', '')
    s_args = sep.join((str(arg) for arg in args))
    s_kwargs = sep.join((str(k) + '=' + str(v) for k, v in kwargs.items()))
    text = s_args + (sep if s_args and s_kwargs else '') + s_kwargs + end
    api.AddToSystemJournal(text)


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
    'RstkLayer', 'NRstkLayer', 'SellLayer', 'BankLayer',
]
