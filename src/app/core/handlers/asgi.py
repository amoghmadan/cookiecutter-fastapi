from fastapi import FastAPI

from app.conf import settings
from app.middleware import middlewares
from app.urls import urlpatterns
from app.utils.lifespan import lifespan


class ASGIHandler:
    """Handler for ASGI requests."""

    def __new__(cls: type) -> FastAPI:
        application: FastAPI = FastAPI(
            debug=settings.DEBUG,
            lifespan=lifespan,
            **settings.OPENAPI,
        )

        for protocol in middlewares:  # Register middlewares
            for middleware in middlewares[protocol]:
                application.middleware(protocol)(middleware)

        for router in urlpatterns:  # Register routers
            application.include_router(router)

        return application
