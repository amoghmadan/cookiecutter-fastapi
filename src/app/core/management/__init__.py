import typer

from app.core.management.commands import commands

execute_from_command_line = typer.Typer()

for command in commands:
    execute_from_command_line.add_typer(command)


__all__ = ["execute_from_command_line"]
