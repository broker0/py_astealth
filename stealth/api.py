"""
Synchronous wrappers for all Stealth API methods.
Auto-generated from StealthApi specification.

This module provides direct access to all API methods in a synchronous manner,
using the global client manager to handle threading and async operations.
"""

from py_astealth.stealth_api import StealthApi
from ._internals import _create_global_proxy

from py_astealth.generated.sync_module import *
from py_astealth.generated import sync_module as _sync_module

# Auto-generate synchronous wrappers for all API methods
globals().update({
    spec.name: _create_global_proxy(spec) for spec in StealthApi.get_methods()
})


__all__ = sorted(set(_sync_module.__all__))
