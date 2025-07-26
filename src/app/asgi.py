"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

from app.core.asgi import get_asgi_application

os.environ.setdefault("SETTINGS_MODULE", "app.settings")

application = get_asgi_application()
