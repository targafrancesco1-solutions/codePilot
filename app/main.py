from pathlib import Path

from scanner import find_source_files


def get_project_name():
    return "codePilot"


def main():
    extensions = {".java", ".py", ".md"}
    
    name = get_project_name()
    version = get_version()
    file_count = get_file_count()


    print(name)
    print("version: " + version)
    print("Files: " + str(file_count))
    print(find_source_files(Path("."),extensions))


def get_version() -> str:
    return "0.1"


def get_file_count() -> int:
    return 10





if __name__ == "__main__":
    main()
