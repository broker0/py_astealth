"""Internal converter functions for type-safe parameter handling."""
from typing import Union, Type, TypeVar
from enum import Enum

from py_astealth.stealth import api
from py_astealth.stealth_enums import Spell, Messenger, Global, EventType, Virtue


T = TypeVar("T", bound=Enum)


def _get_enum_value(value: Union[str, int, T], enum_class: Type[T], item_name: str) -> int:
    """
    Generic converter for Enum variants.
    """
    if isinstance(value, int):
        return value
    elif isinstance(value, enum_class):
        return value.value
    elif isinstance(value, str):
        # Normalize: lowercase, remove spaces and underscores
        normalized = value.lower().replace(" ", "").replace("_", "")
        # Try to find matching Enum member
        for member in enum_class:
            if member.name.lower() == normalized:
                return member.value
        raise ValueError(f'Unknown {item_name} name: "{value}"')
    else:
        raise TypeError(f"Invalid {item_name} type: {type(value)}. Expected str, int, or {enum_class.__name__} enum")


def _get_spell_id(spell: Union[str, int, Spell]) -> int:
    """
    Convert spell to spell ID.
    Accepts:
    - str: spell name (case-insensitive, spaces/underscores ignored)
    - int: spell ID directly
    - Spell: enum member
    Returns: int spell ID
    """
    return _get_enum_value(spell, Spell, "spell")


def _get_virtue_id(virtue: Union[str, int, Virtue]) -> int:
    """
    Convert virtue to virtue ID.
    Accepts:
    - str: virtue name (case-insensitive, spaces/underscores ignored)
    - int: virtue ID directly
    - Virtue: enum member
    Returns: int virtue ID
    """
    return _get_enum_value(virtue, Virtue, "virtue")


def _get_messenger_id(messenger: Union[str, int, Messenger]) -> int:
    """
    Convert messenger to messenger ID.
    Accepts:
    - str: messenger name (case-insensitive: 'Telegram', 'Viber', 'Discord')
    - int: messenger ID directly (1, 2, 3) or 0 for default (Telegram)
    - Messenger: enum member
    Returns: int messenger ID
    """
    if isinstance(messenger, int) and messenger == 0:
        return 1
    return _get_enum_value(messenger, Messenger, "messenger")


def _get_global_region_id(region: Union[str, int, Global]) -> int:
    """
    Convert global region to region ID.
    Accepts:
    - str: region name (case-insensitive: 'Stealth', 'Char')
    - int: region ID directly (0, 1)
    - GlobalRegion: enum member
    Returns: int region ID
    """
    return _get_enum_value(region, Global, "global region")


def _get_event_type_id(event_type: Union[str, int, EventType]) -> int:
    """
    Convert global region to region ID.
    Accepts:
    - str: region name (case-insensitive: 'Stealth', 'Char')
    - int: region ID directly (0, 1)
    - GlobalRegion: enum member
    Returns: int region ID
    """
    return _get_enum_value(event_type, EventType, "event type")


def _get_skill_id(skill_id: Union[str, int]) -> int:
    """Convert skill name to skill ID, raises ValueError if invalid."""
    if isinstance(skill_id, int):
        return skill_id
    else:
        skill_id = api.GetSkillID(skill_id)

    if skill_id < 0:
        raise ValueError(f'Unknown skill name: "{skill_id}"')

    return skill_id