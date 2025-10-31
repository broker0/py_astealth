import threading
from py_astealth import stealth

COUNT = 5000


def worker(item_type):
    print(f"Thread {threading.get_ident()} finding {hex(item_type)}...")
    # first call in this thread create new connection
    obj_id = stealth.FindTypeEx(item_type, 0xFFFF, 0, False)

    if obj_id:
        print(f"Thread {threading.get_ident()}: found {obj_id}!")
    else:
        print(f"Thread {threading.get_ident()}: not found")


threads = [
    threading.Thread(target=worker, args=(0x0EED,)),  # Gold
    threading.Thread(target=worker, args=(0x1BF2,)),  # Bandage
    threading.Thread(target=worker, args=(0x0F88,)),  # Nightshade
]

for t in threads:
    t.start()

for t in threads:
    t.join()

