"""Command-line interface."""

import datetime
import logging
from pathlib import Path
from time import perf_counter_ns
from typing import Annotated

from {{ cookiecutter.package_name }}.cli import hash_file_cli
import typer

logger = logging.getLogger(__name__)

APP_NAME = "{{ cookiecutter.project_name }}"


def app_dir() -> Path:
    """Get the system approiate application directory.

    Returns:
        _type_: The app dir.
    """
    return Path(typer.get_app_dir(app_name=APP_NAME))


def default_options(
    ctx: typer.Context,
    debug: Annotated[bool, typer.Option(help="Enable debug output.")] = False,
    verbosity: Annotated[int, typer.Option("-v", help="Verbosity.", count=True)] = 1,
):
    """Describe what your app does here."""
    ctx.ensure_object(dict)
    ctx.obj["START_TIME"] = perf_counter_ns()
    ctx.obj["DEBUG"] = debug
    ctx.obj["VERBOSITY"] = verbosity
    if ctx.obj["VERBOSITY"] >= 3:
        typer.echo(f"Verbosity: {ctx.obj["VERBOSITY"]}")
        typer.echo(f"Debug: {ctx.obj["DEBUG"]}")
        dt = datetime.datetime.now(datetime.UTC)
        formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S.%fZ")
        typer.echo(f"Started at: {formatted_time}")


app = typer.Typer(callback=default_options)
app.add_typer(hash_file_cli.app)


@app.command()
def hello(
    ctx: typer.Context, name: Annotated[str, typer.Argument(help="Name to greet.")]
):
    """An example of a command, prints a greeting."""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
