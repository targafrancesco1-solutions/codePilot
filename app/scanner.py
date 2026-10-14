from pathlib import Path


def find_source_files(
                      path: Path,
                      extensions : set[str]
                      ) -> list[str]:
    source_files: list[str] = []
    ignored_dirs = {".venv", ".git", "__pycache__", "node_modules"}
    for file in path.rglob("*"):
        if any(part in ignored_dirs for part in file.parts):
            continue

        if file.is_file() and file.suffix in extensions:
            source_files.append(str(file.relative_to(path)))

    return source_files