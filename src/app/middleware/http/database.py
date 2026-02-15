from typing import Awaitable, Callable

from fastapi import Request, Response

from app.db import DEFAULT_DB_ALIAS


async def database_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """
    Database Middleware
    :param request: Request
    :param call_next: Callable[[Request], Awaitable[Response]]
    :return: Response
    """
    session_class = request.app.state.sessions[DEFAULT_DB_ALIAS]
    async with session_class() as session:
        request.state.db = session
        response = await call_next(request)
    return response
