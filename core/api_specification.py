import inspect
import os

from typing import Any, get_type_hints, Callable, Optional

from py_astealth.core.base_types import ParameterSpec, MethodSpec
from py_astealth.core.codec import build_args_decoder, build_packet_encoder, build_result_decoder


# Per-call RPC timeouts can be controlled two ways:
#   (1) `py_astealth.set_per_call_timeout(t)` — runtime API, primary path.
#   (2) `PY_ASTEALTH_NO_TIMEOUT=1` env var — read once at import time, kept as
#       a deployment-time fallback (e.g. for Stealth-launcher .bat or ps1 files
#       where Python code can't easily be edited).
# Effect is workload-dependent (see notes in pull requests for measurements):
# drop-in sync module gains ~+20%, Pool LOSES ~15% due to scheduling
# interactions, others are noise. Trade-off when disabled: a hung Stealth
# server blocks the call indefinitely; only connection-level TCP errors
# surface. Default: timeouts ON at the project default of 1.0s per call.
_DISABLE_TIMEOUTS_AT_IMPORT = os.environ.get("PY_ASTEALTH_NO_TIMEOUT") == "1"


class ApiSpecification:
    @classmethod
    def get_methods(cls) -> list[MethodSpec]:
        """
        Return collected methods specifications.
        """
        return getattr(cls, '_methods_list', [])

    @classmethod
    def get_method(cls, method_id: int) -> Optional[MethodSpec]:
        """
        Find a method specification by its ID using a pre-calculated dictionary.
        """
        return getattr(cls, '_methods_dict', {}).get(method_id)


def method_api(method_id: int, timeout: float | None = 1.0):
    """
    This decorator inspects the method signature to construct a MethodSpec
    with arguments and result and attach this to decorated method as 'method_spec' attribute.

    :param method_id: unique method identifier
    :param timeout: RPC timeout in seconds
    """
    def decorator(func):
        hints = get_type_hints(func)
        sig = inspect.signature(func)

        # we go through all the arguments of the method, skipping self
        args = [
            ParameterSpec(name, hints.get(name, Any))
            for name, param in sig.parameters.items()
            if name != 'self'
        ]

        # get the return value type
        return_type = hints.get('return', type(None))

        # form a method descriptor
        effective_timeout = None if _DISABLE_TIMEOUTS_AT_IMPORT else timeout
        method_spec = MethodSpec(
            id=method_id,
            name=func.__name__,
            args=args,
            result=ParameterSpec("Result", return_type),
            timeout=effective_timeout,
        )

        # Precompile encoder/decoder closures so the hot path skips per-call
        # reflection. `decode_result` is None when the method returns None.
        # `decode_args` decodes incoming packets (most importantly
        # `_FunctionResultCallback` — fires once per reply).
        method_spec.encode_packet = build_packet_encoder(method_id, args)
        method_spec.decode_result = build_result_decoder(return_type)
        method_spec.decode_args = build_args_decoder(args)

        func.method_spec = method_spec

        return func

    return decorator


def set_per_call_timeout(timeout: float | None) -> None:
    """Override the per-call RPC timeout for every registered Stealth method.

    Pass ``None`` to disable per-call timeouts entirely (skips
    ``asyncio.wait_for`` — saves ~5-10% per call on async paths). Pass any
    positive float to set a uniform per-call timeout in seconds. Pass ``1.0``
    to restore the project default.

    Can be called at any time. ``call_method`` reads ``MethodSpec.timeout`` on
    every call, so the change takes effect immediately for in-flight clients
    (no need to reconnect).

    Effect of disabling is **workload-dependent** — see notes in pull request
    for measured numbers. The drop-in ``py_astealth.stealth`` sync module gains
    ~+20%; ``AsyncClientPool`` LOSES ~15% due to scheduling interactions. Use
    with care if you rely on Pool throughput.

    Trade-off when disabled: a hung Stealth server blocks the call indefinitely.
    Only connection-level TCP errors will surface.
    """
    # Late import: `stealth_api` imports this module, so we can't pull it at
    # module top.
    from py_astealth.stealth_api import StealthApi
    for spec in StealthApi.get_methods():
        spec.timeout = timeout


def register_api(cls):
    """
    Class decorator that scans the class for methods with 'method_spec' attribute
    and creates _methods_list and _methods_dict for efficient lookup.
    """
    methods_list = []
    methods_dict = {}

    for _, member in inspect.getmembers(cls):
        if hasattr(member, 'method_spec'):
            spec = member.method_spec
            methods_list.append(spec)
            methods_dict[spec.id] = spec

    setattr(cls, '_methods_list', methods_list)
    setattr(cls, '_methods_dict', methods_dict)

    return cls


def implement_api(api_spec: type[ApiSpecification], method_factory: Callable[[MethodSpec], Callable]):
    """
    This decorator for methods from 'api_spec' creates an implementation by
    calling the function factory 'method_factory' with the argument of MethodSpec
    and binds this implementation to the decorated class.
    """
    def decorator(cls):
        for spec in api_spec.get_methods():
            # bind method using method_factory
            method_function = method_factory(spec)
            setattr(cls, spec.name, method_function)
        return cls

    return decorator
