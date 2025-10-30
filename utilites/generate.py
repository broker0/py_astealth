from py_astealth.stealth_api import StealthApi


def main():
    StealthApi.generate_base_class("../generated/sync_interface.py", "SyncInterface", True)
    StealthApi.generate_base_class("../generated/async_interface.py", "AsyncInterface", False)


if __name__ == "__main__":
    main()

