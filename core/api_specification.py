import asyncio
import inspect
import typing
from dataclasses import dataclass
from typing import Any, get_type_hints, Callable


@dataclass
class ParameterSpec:
    name: str
    type: Any


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

    @staticmethod
    def get_type_name(type_obj: Any) -> str:
        """returns a string representation of the type"""
        if type_obj is type(None):
            return "None"

        origin = typing.get_origin(type_obj)
        if origin is list:  # list special case
            arg_list = []
            for arg in typing.get_args(type_obj):
                arg_list.append(f"{ApiSpecification.get_type_name(arg)}")

            inner_types = ", ".join(arg_list)
            return f"{origin.__name__}[{inner_types}]"

        # apply type mapping, for example 'I8' will be replaced with 'int'
        if hasattr(type_obj, '_mapping') and type_obj._mapping is not None:
            type_obj = type_obj._mapping

        if hasattr(type_obj, '__name__'):
            return type_obj.__name__

        return str(type_obj)

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
    def generate_base_class(cls, output_path: str, class_name: str, sync):
        """
        generates a base class interface with defined method signatures
        """

        lines = [
            "###################################################################",
            "# This file was generated automatically. Do not edit it manually! #",
            "###################################################################",
            "", "",
            f"from py_astealth.stealth_types import *",
            f"from py_astealth.stealth_structs import *",
            "", "",
            f"class {class_name}:",
            f"    \"\"\"base class defining the interface of {cls.__name__}.\"\"\"",
            ""
        ]
        prefix = "" if sync else "async "

        for spec in cls.get_methods():
            arg_list = ['self']
            for arg in spec.args:
                arg_list.append(f"{arg.name}: {cls.get_type_name(arg.type)}")

            args_str = ", ".join(arg_list)
            ret_type_str = ApiSpecification.get_type_name(spec.result.type)

            lines.append(f"    {prefix}def {spec.name}({args_str}) -> {ret_type_str}:")
            lines.append(f"        raise NotImplementedError")
            lines.append("")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"Async interface '{cls.__name__}' generated in '{output_path}'")


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
