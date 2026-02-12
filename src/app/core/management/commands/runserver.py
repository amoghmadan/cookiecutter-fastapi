import typer
import uvicorn

app = typer.Typer()


@app.command()
def runserver(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run server."""
    uvicorn.run("app.asgi:application", host=host, port=port, reload=True)
