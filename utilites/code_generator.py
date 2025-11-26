import inspect
import typing
import json
from typing import Any, Type

from py_astealth.core.api_specification import ApiSpecification
from py_astealth.stealth_api import StealthApi


class CodeGenerator:
    # Константы для генерации
    COMMON_IMPORTS = [
        "from py_astealth.stealth_types import *",
        "from py_astealth.stealth_structs import *",
        "from py_astealth.stealth_enums import *",
        "from datetime import datetime",
    ]

    HEADER = [
        "###################################################################",
        "# This file was generated automatically. Do not edit it manually! #",
        "###################################################################",
    ]


    def __init__(self, api_spec: Type[ApiSpecification]):
        self.api_spec = api_spec

    def _format_type_name(self, type_obj: Any, use_mapping: bool = True) -> str:
        """
        Returns a string representation of the type.
        :param use_mapping: If True, applies _mapping (e.g., I8 -> int).
        """
        if type_obj is type(None):
            return "None"

        origin = typing.get_origin(type_obj)

        # Recursive processing of containers (List, Tuple, etc.)
        if origin is not None:
            args = [self._format_type_name(arg, use_mapping) for arg in typing.get_args(type_obj)]
            return f"{origin.__name__}[{', '.join(args)}]"

        # Apply type mapping if required
        if use_mapping and hasattr(type_obj, '_mapping') and type_obj._mapping is not None:
            type_obj = type_obj._mapping

        if hasattr(type_obj, '__name__'):
            return type_obj.__name__

        return str(type_obj)


    @staticmethod
    def get_original_type_name(type_obj: Any) -> str:
        """returns the original type name without applying _mapping transformation"""
        if type_obj is type(None):
            return "None"

        origin = typing.get_origin(type_obj)
        if origin is list:  # list special case
            arg_list = []
            for arg in typing.get_args(type_obj):
                arg_list.append(f"{CodeGenerator.get_original_type_name(arg)}")

            inner_types = ", ".join(arg_list)
            return f"{origin.__name__}[{inner_types}]"

        if origin is tuple:
            arg_list = []
            for arg in typing.get_args(type_obj):
                arg_list.append(f"{CodeGenerator.get_original_type_name(arg)}")

            inner_types = ", ".join(arg_list)
            return f"{origin.__name__}[{inner_types}]"

        # Do NOT apply type mapping - keep original type name
        if hasattr(type_obj, '__name__'):
            return type_obj.__name__

        return str(type_obj)

    def generate_json(self, output_path):
        """Generate JSON file with API specification"""
        methods_data = []

        for spec in self.api_spec.get_methods():
            args_list = [{
                "name": arg.name,
                "type": self._format_type_name(arg.type, use_mapping=False)
            } for arg in spec.args]

            methods_data.append({
                "name": spec.name,
                "id": spec.id,
                "args": args_list,
                "result": self._format_type_name(spec.result.type, use_mapping=False)
            })

        methods_data.sort(key=lambda x: x["id"])

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(methods_data, f, indent=4, ensure_ascii=False)

        print(f"JSON API specification generated in '{output_path}'")

    def _write_file(self, path: str, lines: list[str]):
        """Utility for writing a list of lines to a file"""
        with open(path, "wt", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"Generated: {path}")

    def _build_method_signature(self, spec, is_async: bool, include_self: bool) -> str:
        """Builds a method signature string: def name(args) -> ret: pass"""
        arg_parts = []

        if include_self:
            arg_parts.append("self")

        for arg in spec.args:
            type_str = self._format_type_name(arg.type, use_mapping=True)
            arg_parts.append(f"{arg.name}: {type_str}")

        args_str = ", ".join(arg_parts)
        ret_type_str = self._format_type_name(spec.result.type, use_mapping=True)
        prefix = "async " if is_async else ""

        return f"{prefix}def {spec.name}({args_str}) -> {ret_type_str}: pass"

    def generate_python(self, output_path: str, is_async: bool, class_name: typing.Optional[str] = None):
        """
        A universal method for generating Python code.
        If a class_name is passed, it generates a class. Otherwise, it generates a flat module.
        """
        lines = self.HEADER + ["", ""] + self.COMMON_IMPORTS + ["", ""]

        indent = ""
        include_self = False

        if class_name:
            lines.append(f"class {class_name}:")
            lines.append(f'    """Base class defining the interface of {self.api_spec.__name__}."""')
            lines.append("")
            indent = "    "
            include_self = True

        for spec in self.api_spec.get_methods():
            signature = self._build_method_signature(spec, is_async, include_self)
            lines.append(f"{indent}{signature}")

        self._write_file(output_path, lines)


def main():
    generator = CodeGenerator(StealthApi)

    # classes
    generator.generate_python("../generated/sync_interface.py", is_async=False, class_name="SyncInterface")
    generator.generate_python("../generated/async_interface.py", is_async=True, class_name="AsyncInterface")

    # modules
    generator.generate_python("../generated/async_module.py", is_async=True)
    generator.generate_python("../generated/sync_module.py", is_async=False)

    # json
    generator.generate_json('../generated/methods.json')


if __name__ == "__main__":
    main()
