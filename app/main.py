from pathlib import Path

import scanner


def get_project_name():
    return "codePilot"


def main():
    extensions = {".java", ".py", ".md"}
    
    name = get_project_name()
    version = get_version()


    print(name)
    print("version: " + version)
    files = scanner.find_source_files(Path("."),extensions)
    print(scanner.count_by_extension(files))


def get_version() -> str:
    return "0.1"




if __name__ == "__main__":
    main()
