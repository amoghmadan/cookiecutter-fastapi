from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db.engines import engines

sessions: dict[str, async_sessionmaker[AsyncSession]] = {
    alias: async_sessionmaker(engine, expire_on_commit=True, autocommit=False)
    for alias, engine in engines.items()
}
