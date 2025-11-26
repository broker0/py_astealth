"""Character-related helpers: skills and spells."""
from typing import Union

from py_astealth.stealth import api
from py_astealth.stealth_enums import Spell

from ._converters import _get_skill_id, _get_spell_id
from .common import Wait


# Skill helpers
def UseSkill(skill_name: str) -> None:
    """Use a skill by name."""
    api.UseSkill(_get_skill_id(skill_name))


def GetSkillValue(skill_name: str) -> float:
    """Get the base skill value by name."""
    return api.GetSkillValue(_get_skill_id(skill_name))


def GetSkillCurrentValue(skill_name: str) -> float:
    """Get the current skill value by name (with bonuses)."""
    return api.GetSkillCurrentValue(_get_skill_id(skill_name))


def GetSkillCap(skill_name: str) -> float:
    """Get the skill cap by name."""
    return api.GetSkillCap(_get_skill_id(skill_name))


def SetSkillLockState(skill_name: str, state: int) -> None:
    """Set the skill lock state by name."""
    api.SetSkillLockState(_get_skill_id(skill_name), state)


def GetSkillLockState(skill_name: str) -> int:
    """Get the skill lock state by name."""
    return api.GetSkillLockState(_get_skill_id(skill_name))


def ChangeSkillLockState(skill_name: str, state: int) -> None:
    """Alias for SetSkillLockState."""
    SetSkillLockState(skill_name, state)


# Stat helpers
def GetHP(obj_id: int) -> int:
    """Get HP of object, requesting stats if necessary."""
    result = api.GetHP(obj_id)
    if not result and api.IsObjectExists(obj_id) and api.IsNPC(obj_id):
        api.RequestStats(obj_id)
        Wait(100)
        result = api.GetHP(obj_id)
    return result


def GetMana(obj_id: int) -> int:
    """Get Mana of object, requesting stats if necessary."""
    result = api.GetMana(obj_id)
    if not result and api.IsObjectExists(obj_id) and api.IsNPC(obj_id):
        api.RequestStats(obj_id)
        Wait(100)
        result = api.GetMana(obj_id)
    return result


def GetStam(obj_id: int) -> int:
    """Get Stamina of object, requesting stats if necessary."""
    result = api.GetStam(obj_id)
    if not result and api.IsObjectExists(obj_id) and api.IsNPC(obj_id):
        api.RequestStats(obj_id)
        Wait(100)
        result = api.GetStam(obj_id)
    return result


def Str():
    return api.GetSelfStr()


def Int():
    return api.GetSelfInt()


def Dex():
    return api.GetSelfDex()


def Life():
    return api.GetSelfLife()


def HP():
    Life()


def Mana():
    return api.GetSelfMana()


def Stam():
    return api.GetSelfStam()


def MaxLife():
    return api.GetSelfMaxLife()


def MaxHP():
    return MaxLife()


def MaxMana():
    return api.GetSelfMaxMana()


def MaxStam():
    return api.GetSelfMaxStam()


def Luck():
    return api.GetSelfLuck()


# Spell helpers
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


def WarMode() -> bool:
    """Check if self is in war mode."""
    return api.IsWarMode(api.Self())


__all__ = [
    'UseSkill', 'GetSkillValue', 'GetSkillCurrentValue', 'GetSkillCap',
    'UseSkill', 'GetSkillValue', 'GetSkillCurrentValue', 'GetSkillCap',
    'SetSkillLockState', 'GetSkillLockState', 'ChangeSkillLockState',
    'GetHP', 'GetMana', 'GetStam',
    'Str', 'Int', 'Dex', 'Life', 'HP', 'Mana', 'Stam',
    'MaxLife', 'MaxHP', 'MaxMana', 'MaxStam',
    'Luck',
    'Cast', 'CastToObj', 'CastToObject', 'IsActiveSpellAbility',
    'WarMode',
]
