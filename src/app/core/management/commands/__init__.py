from typer import Typer

from app.core.management.commands import loaddata, runserver, shell

commands: list[Typer] = [loaddata.cli, runserver.cli, shell.cli]

__all__ = ["commands"]
