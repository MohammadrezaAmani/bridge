import pathlib
import yaml
from typing import Any, List, Tuple

from pybridge.utils.templates import FUNC_TEMPLATE, IMPORTS, INITIAL, OUTPUT
from pybridge.utils.convert import convert_type, get_format

DATA_PATH = "example.yaml"


def update_code_format(
    file: str,
    with_isort: bool = True,
    with_black: bool = True,
    order: List[str] = ["isort", "black"],
) -> None:
    """
    Updates the format of the source code using black.
    """
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


def read(path: str = DATA_PATH) -> str:
    imports = IMPORTS.copy()
    output = []

    with open(path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

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

            output.append(
                FUNC_TEMPLATE.format(
                    path=func["path"],
                    format=get_format(func["path"]),
                    compiler_options=(
                        ", ".join(
                            [f"{k}={v}" for k, v in func["compiler_options"].items()]
                        )
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

    return "\n".join([imports, INITIAL, "\n".join(output)])


def write(
    path: str = "out.py",
    data: List[str] = None,
    config_path: str = None,
    format_code: bool = True,
) -> None:
    with open(path, "w") as f:
        f.write(data or read(config_path or DATA_PATH))

    if format_code:
        update_code_format("out.py")


if __name__ == "__main__":
    write()
