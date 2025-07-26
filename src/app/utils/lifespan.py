from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.db import engines, sessions


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncGenerator:
    """
    Lifespan for FastAPI application.
    :param application: FastAPI
    :return: AsyncGenerator
    """
    application.state.engines = engines
    application.state.sessions = sessions
    yield
