# import all methods from generated interface file to help the IDE
from py_astealth.generated.sync_module import *

from py_astealth.stealth._internals import _create_global_proxy
from py_astealth.stealth_api import StealthApi

from py_astealth.stealth import methods as _methods
from py_astealth.generated import sync_module as _sync_module


# binding real proxy functions to stubs
globals().update({
    spec.name: _create_global_proxy(spec) for spec in StealthApi.get_methods()
})

# Import helpers, overriding any API methods if names collide (e.g. AddToSystemJournal)
from py_astealth.stealth.methods import *


__all__ = sorted(set(_sync_module.__all__) | set(_methods.__all__))
