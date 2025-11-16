from pathlib import Path
from typing import List

import typer

from ingestion.scanner import find_source_files

app = typer.Typer(no_args_is_help=True, help="CLI for the AI chat agent.")

@app.callback()
def _root() -> None:
    """CLI for the AI chat agent."""
    return None

@app.command("scan-directory")
def scan(
    dir: str = typer.Argument(..., help="Directory to scan (ex ./data/raw)"),
    exts: List[str] = typer.Option(
        ["pdf"], "--ext", "-e", help='File extensions to include (ex -e pdf -e md). Use multiple -e flags for multiple extensions.'
    ),
):
    """
    Recursively scan for source files matching the given extensions and print them.
    """
    root_path = Path(dir).expanduser().resolve()
    if not root_path.exists():
        typer.echo(f"Root path does not exist: {root_path}")
        raise typer.Exit(code=1)

    matched_files = find_source_files(root_path, exts=exts)
    if not matched_files:
        typer.echo("No files found.")
        raise typer.Exit(code=0)

    for f in matched_files:
        typer.echo(str(f))


def main() -> None:
    app()


if __name__ == "__main__":
    main()
