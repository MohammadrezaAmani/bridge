from typing import Any


class Function:
    def __init__(
        self,
        path: str,
        compiler_options: str,
        name: str,
        args: str,
        return_type: str,
        doc: str,
        return_value: str,
    ) -> None:
        self.path = path
        self.compiler_options = compiler_options
        self.name = name
        self.args = args
        self.return_type = return_type
        self.doc = doc
        self.return_value = return_value

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return f"Function {self.name} called with {args} and {kwds}"


class IdkWhy:
    def __init__(self) -> None: ...

    def js(self, path: str = None, compiler_options: str = None, *args, **kwargs):
        def decorator(func):
            func = Function(
                path=path,
                compiler_options=compiler_options,
                name=func.__name__,
                args=args,
                return_type=func.__annotations__["return"],
                doc=func.__doc__,
                return_value=func.__code__.co_varnames,
            )
            return func

        return decorator
