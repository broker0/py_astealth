import inspect
import typing
import json
from typing import Any, Type
from py_astealth.core.api_specification import ApiSpecification, MethodSpec

class CodeGenerator:
    def __init__(self, api_spec: Type[ApiSpecification]):
        self.api_spec = api_spec

    @staticmethod
    def get_type_name(type_obj: Any) -> str:
        """returns a string representation of the type"""
        if type_obj is type(None):
            return "None"

        origin = typing.get_origin(type_obj)
        if origin is list:  # list special case
            arg_list = []
            for arg in typing.get_args(type_obj):
                arg_list.append(f"{CodeGenerator.get_type_name(arg)}")

            inner_types = ", ".join(arg_list)
            return f"{origin.__name__}[{inner_types}]"

        # apply type mapping, for example 'I8' will be replaced with 'int'
        if hasattr(type_obj, '_mapping') and type_obj._mapping is not None:
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

        # Do NOT apply type mapping - keep original type name
        if hasattr(type_obj, '__name__'):
            return type_obj.__name__

        return str(type_obj)

    def generate_json(self, output_path):
        """
        Generate JSON file with API specification
        """
        methods_data = []
        
        for spec in self.api_spec.get_methods():
            # Build args list
            args_list = []
            for arg in spec.args:
                args_list.append({
                    "name": arg.name,
                    "type": self.get_original_type_name(arg.type)
                })
            
            # Build method entry
            method_entry = {
                "name": spec.name,
                "id": spec.id,
                "args": args_list,
                "result": self.get_original_type_name(spec.result.type)
            }
            
            methods_data.append(method_entry)
        
        # Sort by id for better readability
        methods_data.sort(key=lambda x: x["id"])
        
        # Write to file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(methods_data, f, indent=4, ensure_ascii=False)
        
        print(f"JSON API specification '{self.api_spec.__name__}' generated in '{output_path}'")

    def generate_module(self, output_path, sync):
        lines = [
            "###################################################################",
            "# This file was generated automatically. Do not edit it manually! #",
            "###################################################################",
            "", "",
            f"from py_astealth.stealth_types import *",
            f"from py_astealth.stealth_structs import *",
            f"from datetime import datetime",
            "", "",
            ""
        ]
        prefix = "" if sync else "async "
        for spec in self.api_spec.get_methods():
            arg_list = []
            for arg in spec.args:
                arg_list.append(f"{arg.name}: {self.get_type_name(arg.type)}")

            args_str = ", ".join(arg_list)
            ret_type_str = self.get_type_name(spec.result.type)

            lines.append(f"{prefix}def {spec.name}({args_str}) -> {ret_type_str}: pass")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"{prefix}module '{self.api_spec.__name__}' generated in '{output_path}'")

    def generate_base_class(self, output_path: str, class_name: str, sync):
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
            f"from datetime import datetime",
            "", "",
            f"class {class_name}:",
            f"    \"\"\"base class defining the interface of {self.api_spec.__name__}.\"\"\"",
            ""
        ]
        prefix = "" if sync else "async "

        for spec in self.api_spec.get_methods():
            arg_list = ['self']
            for arg in spec.args:
                arg_list.append(f"{arg.name}: {self.get_type_name(arg.type)}")

            args_str = ", ".join(arg_list)
            ret_type_str = self.get_type_name(spec.result.type)

            lines.append(f"    {prefix}def {spec.name}({args_str}) -> {ret_type_str}: pass")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"{prefix}interface '{self.api_spec.__name__}' generated in '{output_path}'")
