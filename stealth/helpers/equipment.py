"""Equipment helpers: managing character equipment."""
from py_astealth.stealth import api
from py_astealth.stealth_enums import Layer

from .items import FindType, MoveItem
from .common import Wait


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


def Undress() -> bool:
    """
    Undress all layers.
    """
    dress_set = []
    client_version_int = api.GetClientVersionInt()
    if client_version_int < 7007400:
        delay = api.GetDressSpeed()
        char = api.Self()
        backpack = api.Backpack()
        wearable_layers = (
            RhandLayer(), LhandLayer(), ShoesLayer(), PantsLayer(),
            ShirtLayer(), HatLayer(), GlovesLayer(), RingLayer(),
            NeckLayer(), WaistLayer(), TorsoLayer(), BraceLayer(),
            TorsoHLayer(), EarLayer(), ArmsLayer(), CloakLayer(),
            RobeLayer(), EggsLayer(), LegsLayer()
        )
        for layer in wearable_layers:
            item = api.ObjAtLayerEx(layer, char)
            if item:
                dress_set.append(MoveItem(item, 1, backpack, 0, 0, 0))
                Wait(delay)
    else:
        api.UnequipItemsSetMacro()
        dress_set.append(True)
    return all(dress_set)


def EquipDressSet() -> bool:
    """Equip the saved dress set."""
    res = []
    client_version_int = api.GetClientVersionInt()
    if client_version_int < 7007400:
        delay = api.GetDressSpeed()
        dress_set = api.GetDressSet()
        for layer_obj in dress_set:
            if layer_obj.ObjID:
                res.append(Equip(layer_obj.Layer, layer_obj.ObjID))
                Wait(delay)
    else:
        api.EquipItemsSetMacro()
        res.append(True)
    return all(res)


def DressSavedSet() -> None:
    """Alias for EquipDressSet."""
    EquipDressSet()


__all__ = [
    'ObjAtLayer', 'Equip', 'Equipt', 'UnEquip', 'Disarm',
    'Undress', 'EquipDressSet', 'DressSavedSet',
    'RhandLayer', 'LhandLayer', 'ShoesLayer', 'PantsLayer', 'ShirtLayer', 'HatLayer',
    'GlovesLayer', 'RingLayer', 'TalismanLayer', 'NeckLayer', 'HairLayer', 'WaistLayer',
    'TorsoLayer', 'BraceLayer', 'BeardLayer', 'TorsoHLayer', 'EarLayer', 'ArmsLayer',
    'CloakLayer', 'BpackLayer', 'RobeLayer', 'EggsLayer', 'LegsLayer', 'HorseLayer',
    'RstkLayer', 'NRstkLayer', 'SellLayer', 'BankLayer',
]
