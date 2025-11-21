import json

PASCAL_TO_PYTHON_TYPE_MAP = {
    "string": "String",
    "byte": "I8",
    "ubyte": "U8",
    "word": "U16",
    "short": "I16",
    "shortint": "I16",
    "ushort": "U16",
    "integer": "I32",
    "uint": "U32",
    "cardinal": "U32",
    "int64": "I64",
    "single": "F32",
    "double": "F64",
    "datetime": "DateTime",
    "tdatetime": "DateTime",
    "bool": "Bool",
    "boolean": "Bool",
    "variant": "Any",

    "": "None"
}


def convert_type(pascal_type: str) -> str:
    stripped_type = pascal_type.strip()
    lookup_key = stripped_type.lower()

    return PASCAL_TO_PYTHON_TYPE_MAP.get(lookup_key, stripped_type)


def generate_python_class(api_definitions: list) -> str:
    class_code = [
        "class StealthApi(ApiSpecification):",
        '    """',
        "    Declarative API description using decorators.",
        "    The key is the method signatures with a detailed description of the argument types and the return type.",
        "    Methods do not have to have an implementation, they are just a protocol specification.",
        '    """',
        ""
    ]

    for method in api_definitions:
        method_id = method.get("id")
        pascal_name = method.get("pascal_name")
        args = method.get("args", [])

        # Преобразуем тип возвращаемого значения
        result_type = convert_type(method.get("result", ""))

        # Формируем список аргументов с преобразованными типами
        formatted_args = []
        for arg in args:
            arg_name = arg.get("name", "").strip()
            # Преобразуем тип аргумента
            arg_type = convert_type(arg.get("type", ""))
            formatted_args.append(f"{arg_name}: {arg_type}")

        method_signature = f"self, {', '.join(formatted_args)}" if formatted_args else "self"

        # Собираем итоговый код для метода
        class_code.append(f"    @ApiSpecification.method({method_id})")
        class_code.append(f"    def {pascal_name}({method_signature}) -> {result_type}:")
        class_code.append("        pass")
        class_code.append("")

    return "\n".join(class_code)


with open('stealth_methods.json', 'rt') as fl:
    json_data = fl.read()
    api_definitions = json.loads(json_data)

    api_definitions = sorted(api_definitions, key=lambda v: v['id'])

    api_class = generate_python_class(api_definitions)
    print(api_class)
