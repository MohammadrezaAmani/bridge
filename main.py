import yaml
from typing import Any

with open("data.yaml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

FUNC_TEMPLATE = """
@idk.{format}(path="{path}"{compiler_options})
async def {name}({args}) -> {return_type}:{doc}
  ...
"""

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

imports = ["from typing import Any", "from idkwhy import IdkWhy"]


initialization = """

idk = IdkWhy()

"""

outputs = []


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


f = open("out.py", "w")

if "functions" in data["data"]:
    for func in data["data"]["functions"]:
        func_name = func["name"]
        func_args = ", ".join(
            [
                f"{arg['name']}: {convert_type(arg['type'])} = {arg['default']}"
                for arg in func["args"]
            ]
        )
        func_return_type = ", ".join([convert_type(i) for i in func["outputs"]])
        func_doc = "\n" + func["doc"] if func["doc"] else ""
        func_return_value = ", ".join([f"{arg['name']}" for arg in func["args"]])
        if len(func["outputs"]) > 1:
            func_return_type = f"Tuple[{func_return_type}]"
            imports.append("from typing import Tuple")

        outputs.append(
            FUNC_TEMPLATE.format(
                path=func["path"],
                format=get_format(func["path"]),
                compiler_options=(
                    ", ".join([f"{k}={v}" for k, v in func["compiler_options"].items()])
                    if "compiler_options" in func
                    else ""
                ),
                name=func_name,
                args=func_args,
                return_type=func_return_type,
                doc=func_doc,
                return_value=func_return_value,
            )
        )


with open("out.py", "w") as f:
    f.write("\n".join(imports))
    f.write("\n")
    f.write(initialization)
    f.write("\n")
    f.write("\n".join(outputs))
    f.write("\n")


def update_code_format(
    file: str,
    with_isort: bool = True,
    with_black: bool = True,
    # with_ruff: bool = True,
    order: list = ["isort", "black"],
) -> "None":
    """
    Updates the format of the source code using black.
    """
    import pathlib

    file = pathlib.Path(file)

    for i in order:
        if i == "isort" and with_isort:
            import isort

            isort.file(file)
        elif i == "black" and with_black:
            import black

            black.format_file_in_place(
                file,
                mode=black.FileMode(line_length=110),
                fast=False,
                write_back=black.WriteBack.YES,
            )


update_code_format("out.py")
