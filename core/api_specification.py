import inspect
from dataclasses import dataclass
from typing import Any, get_type_hints, Callable

from py_astealth.core.base_types import ParameterSpec


@dataclass
class MethodSpec:
    id: int
    name: str
    args: list[ParameterSpec]
    result: Any


class ApiSpecification:
    @classmethod
    def method(cls, method_id: int):
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

            # cls._methods.append(method_spec)
            func.method_spec = method_spec

            return func

        return decorator

    @classmethod
    def get_methods(cls) -> list[MethodSpec]:
        """
        Dynamically collect methods specifications from class attributes.
        """

        return [
            member.method_spec
            for _, member in inspect.getmembers(cls)
            if hasattr(member, 'method_spec')  # We are only interested in those who have 'method_spec' field
        ]

    @classmethod
    def get_method_by_id(cls, method_id: int) -> MethodSpec | None:
        """
        Find a method specification by its ID.
        """
        for spec in cls.get_methods():
            if spec.id == method_id:
                return spec
        return None


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
