from time import sleep

from py_astealth.sync.client import SyncStealthApiClient
from py_astealth.stealth_types import EventType


def main():
    client = SyncStealthApiClient()
    client.connect()
    client.SetEventCallback(EventType.EvSpeech)
    client.SetEventCallback(EventType.EvItemInfo)
    client.SetEventCallback(EventType.EvSound)

    while True:
        event = client.get_event()
        if event:
            print(event)

        sleep(1/1000)


if __name__ == "__main__":
    main()
