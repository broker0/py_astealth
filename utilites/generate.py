from py_astealth.stealth_api import StealthApi


def main():
    StealthApi.generate_base_class("../generated/sync_interface.py", "SyncInterface", True)
    StealthApi.generate_base_class("../generated/async_interface.py", "AsyncInterface", False)
    StealthApi.generate_module("../generated/async_module.py", False)
    StealthApi.generate_module("../generated/sync_module.py", True)
    StealthApi.generate_json('../generated/methods.json')


if __name__ == "__main__":
    main()

