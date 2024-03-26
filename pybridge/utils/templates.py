FUNC_TEMPLATE = """
@idk.{format}(path="{path}"{compiler_options})
async def {name}({args}) -> {return_type}:{doc}
  ...
"""


IMPORTS = ["from typing import Any", "from pybridge import Bridge"]


INITIAL = """

idk = Bridge()

"""

OUTPUT = []
