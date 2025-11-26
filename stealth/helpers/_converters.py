"""Internal converter functions for type-safe parameter handling."""
from typing import Union

from py_astealth.stealth import api
from py_astealth.stealth_enums import Spell, Messenger, Global, EventType


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


def _get_messenger_id(messenger: Union[str, int, Messenger]) -> int:
    """
    Convert messenger to messenger ID.
    Accepts:
    - str: messenger name (case-insensitive: 'Telegram', 'Viber', 'Discord')
    - int: messenger ID directly (1, 2, 3) or 0 for default (Telegram)
    - Messenger: enum member
    Returns: int messenger ID
    """
    if isinstance(messenger, int):
        # 0 means default (Telegram)
        return 1 if messenger == 0 else messenger
    elif isinstance(messenger, Messenger):
        return messenger.value
    elif isinstance(messenger, str):
        # Normalize: lowercase
        normalized = messenger.lower()
        # Try to find matching Messenger enum member
        for mes_enum in Messenger:
            if mes_enum.name.lower() == normalized:
                return mes_enum.value
        raise ValueError(f'Unknown messenger name: "{messenger}". Must be "Telegram", "Viber", or "Discord"')
    else:
        raise TypeError(f'Invalid messenger type: {type(messenger)}. Expected str, int, or Messenger enum')


def _get_global_region_id(region: Union[str, int, Global]) -> int:
    """
    Convert global region to region ID.
    Accepts:
    - str: region name (case-insensitive: 'Stealth', 'Char')
    - int: region ID directly (0, 1)
    - GlobalRegion: enum member
    Returns: int region ID
    """

    if isinstance(region, int):
        return region
    elif isinstance(region, Global):
        return region.value
    elif isinstance(region, str):
        # Normalize: lowercase
        normalized = region.lower()
        # Try to find matching Global enum member
        for reg_enum in Global:
            if reg_enum.name.lower() == normalized:
                return reg_enum.value
        raise ValueError(f'Unknown global region: "{region}". Must be "Stealth" or "Char"')
    else:
        raise TypeError(f'Invalid global region type: {type(region)}. Expected str, int, or GlobalRegion enum')


def _get_event_type_id(event_type: Union[str, int, EventType]) -> int:
    """
    Convert global region to region ID.
    Accepts:
    - str: region name (case-insensitive: 'Stealth', 'Char')
    - int: region ID directly (0, 1)
    - GlobalRegion: enum member
    Returns: int region ID
    """

    if isinstance(event_type, int):
        return event_type
    elif isinstance(event_type, EventType):
        return event_type.value
    elif isinstance(event_type, str):
        # Normalize: lowercase
        normalized = event_type.lower()
        # Try to find matching Global enum member
        for reg_enum in EventType:
            if reg_enum.name.lower() == normalized:
                return reg_enum.value
        raise ValueError(f'Unknown event name: "{event_type}"')
    else:
        raise TypeError(f'Invalid event type: {type(event_type)}. Expected str, int, or EventType enum')
