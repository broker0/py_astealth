from datetime import datetime, timedelta
from time import sleep
from typing import Union

from py_astealth.stealth import api
from py_astealth.stealth._internals import _manager
from py_astealth.stealth_enums import Spell, Messenger, Layer


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


# Journal helper functions
def _wait_journal_line_internal(start_time: datetime, text: str, max_wait_ms: int, check_system: bool) -> bool:
    """Internal helper for waiting journal lines."""
    if max_wait_ms:
        stop_time = start_time + timedelta(milliseconds=max_wait_ms)
    else:
        stop_time = datetime.max
    
    while datetime.now() <= stop_time:
        if api.InJournalBetweenTimes(text, start_time, stop_time) >= 0:
            if not check_system or api.GetLineName() == 'System':
                return True
        Wait(10)
    return False


def WaitJournalLine(start_time: datetime, text: str, max_wait_ms: int = 0) -> bool:
    """
    Wait for a journal line containing the specified text.
    
    Args:
        start_time: Starting time for the search window (datetime object)
        text: Text to search for in journal
        max_wait_ms: Maximum wait time in milliseconds (0 = wait indefinitely)
        
    Returns:
        True if text was found, False if timeout
    """
    return _wait_journal_line_internal(start_time, text, max_wait_ms, check_system=False)


def WaitJournalLineSystem(start_time: datetime, text: str, max_wait_ms: int = 0) -> bool:
    """
    Wait for a system journal line containing the specified text.
    
    Args:
        start_time: Starting time for the search window (datetime object)
        text: Text to search for in journal
        max_wait_ms: Maximum wait time in milliseconds (0 = wait indefinitely)
        
    Returns:
        True if system message with text was found, False if timeout
    """
    return _wait_journal_line_internal(start_time, text, max_wait_ms, check_system=True)


# Find and Click helpers
def Ground() -> int:
    """Returns the ground container constant (0)."""
    return 0


def FindType(obj_type: int, container: int = None) -> int:
    """
    Find an object by type in the specified container (simplified version).
    
    Args:
        obj_type: Object type to search for
        container: Container ID to search in (default: Backpack)
        
    Returns:
        Object ID if found, 0 if not found
    """
    if container is None:
        container = api.Backpack()
    return api.FindTypeEx(obj_type, 0xFFFF, container, False)


def FindTypeEx(obj_type: int, color: int, container: int = None, in_sub: bool = True) -> int:
    """
    Find an object by type and color in the specified container.
    
    Args:
        obj_type: Object type to search for
        color: Object color (0xFFFF for any color)
        container: Container ID to search in (default: Backpack)
        in_sub: Search in sub-containers
        
    Returns:
        Object ID if found, 0 if not found
    """
    if container is None:
        container = api.Backpack()
    return api.FindTypeEx(obj_type, color, container, in_sub)


def ClickOnObject(obj_id: int) -> None:
    """
    Click on an object (with existence check).
    
    Args:
        obj_id: Object ID to click on
    """
    if not api.IsObjectExists(obj_id):
        AddToSystemJournal(f'ClickOnObject error: Object {hex(obj_id)} not found.')
    else:
        api.ClickOnObject(obj_id)


# Target helpers
def TargetPresent() -> bool:
    """Check if target cursor is present."""
    return bool(api.TargetID())


def WaitForTarget(max_wait_ms: int) -> bool:
    """
    Wait for target cursor to appear.
    
    Args:
        max_wait_ms: Maximum wait time in milliseconds
        
    Returns:
        True if target appeared, False if timeout
    """
    from time import time
    start_time = time()
    end_time = start_time + max_wait_ms / 1000
    
    while not api.TargetID() and time() < end_time:
        Wait(10)
    
    return time() < end_time


def CancelTarget() -> None:
    """Cancel target cursor and wait until it disappears."""
    api.CancelTarget()
    while api.TargetID():
        Wait(10)


# CatchBag helpers
def SetCatchBag(obj_id: int) -> int:
    """
    Set the catch bag for auto-looting with validation.
    
    Args:
        obj_id: Object ID of the bag (0 to clear)
        
    Returns:
        0 if cleared, 1 if object not found, 2 if set successfully
    """
    if obj_id == 0:
        api.UnsetCatchBag()
        return 0
    elif not api.IsObjectExists(obj_id):
        AddToSystemJournal(f'SetCatchBag Error: Object {hex(obj_id)} not found.')
        return 1
    else:
        api.SetCatchBag(obj_id)
        return 2


def UnsetCatchBag() -> None:
    """Clear the catch bag."""
    api.UnsetCatchBag()


# UseType helpers
def UseType2(obj_type: int) -> int:
    """
    Use an item of the specified type (any color).
    
    Args:
        obj_type: Object type to use
        
    Returns:
        Object ID of used item, or 0 if not found
    """
    return api.UseType(obj_type, 0xFFFF)


# Messenger helpers
def MessengerGetConnected(messenger: Union[str, int, Messenger]) -> bool:
    """
    Check if messenger is connected.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        
    Returns:
        True if connected, False otherwise
    """
    return api.Messenger_GetConnected(_get_messenger_id(messenger))


def MessengerSetConnected(messenger: Union[str, int, Messenger], value: bool) -> None:
    """
    Set messenger connection status.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        value: Connection status
    """
    api.Messenger_SetConnected(_get_messenger_id(messenger), value)


def MessengerGetToken(messenger: Union[str, int, Messenger]) -> str:
    """
    Get messenger token.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        
    Returns:
        Messenger token
    """
    return api.Messenger_GetToken(_get_messenger_id(messenger))


def MessengerSetToken(messenger: Union[str, int, Messenger], token: str) -> None:
    """
    Set messenger token.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        token: Authentication token
    """
    api.Messenger_SetToken(_get_messenger_id(messenger), token)


def MessengerGetName(messenger: Union[str, int, Messenger]) -> str:
    """
    Get messenger name.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        
    Returns:
        Messenger name
    """
    return api.Messenger_GetName(_get_messenger_id(messenger))


def MessengerSendMessage(messenger: Union[str, int, Messenger], msg: str, user_id: str) -> None:
    """
    Send a message via messenger.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        msg: Message text
        user_id: Recipient user ID
    """
    api.Messenger_SendMessage(_get_messenger_id(messenger), msg, user_id)


# Item movement helpers
def MoveItem(item_id: int, count: int, move_into_id: int, x: int, y: int, z: int) -> bool:
    """
    Move an item to a container or location.
    
    Args:
        item_id: Item to move
        count: Amount to move (0 = all)
        move_into_id: Destination container (or 0 for ground)
        x, y, z: Destination coordinates
        
    Returns:
        True if successful, False otherwise
    """
    if not api.DragItem(item_id, count):
        return False
    Wait(100)
    return api.DropItem(move_into_id, x, y, z)


def Grab(item_id: int, count: int) -> bool:
    """
    Move an item to backpack.
    
    Args:
        item_id: Item to grab
        count: Amount to grab (0 = all)
        
    Returns:
        True if successful, False otherwise
    """
    return MoveItem(item_id, count, api.Backpack(), 0, 0, 0)


def Drop(item_id: int, count: int, x: int, y: int, z: int) -> bool:
    """
    Drop an item on the ground at specified coordinates.
    
    Args:
        item_id: Item to drop
        count: Amount to drop (0 = all)
        x, y, z: Ground coordinates
        
    Returns:
        True if successful, False otherwise
    """
    return MoveItem(item_id, count, Ground(), x, y, z)


def DropHere(item_id: int) -> bool:
    """
    Drop an item on the ground at current position.
    
    Args:
        item_id: Item to drop
        
    Returns:
        True if successful, False otherwise
    """
    return MoveItem(item_id, 0, Ground(), 0, 0, 0)


def MoveItems(container: int, items_type: int, items_color: int, 
              move_into_id: int, x: int, y: int, z: int,
              delay_ms: int, max_count: int = 0) -> bool:
    """
    Move multiple items of specified type from container.
    
    Args:
        container: Source container
        items_type: Item type to move (-1 = all types)
        items_color: Item color (-1 = all colors)
        move_into_id: Destination container
        x, y, z: Destination coordinates
        delay_ms: Delay between moves in milliseconds
        max_count: Maximum items to move (0 = all found items)
        
    Returns:
        True if any items were moved, False otherwise
    """
    FindTypeEx(items_type, items_color, container, False)
    items = api.GetFindedList()
    if not items:  # nothing found
        return False
    
    drop_delay = api.GetDropDelay()
    if not 50 <= drop_delay <= 10000:
        drop_delay = 50 if drop_delay < 50 else 10000
    if drop_delay > delay_ms:
        delay_ms = 0
    api.SetDropDelay(drop_delay)
    
    if not 0 < max_count < len(items):
        max_count = len(items)
    
    for i in range(max_count):
        MoveItem(items[i], 0, move_into_id, x, y, z)
        Wait(delay_ms)
    return True


def EmptyContainer(container: int, dest_container: int, delay_ms: int) -> bool:
    """
    Move all items from one container to another.
    
    Args:
        container: Source container
        dest_container: Destination container
        delay_ms: Delay between moves in milliseconds
        
    Returns:
        True if any items were moved, False otherwise
    """
    return MoveItems(container, -1, -1, dest_container, 0xFFFF, 0xFFFF, 0, delay_ms)


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
    'Cast', 'CastToObj', 'CastToObject', 'IsActiveSpellAbility',
    # Journal helpers
    'WaitJournalLine', 'WaitJournalLineSystem',
    # Find and Click helpers
    'Ground', 'FindType', 'FindTypeEx', 'ClickOnObject',
    # Target helpers
    'TargetPresent', 'WaitForTarget', 'CancelTarget',
    # CatchBag helpers
    'SetCatchBag', 'UnsetCatchBag',
    # UseType helpers
    'UseType2',
    # Messenger helpers
    'MessengerGetConnected', 'MessengerSetConnected', 'MessengerGetToken',
    'MessengerSetToken', 'MessengerGetName', 'MessengerSendMessage',
    # Item movement helpers
    'MoveItem', 'Grab', 'Drop', 'DropHere', 'MoveItems', 'EmptyContainer'
]
