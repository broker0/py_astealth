from py_astealth import stealth
from py_astealth.stealth_client import EventType


def speech_handler(text, sender_name, sender_id):
    print(f"Speech {sender_name}({sender_id}): {text}")


def iteminfo_handler(item_id):
    print(f"ItemInfo {item_id}")


def event_handlers_demo():
    stealth.SetEventProc(EventType.EvSpeech, speech_handler)
    stealth.SetEventProc(EventType.EvItemInfo, iteminfo_handler)

    while True:
        stealth.Wait(100)


def event_wait_demo():
    stealth.SetEventCallback(EventType.EvSpeech)
    stealth.SetEventCallback(EventType.EvItemInfo)

    while True:
        event = stealth.WaitForEvent(100)
        if event:
            print(event)




event_wait_demo()
# event_handlers_demo()
