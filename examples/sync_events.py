from time import sleep

from py_astealth.api_client import SyncStealthApiClientFast, SyncStealthApiClient
from py_astealth.stealth_client import EventType
from py_stealth.protocol import get_port


def main():
    client = SyncStealthApiClientFast("127.0.0.1", get_port())
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
