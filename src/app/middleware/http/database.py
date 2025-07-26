from typing import Awaitable, Callable

from fastapi import Request, Response

from app.dependencies.session_maker import AliasedSessionMaker


async def database_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """
    Database Middleware
    :param request: Request
    :param call_next: Callable[[Request], Awaitable[Response]]
    :return: Response
    """
    aliased_session_maker = AliasedSessionMaker()
    session_class = aliased_session_maker(request)
    async with session_class() as session:
        request.state.db = session
        response = await call_next(request)
    return response
