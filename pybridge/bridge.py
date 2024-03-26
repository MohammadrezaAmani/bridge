from typing import Any
from shared_memory import (
    create_shared_memory,
    read_from_shared_memory,
    write_to_shared_memory,
)
import time
import uuid
import orjson as json
import subprocess

shard_memory = create_shared_memory()


class Function:
    def __init__(
        self,
        path: str,
        compiler_options: str,
        name: str,
        return_type: str,
    ) -> None:
        self.path = path
        self.compiler_options = compiler_options
        self.name = name
        self.return_type = return_type

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        id = str(uuid.uuid4())
        write_to_shared_memory(
            shard_memory,
            json.dumps(
                {
                    "op": "call",
                    "uuid": id,
                    "args": args,
                    "path": self.path,
                    "name": self.name,
                }
            ),
        )
        subprocess.call(["node", "use2.js"])
        while True:
            data = read_from_shared_memory(shard_memory)
            data = json.loads(data)
            if data["uuid"] == id and data["op"] == "response":
                return data["result"]


class Bridge:
    def __init__(self) -> None: ...

    def js(self, path: str = None, compiler_options: str = None, *args, **kwargs):
        def decorator(func):
            func = Function(
                path=path,
                compiler_options=compiler_options,
                name=func.__name__,
                return_type=func.__annotations__["return"],
            )
            return func

        return decorator
