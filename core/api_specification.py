import inspect
from dataclasses import dataclass
from typing import Any, get_type_hints, Callable, Optional

from py_astealth.core.base_types import ParameterSpec


@dataclass
class MethodSpec:
    id: int
    name: str
    args: list[ParameterSpec]
    result: Any


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


def method_api(method_id: int):
    """
    This decorator inspects the method signature to construct a MethodSpec
    with arguments and result and attach this to decorated method as 'method_spec' attribute.
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
        method_spec = MethodSpec(
            id=method_id,
            name=func.__name__,
            args=args,
            result=ParameterSpec("Result", return_type),
        )

        func.method_spec = method_spec

        return func

    return decorator


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
