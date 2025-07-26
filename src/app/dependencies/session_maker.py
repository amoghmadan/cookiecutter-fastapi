from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db import DEFAULT_DB_ALIAS


class AliasedSessionMaker:
    """Aliased: Session Maker"""

    def __init__(self: "AliasedSessionMaker", alias: str = DEFAULT_DB_ALIAS) -> None:
        """
        Set alias to be used as key for getting the async session maker.
        :param alias: str
        """
        self._alias = alias

    def __repr__(self: "AliasedSessionMaker") -> str:
        """
        Representation of the class' instance.
        :return: str
        """
        return "<%s %r>" % (self.__class__.__name__, self._alias)

    def __call__(
        self: "AliasedSessionMaker", request: Request
    ) -> async_sessionmaker[AsyncSession]:
        """
        User "fastapi.Depends" class and pass this object to access session maker class.
        :param request: Request
        :return: AsyncSession
        """
        assert self._alias in request.app.state.sessions, (  # nosec: B101
            "%r database not configured properly."
            "Did you forget to specify %r in the DATABASES settings?"
        ) % (self._alias, self._alias)
        return request.app.state.sessions[self._alias]
