from typing import Tuple

from pybridge import Bridge

idk = Bridge()


@idk.js(path="./use.js")
async def hello(name: str = None, age: int = None) -> Tuple[str, int]: ...
