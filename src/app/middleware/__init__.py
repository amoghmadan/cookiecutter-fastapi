from typing import Any, Awaitable, Callable, Coroutine

from fastapi import Request, Response

from app.middleware.http import http

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
