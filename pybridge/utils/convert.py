from typing import Any

type_table = {
    "string": "str",
    "integer": "int",
    "float": "float",
    "boolean": "bool",
    "any": "Any",
    "null": "None",
    "object": "Dict",
    "array": "List",
}


def convert_type(type: str = None):
    if type in type_table:
        return type_table[type]
    return Any


formats = {
    "js": "js",
    "jsx": "js",
    "ts": "ts",
    "tsx": "ts",
    "py": "py",
    "pyo": "py",
    "pyc": "py",
    "c": "c",
    "cpp": "cpp",
    "h": "h",
    "hpp": "hpp",
}


def get_format(path: str):
    return formats[path.split(".")[-1]]
