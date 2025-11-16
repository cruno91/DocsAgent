from pathlib import Path
from typing import Iterable, List


def find_source_files(
    root: Path,
    exts: Iterable[str] = ("pdf",),
) -> List[Path]:
    """
    Recursively find files under `root` with given extensions.

    Returns absolute Paths.
    """
    # Normalize extensions to lowercase and remove leading dots.
    normalized_exts = {e.lower().lstrip(".") for e in exts}
    results: List[Path] = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower().lstrip(".")
        if suffix in normalized_exts:
            results.append(path.resolve())

    return sorted(results)
