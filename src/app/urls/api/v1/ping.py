from http import HTTPMethod, HTTPStatus

from fastapi import APIRouter

from app.views import pong

ping: APIRouter = APIRouter(prefix="/ping")
ping.add_api_route("/", pong, status_code=HTTPStatus.OK, methods=[HTTPMethod.GET])

__all__ = ["ping"]
