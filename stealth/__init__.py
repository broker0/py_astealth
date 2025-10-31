# import all methods from generated interface file to help the IDE
from py_astealth.generated.sync_module import *

from ._internals import _create_global_proxy
from py_astealth.stealth_api import StealthApi


__all__ = []


def _populate_module():
    """
    Dynamically creates and adds all API functions to this module.
    """
    current_module = globals()
    specs = StealthApi.get_methods()

    for spec in specs:
        proxy_function = _create_global_proxy(spec)
        current_module[spec.name] = proxy_function
        __all__.append(spec.name)


_populate_module()
