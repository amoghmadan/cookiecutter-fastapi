from fastapi import FastAPI

from {{cookiecutter.project_name}}.conf import settings
from {{cookiecutter.project_name}}.middleware import middlewares
from {{cookiecutter.project_name}}.urls import urlpatterns
from {{cookiecutter.project_name}}.utils.lifespan import lifespan


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
