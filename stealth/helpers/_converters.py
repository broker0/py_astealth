"""Internal converter functions for type-safe parameter handling."""
from typing import Union

from py_astealth.stealth import api
from py_astealth.stealth_enums import Spell, Messenger


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
