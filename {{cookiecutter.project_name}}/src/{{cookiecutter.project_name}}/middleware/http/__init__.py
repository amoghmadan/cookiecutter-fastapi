from typing import Any, Awaitable, Callable, Coroutine

from fastapi import Request, Response

from {{cookiecutter.project_name}}.middleware.http.database import database_middleware
from {{cookiecutter.project_name}}.middleware.http.exception import exception_middleware

http: list[
    Callable[
        [Request, Callable[[Request], Awaitable[Response]]],
        Coroutine[Any, Any, Response],
    ]
] = [database_middleware, exception_middleware]

__all__ = ["http"]
