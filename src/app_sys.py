"""System module for creating, listing, and deleting files and directories."""

import os
import sys


def create_file(file_path):
    """Create a file at the specified path."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("This is a test file.")
    print(f"File created at {file_path}")


def create_directory(directory_path):
    """Create a directory at the specified path."""
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory created at {directory_path}")


def list_directory(directory_path):
    """List the contents of the specified directory."""
    if os.path.exists(directory_path):
        print(f"Contents of {directory_path}:")
        for item in os.listdir(directory_path):
            print(item)
    else:
        print(f"Directory {directory_path} does not exist.")


def delete_path(path):
    """Delete the specified file or directory."""
    if os.path.isfile(path):
        os.remove(path)
        print(f"File {path} deleted.")
    elif os.path.isdir(path):
        os.rmdir(path)
        print(f"Directory {path} deleted.")
    else:
        print(f"Path {path} does not exist.")


def print_help():
    """Print the help message."""
    help_message = """
    Usage: python app_sys.py <command> <path>

    Commands:
    create_file <file_path>       Create a file at the specified path.
    create_directory <dir_path>   Create a directory at the specified path.
    list_directory <dir_path>     List the contents of the specified directory.
    delete_path <path>            Delete the specified file or directory.
    help                          Print this help message.
    """
    print(help_message)


def main():
    """Parse command line arguments and call the appropriate function."""
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "help":
        print_help()
    elif len(sys.argv) < 3:
        print("Error: Path not specified.")
        print_help()
        sys.exit(1)
    else:
        path = sys.argv[2]
        if command == "create_file":
            create_file(path)
        elif command == "create_directory":
            create_directory(path)
        elif command == "list_directory":
            list_directory(path)
        elif command == "delete_path":
            delete_path(path)
        else:
            print(f"Unknown command: {command}")
            print_help()


if __name__ == "__main__":
    main()
