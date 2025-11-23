from py_astealth.stealth_api import StealthApi
from py_astealth.utilites.code_generator import CodeGenerator


def main():
    generator = CodeGenerator(StealthApi)
    generator.generate_base_class("../generated/sync_interface.py", "SyncInterface", True)
    generator.generate_base_class("../generated/async_interface.py", "AsyncInterface", False)
    generator.generate_module("../generated/async_module.py", False)
    generator.generate_module("../generated/sync_module.py", True)
    generator.generate_json('../generated/methods.json')


if __name__ == "__main__":
    main()

