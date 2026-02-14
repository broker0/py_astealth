"""Item-related helpers: finding, clicking, and moving items."""
from py_astealth.stealth import api
from py_astealth.stealth_enums import Reagent

from .common import Wait, AddToSystemJournal


class FinderSettings:
    """
    Helper class for managing Find-related settings similar to MoverSettings.
    
    Usage:
        # Set settings
        FinderSettings.FindDistance = 20
        FinderSettings.FindInNulPoint = True
        print(Finder.FindVertical)
    """
    
    @property
    def FindDistance(self) -> int:
        """Get current find distance."""
        return api.GetFindDistance()
    
    @FindDistance.setter
    def FindDistance(self, value: int) -> None:
        """Set find distance."""
        api.SetFindDistance(value)

    @property
    def FindVertical(self) -> int:
        """Get current find vertical distance."""
        return api.GetFindVertical()

    @FindVertical.setter
    def FindVertical(self, value: int) -> None:
        """Set find vertical distance."""
        api.SetFindVertical(value)
    
    @property
    def FindInNulPoint(self) -> bool:
        """Get whether to search at null point (0, 0, 0)."""
        return api.GetFindInNulPoint()
    
    @FindInNulPoint.setter
    def FindInNulPoint(self, value: bool) -> None:
        """Set whether to search at null point (0, 0, 0)."""
        api.SetFindInNulPoint(value)


# Create a singleton instance
Finder = FinderSettings()


# Find and Click helpers
def GetFoundList() -> list[int]:
    return api.GetFindedList()


def Ground() -> int:
    """Returns the ground container constant (0)."""
    return 0


def FindType(obj_type: int, container: int = None) -> int:
    """
    Find an object by type in the specified container (simplified version).
    
    Args:
        obj_type: Object type to search for (0xFFFF for any type)
        container: Container ID to search in (default: Backpack)
        
    Returns:
        Object ID if found, 0 if not found
    """
    if obj_type == -1:
        obj_type = 0xFFFF

    if container is None:
        container = api.Backpack()
    return api.FindTypeEx(obj_type, 0xFFFF, container, False)


def FindTypeEx(obj_type: int, color: int, container: int = None, in_sub: bool = True) -> int:
    """
    Find an object by type and color in the specified container.
    
    Args:
        obj_type: Object type to search for (0xFFFF for any type)
        color: Object color (0xFFFF for any color)
        container: Container ID to search in (default: Backpack)
        in_sub: Search in sub-containers
        
    Returns:
        Object ID if found, 0 if not found
    """
    if obj_type == -1:
        obj_type = 0xFFFF

    if color == -1:
        color = 0xFFFF

    if container is None:
        container = api.Backpack()
        
    return api.FindTypeEx(obj_type, color, container, in_sub)


def FindTypesArrayEx(obj_types: list[int], colors: list[int], containers: list[int], in_sub: bool) -> int:
    """
    Find an object by types and colors in the specified container.

    Args:
        obj_types: List of object types to search for (0xFFFF for any type)
        colors: List of object colors (0xFFFF for any color)
        containers: List of container ID to search
        in_sub: Search in sub-containers

    Returns:
        Object ID if found, 0 if not found
    """
    obj_types = [obj_type if obj_type != -1 else 0xFFFF for obj_type in obj_types]
    colors = [color if color != -1 else 0xFFFF for color in colors]

    return api.FindTypesArrayEx(obj_types, colors, containers, in_sub)


def FindNotoriety(obj_type: int, notoriety: int) -> int:
    """
    Find a mobile (npc) by type and notoriety.

    Args:
        obj_type: Object type to search for (0xFFFF for any type)
        notoriety: 1 - innocent (blue)
                   2 - guilded/ally (green)
                   3 - attackable but not criminal (gray)
                   4 - criminal (gray)
                   5 - enemy (orange)
                   6 - murderer (red)
    Returns:
        Object ID if found, 0 if not found
    """
    if obj_type == -1:
        obj_type = 0xFFFF

    return api.FindNotoriety(obj_type, notoriety)


# Count helpers
def Count(obj_type: int) -> int:
    """Count items of type in backpack."""
    FindType(obj_type, api.Backpack())
    return api.FindFullQuantity()


def CountGround(obj_type: int) -> int:
    """Count items of type on ground."""
    FindType(obj_type, Ground())
    return api.FindFullQuantity()


def CountEx(obj_type: int, color: int, container: int) -> int:
    """Count items of type and color in container."""
    FindTypeEx(obj_type, color, container, False)
    return api.FindFullQuantity()


# Reagent types helpers
def BP() -> int:
    """Count Black Pearl in backpack."""
    return Reagent.BlackPearl


def BM() -> int:
    """Count Blood Moss in backpack."""
    return Reagent.BloodMoss


def GA() -> int:
    """Count Garlic in backpack."""
    return Reagent.Garlic


def GS() -> int:
    """Count Ginseng in backpack."""
    return Reagent.Ginseng


def MR() -> int:
    """Count Mandrake Root in backpack."""
    return Reagent.MandrakeRoot


def NS() -> int:
    """Count Nightshade in backpack."""
    return Reagent.Nightshade


def SA() -> int:
    """Count Sulfurous Ash in backpack."""
    return Reagent.SulfurousAsh


def SS() -> int:
    """Count Spider's Silk in backpack."""
    return Reagent.SpidersSilk


# Reagent count helpers
def BPCount() -> int:
    """Count Black Pearl in backpack."""
    return CountEx(Reagent.BlackPearl, 0, api.Backpack())


def BMCount() -> int:
    """Count Blood Moss in backpack."""
    return CountEx(Reagent.BloodMoss, 0, api.Backpack())


def GACount() -> int:
    """Count Garlic in backpack."""
    return CountEx(Reagent.Garlic, 0, api.Backpack())


def GSCount() -> int:
    """Count Ginseng in backpack."""
    return CountEx(Reagent.Ginseng, 0, api.Backpack())


def MRCount() -> int:
    """Count Mandrake Root in backpack."""
    return CountEx(Reagent.MandrakeRoot, 0, api.Backpack())


def NSCount() -> int:
    """Count Nightshade in backpack."""
    return CountEx(Reagent.Nightshade, 0, api.Backpack())


def SACount() -> int:
    """Count Sulfurous Ash in backpack."""
    return CountEx(Reagent.SulfurousAsh, 0, api.Backpack())


def SSCount() -> int:
    """Count Spider's Silk in backpack."""
    return CountEx(Reagent.SpidersSilk, 0, api.Backpack())


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

    Wait(api.GetDropDelay())
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


__all__ = [
    'FinderSettings', 'Finder',
    'GetFoundList', 'Ground', 'FindType', 'FindTypeEx', 'FindTypesArrayEx', 'FindNotoriety',
    'Count', 'CountGround', 'CountEx',
    'BPCount', 'BMCount', 'GACount', 'GSCount', 'MRCount', 'NSCount', 'SACount', 'SSCount',
    'BP', 'BM', 'GA', 'GS', 'MR', 'NS', 'SA', 'SS',
    'MoveItem', 'Grab', 'Drop', 'DropHere', 'MoveItems', 'EmptyContainer',
    'ClickOnObject',
]
