from typing import Any, Awaitable, Callable, Coroutine

from fastapi import Request, Response

from {{cookiecutter.project_name}}.middleware.http import http

middlewares: dict[
    str,
    list[
        Callable[
            [Request, Callable[[Request], Awaitable[Response]]],
            Coroutine[Any, Any, Response],
        ]
    ],
] = {"http": http}

__all__ = ["middlewares"]
