from fastapi import FastAPI


def get_asgi_application() -> FastAPI:
    """
    Generate and configure FastAPI ASGI consumable application.
    :return: FastAPI
    """
    from app.core.handlers.asgi import ASGIHandler

    return ASGIHandler()
