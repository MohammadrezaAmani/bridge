import asyncio
from typing import Any, Tuple

from idkwhy import IdkWhy

idk = IdkWhy()


@idk.js(path="./use.js")
async def hello(name: str = None, age: int = None) -> Tuple[str, int]: ...


async def main():
    print(hello("John", 25))


asyncio.run(main())
