from datetime import datetime, timedelta
from time import sleep
from typing import Union

from . import api
from ._internals import _manager
from py_astealth.stealth_enums import Spell


def _get_skill_id(skill_name: str) -> int:
    """Convert skill name to skill ID, raises ValueError if invalid."""
    skill_id = api.GetSkillID(skill_name)
    if skill_id < 0:
        raise ValueError(f'Unknown skill name: "{skill_name}"')
    return skill_id


def _get_spell_id(spell: Union[str, int, Spell]) -> int:
    """
    Convert spell to spell ID.
    Accepts:
    - str: spell name (case-insensitive, spaces/underscores ignored)
    - int: spell ID directly
    - Spell: enum member
    Returns: int spell ID
    """
    if isinstance(spell, int):
        return spell
    elif isinstance(spell, Spell):
        return spell.value
    elif isinstance(spell, str):
        # Normalize: lowercase, remove spaces and underscores
        normalized = spell.lower().replace(' ', '').replace('_', '')
        # Try to find matching Spell enum member
        for spell_enum in Spell:
            enum_normalized = spell_enum.name.lower()
            if enum_normalized == normalized:
                return spell_enum.value
        raise ValueError(f'Unknown spell name: "{spell}"')
    else:
        raise TypeError(f'Invalid spell type: {type(spell)}. Expected str, int, or Spell enum')


def AddToSystemJournal(*args, **kwargs):
    sep = kwargs.pop('sep', ', ')
    end = kwargs.pop('end', '')
    s_args = sep.join((str(arg) for arg in args))
    s_kwargs = sep.join((str(k) + '=' + str(v) for k, v in kwargs.items()))
    text = s_args + (sep if s_args and s_kwargs else '') + s_kwargs + end
    api.AddToSystemJournal(text)


def GetEvent():
    return _manager.get_event_for_thread()


def SetEventProc(event_type, handler):
    if handler:
        api.SetEventCallback(event_type)
    else:
        api.ClearEventCallback(event_type)

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


# Skill helper functions
def UseSkill(skill_name: str) -> bool:
    """Use a skill by name. Example: UseSkill('Animal Lore')"""
    api.UseSkill(_get_skill_id(skill_name))
    return True


def GetSkillValue(skill_name: str) -> float:
    """Get the skill value by name."""
    return api.GetSkillValue(_get_skill_id(skill_name))


def GetSkillCurrentValue(skill_name: str) -> float:
    """Get the current skill value by name."""
    return api.GetSkillCurrentValue(_get_skill_id(skill_name))


def GetSkillCap(skill_name: str) -> float:
    """Get the skill cap by name."""
    return api.GetSkillCap(_get_skill_id(skill_name))


def SetSkillLockState(skill_name: str, state: int) -> None:
    """Set the skill lock state by name. State: 0=up, 1=down, 2=locked"""
    api.SetSkillLockState(_get_skill_id(skill_name), state)


def GetSkillLockState(skill_name: str) -> int:
    """Get the skill lock state by name."""
    return api.GetSkillLockState(_get_skill_id(skill_name))


# Spell helper functions
def Cast(spell: Union[str, int, Spell]) -> bool:
    """
    Cast a spell.
    
    Args:
        spell: Spell name (str), ID (int), or Spell enum member
        
    Examples:
        Cast("Magic Arrow")  # old style
        Cast(Spell.MagicArrow)  # new style with enum
        Cast(5)  # direct ID
    """
    api.Cast(_get_spell_id(spell))
    return True


def CastToObj(spell: Union[str, int, Spell], obj_id: int) -> None:
    """
    Cast a spell on a target object.
    
    Args:
        spell: Spell name (str), ID (int), or Spell enum member
        obj_id: Target object ID
    """
    api.WaitTargetObject(obj_id)
    api.Cast(_get_spell_id(spell))


# Alias for CastToObj
def CastToObject(spell: Union[str, int, Spell], obj_id: int) -> None:
    """Alias for CastToObj."""
    CastToObj(spell, obj_id)


def IsActiveSpellAbility(spell: Union[str, int, Spell]) -> bool:
    """
    Check if a spell or ability is currently active.
    
    Args:
        spell: Spell name (str), ID (int), or Spell enum member
        
    Returns:
        True if the spell/ability is active, False otherwise
    """
    return api.IsActiveSpellAbility(_get_spell_id(spell))


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
    # Skill helpers
    'UseSkill', 'GetSkillValue', 'GetSkillCurrentValue', 'GetSkillCap',
    'SetSkillLockState', 'GetSkillLockState',
    # Spell helpers
    'Cast', 'CastToObj', 'CastToObject', 'IsActiveSpellAbility'
]
