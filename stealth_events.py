from dataclasses import dataclass
from typing import Any, Dict, Type, List

from py_astealth.stealth_enums import EventType


@dataclass
class StealthEvent:
    """
    Base class for all Stealth events.
    Stored arguments in 'arguments' list for backward compatibility.
    """
    id: EventType
    arguments: List[Any]


@dataclass
class SpeechEvent(StealthEvent):
    text: str
    sender_name: str
    serial: int


@dataclass
class ItemInfoEvent(StealthEvent):
    serial: int


@dataclass
class AddItemToContainerEvent(StealthEvent):
    serial: int
    container_serial: int


@dataclass
class AddMultipleItemsInContEvent(StealthEvent):
    container_serial: int


@dataclass
class ItemDeletedEvent(StealthEvent):
    serial: int


@dataclass
class DrawObjectEvent(StealthEvent):
    serial: int


@dataclass
class RejectMoveItemEvent(StealthEvent):
    reason: int


@dataclass
class DrawContainerEvent(StealthEvent):
    serial: int
    graphic_id: int


@dataclass
class IncomingGumpEvent(StealthEvent):
    serial: int
    gump_id: int
    x: int
    y: int


@dataclass
class MenuEvent(StealthEvent):
    serial: int
    menu_id: int


@dataclass
class ContextMenuEvent(StealthEvent):
    serial: int


@dataclass
class SoundEvent(StealthEvent):
    sound_id: int
    x: int
    y: int
    z: int


@dataclass
class CharAnimationEvent(StealthEvent):
    serial: int
    action: int


class EventFactory:

    _registry: Dict[EventType, Type[StealthEvent]] = {
        EventType.EvSpeech: SpeechEvent,
        EventType.EvItemInfo: ItemInfoEvent,
        EventType.EvAddItemToContainer: AddItemToContainerEvent,
        EventType.EvAddMultipleItemsInCont: AddMultipleItemsInContEvent,
        EventType.EvItemDeleted: ItemDeletedEvent,
        EventType.EvRejectMoveItem: RejectMoveItemEvent,
        EventType.EvDrawObject: DrawObjectEvent,
        EventType.EvDrawContainer: DrawContainerEvent,
        EventType.EvIncomingGump: IncomingGumpEvent,
        EventType.EvMenu: MenuEvent,
        EventType.EvContextMenu: ContextMenuEvent,
        EventType.EvSound: SoundEvent,
        EventType.EvCharAnimation: CharAnimationEvent,
    }

    @classmethod
    def create(cls, event_id: int, arguments: list) -> StealthEvent:
        event_type = EventType(event_id)
        event_cls = cls._registry.get(event_type)
        
        if event_cls:
            try:
                # Unpack arguments directly into the constructor.
                # Constructor signature: cls(id, arguments, *subclass_fields)
                return event_cls(event_type, arguments, *arguments)
            except (TypeError, ValueError, IndexError):
                # Fallback if arguments don't match the signature
                return StealthEvent(id=event_type, arguments=arguments)
        
        return StealthEvent(id=event_type, arguments=arguments)
