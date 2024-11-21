from {{cookiecutter.package_name}}.snippets.hash.file_hash import hash_file
import logging
from hashlib import md5
from pathlib import Path
from typing import Annotated

import typer

logger = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def hash_md5(
    ctx: typer.Context, path_in: Annotated[Path, typer.Argument(help="file to hash.")]
):
    """Print the md5 hash of a given file to the terminal."""
    hashcode = hash_file(path_in, md5())
    typer.echo(f"{hashcode}  {path_in.name}")
