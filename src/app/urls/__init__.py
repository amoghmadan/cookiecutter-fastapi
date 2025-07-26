from fastapi import APIRouter

from app.urls.api import api

urlpatterns: list[APIRouter] = [api]

__all__ = ["urlpatterns"]
