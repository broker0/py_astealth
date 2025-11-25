"""Equipment helpers: managing character equipment."""
from py_astealth.stealth import api
from .base import LhandLayer, RhandLayer
from .items import FindType, MoveItem


def ObjAtLayer(layer: int) -> int:
    """
    Get object at specified layer on self.
    
    Args:
        layer: Layer ID
        
    Returns:
        Object ID at layer, or 0 if empty
    """
    return api.ObjAtLayerEx(layer, api.Self())


def Equip(layer: int, obj: int) -> bool:
    """
    Equip an item to specified layer.
    
    Args:
        layer: Layer to equip to
        obj: Object ID to equip
        
    Returns:
        True if successful, False otherwise
    """
    if layer and api.DragItem(obj, 1):
        api.WearItem(layer, obj)
        api.SetPickupedItem(0)
        return True
    return False


def Equipt(layer: int, obj_type: int) -> bool:
    """
    Find and equip item of specified type from backpack.
    
    Args:
        layer: Layer to equip to
        obj_type: Item type to find and equip
        
    Returns:
        True if successful, False otherwise
    """
    item = FindType(obj_type, api.Backpack())
    if item:
        return Equip(layer, item)
    return False


def UnEquip(layer: int) -> bool:
    """
    Remove item from specified layer to backpack.
    
    Args:
        layer: Layer to remove from
        
    Returns:
        True if successful, False otherwise
    """
    item = ObjAtLayer(layer)
    if item:
        return MoveItem(item, 1, api.Backpack(), 0, 0, 0)
    return False


def Disarm() -> bool:
    """
    Remove weapons from both hands to backpack.
    
    Returns:
        True if all items removed successfully
    """
    backpack = api.Backpack()
    results = []
    for layer in [LhandLayer(), RhandLayer()]:
        item = ObjAtLayer(layer)
        if item:
            results.append(MoveItem(item, 1, backpack, 0, 0, 0))
    return all(results) if results else True


__all__ = [
    'ObjAtLayer', 'Equip', 'Equipt', 'UnEquip', 'Disarm',
]
