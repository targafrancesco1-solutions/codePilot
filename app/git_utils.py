import subprocess
from pathlib import Path


def get_git_status(path: Path) -> str:
    
    result = subprocess.run(["git", "status", "--short"], cwd=path, capture_output=True, text=True, check=True)
    return result.stdout

def get_changed_files(path: Path) -> list[str]:
    result = subprocess.run(["git", "status", "--short"], cwd=path, capture_output=True, text=True, check=True)
    output = result.stdout.splitlines()
    for line in output:
        line = line[3:]
    return output
    
