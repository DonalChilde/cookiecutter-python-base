from time import perf_counter_ns

import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.callback()
def cli(
    ctx: typer.Context,
    debug: Annotated[bool, typer.Option(help="Enable debug output.")] = False,
    verbosity: Annotated[int, typer.Option("-v", help="Verbosity.", count=True)] = 1,
):
    """Extract text from pdf files."""

    ctx.ensure_object(dict)
    ctx.obj["START_TIME"] = perf_counter_ns()
    ctx.obj["DEBUG"] = debug
    typer.echo(f"Verbosity: {verbosity}")
    ctx.obj["VERBOSITY"] = verbosity




if __name__ == "__main__":
    app()
