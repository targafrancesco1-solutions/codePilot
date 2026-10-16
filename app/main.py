import sys
from pathlib import Path

import scanner


def get_project_name():
    return "codePilot"


def main():
    extensions = {".java", ".py", ".md"}
    
    name = get_project_name()
    version = get_version()

    project_path = Path(sys.argv[1])
    print(name)
    print("version: " + version)
    validate_path(project_path)
    files = scanner.find_source_files(project_path,extensions)
    print(scanner.count_by_extension(files))


def get_version() -> str:
    return "0.1"

def validate_path(path : Path):
    if Path.exists(path):
        if(path.is_dir()):
            print("The path exists correctly on your machine, let's analyze the files now.")
        else:
            print("the path must be a directory and not a file, Shutting down...")
            sys.exit(1)
    else:
        print("The following path: " + str(path) + " does not exist on your machine. Shutting down....")
        sys.exit(1)
        





if __name__ == "__main__":
    main()
