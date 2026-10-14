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

def count_by_extension(files: list[str]) -> dict[str, int]:
    count_result : dict[str,int] = {}

    for file in files:
        if(Path(file).suffix in count_result):
            count_result[Path(file).suffix] += 1
        else:
            count_result[Path(file).suffix] = 1
    return count_result
