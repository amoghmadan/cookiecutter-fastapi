from sqlalchemy import Result, TextClause, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import DBSes
from app.schemas.response import Pong


async def pong(db: AsyncSession = DBSes) -> Pong:
    """Reply, Pong"""
    statement: TextClause = text("SELECT 'Pong' AS pong;")
    result: Result = await db.execute(statement)
    string: str = result.scalar_one()
    return Pong(reply=string)
