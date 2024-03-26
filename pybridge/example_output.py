import asyncio
from typing import Any, Tuple

from pybridge.bridge import Bridge

idk = Bridge()


@idk.js(path="./script.js")
async def hello(name: str = None, age: int = None) -> Tuple[str, int]: ...
