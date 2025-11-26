"""
Synchronous wrappers for all Stealth API methods.
Auto-generated from StealthApi specification.

This module provides direct access to all API methods in a synchronous manner,
using the global client manager to handle threading and async operations.
"""

from py_astealth.stealth_api import StealthApi
from ._internals import _create_global_proxy

from py_astealth.generated.sync_module import *

# Auto-generate synchronous wrappers for all API methods
__all__ = []

for spec in StealthApi.get_methods():
    # Create a global wrapper function for each API method
    globals()[spec.name] = _create_global_proxy(spec)
    __all__.append(spec.name)
