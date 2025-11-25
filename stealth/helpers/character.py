"""Character-related helpers: skills and spells."""
from typing import Union

from py_astealth.stealth import api
from py_astealth.stealth_enums import Spell
from ._converters import _get_skill_id, _get_spell_id


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


__all__ = [
    'UseSkill', 'GetSkillValue', 'GetSkillCurrentValue', 'GetSkillCap',
    'SetSkillLockState', 'GetSkillLockState',
    'Cast', 'CastToObj', 'CastToObject', 'IsActiveSpellAbility',
]
