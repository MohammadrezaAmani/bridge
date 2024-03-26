import asyncio
from typing import Any, Tuple

from idkwhy import IdkWhy

idk = IdkWhy()


@idk.js(path="./script.js")
async def hello(name: str = None, age: int = None) -> Tuple[str, int]: ...


async def main():
    print(hello("John", 25))


import time

start = time.time()
asyncio.run(main())

print(time.time() - start)
