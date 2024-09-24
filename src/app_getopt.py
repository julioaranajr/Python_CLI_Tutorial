"""Getopt example script to create, delete, or list files and directories."""

import getopt
import os
import sys


def usage():
    """
    Display the usage information for the script.
    """
    print("Usage: app_getopt.py -c <create> -d <delete> -l <list> -h <help>")
    print("Options:")
    print("  -c, --create <path>   Create a file or directory at the specified path")
    print("  -d, --delete <path>   Delete a file or directory at the specified path")
    print(
        "  -l, --list <path>     List contents of the directory at the specified path"
    )
    print("  -h, --help            Display this help message")


def create_path(path):
    """
    Create a file or directory at the specified path.

    :param path: Path to create
    """
    if os.path.exists(path):
        print(f"Error: {path} already exists.")
    else:
        if path.endswith("/"):
            os.makedirs(path)
            print(f"Directory {path} created.")
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write("")
            print(f"File {path} created.")


def delete_path(path):
    """
    Delete a file or directory at the specified path.

    :param path: Path to delete
    """
    if not os.path.exists(path):
        print(f"Error: {path} does not exist.")
    else:
        if os.path.isdir(path):
            os.rmdir(path)
            print(f"Directory {path} deleted.")
        else:
            os.remove(path)
            print(f"File {path} deleted.")


def list_directory(path):
    """
    List contents of the directory at the specified path.

    :param path: Path to list
    """
    if not os.path.exists(path):
        print(f"Error: {path} does not exist.")
    elif not os.path.isdir(path):
        print(f"Error: {path} is not a directory.")
    else:
        for item in os.listdir(path):
            print(item)


def main(argv):
    """
    Main function to parse command line arguments and perform actions.

    :param argv: Command line arguments
    """
    try:
        opts, args = getopt.getopt(
            argv, "hc:d:l:", ["help", "create=", "delete=", "list="]
        )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-c", "--create"):
            create_path(arg)
        elif opt in ("-d", "--delete"):
            delete_path(arg)
        elif opt in ("-l", "--list"):
            list_directory(arg)
        else:
            print("Invalid option.")
            usage()
            sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
