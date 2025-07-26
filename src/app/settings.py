"""
Settings for app project.
"""

from pathlib import Path

from app.__version__ import __version__

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).parent.parent
LOG_DIR = BASE_DIR.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")uki4xv@9e!b2^rax@qfcmp5#=^^*ziemm^tl1jv+f2nf9e#)$"  # nosec: B105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
ASGI_APPLICATION = "app.asgi.application"

# Database settings
DATABASES = {
    "default": {
        "url": "sqlite+aiosqlite:///db.sqlite3",
    }
}

# Internationalization
TIME_ZONE = "UTC"
USE_TZ = True

# OpenAPI settings
OPENAPI = {
    "title": "App Title",
    "summary": "App Summary.",
    "description": "App as a base for new projects.",
    "version": __version__,
    "openapi_url": "/schema/" if DEBUG else None,
    "docs_url": "/schema/swagger/" if DEBUG else None,
    "redoc_url": "/schema/redoc/" if DEBUG else None,
    "license": {
        "name": "MIT",
    },
}


# Logging config
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  # noqa: E501
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "debug.log",
            "formatter": "verbose",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 15,
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
