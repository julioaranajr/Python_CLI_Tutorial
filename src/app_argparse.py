"""Module to demonstrate file and directory manipulation using argparse."""

import argparse
import os


def create_directory(path):
    """
    Create a directory if it doesn't exist.

    Args:
        path (str): The path of the directory to create.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created.")
    else:
        print(f"Directory '{path}' already exists.")


def create_file(path, content=""):
    """
    Create a file with the given content.

    Args:
        path (str): The path of the file to create.
        content (str): The content to write to the file.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    if content:
        print(f"File '{path}' created with content: {content}")
    else:
        print(f"File '{path}' created.")


def list_directory(path):
    """
    List the contents of a directory.

    Args:
        path (str): The path of the directory to list.
    """
    if os.path.exists(path):
        print(f"Contents of directory '{path}':")
        for item in os.listdir(path):
            print(item)
    else:
        print(f"Directory '{path}' does not exist.")


def delete_file(path):
    """
    Delete a file.

    Args:
        path (str): The path of the file to delete.
    """
    if os.path.exists(path):
        os.remove(path)
        print(f"File '{path}' deleted.")
    else:
        print(f"File '{path}' does not exist.")


def main():
    parser = argparse.ArgumentParser(
        description="File and Directory Manipulation Script using argparse",
    )
    parser.add_argument("--create-dir", type=str, help="Create a directory")
    parser.add_argument("--create-file", type=str, help="Create a file")
    parser.add_argument("--file-content", type=str, help="Content for the file")
    parser.add_argument("--list-dir", type=str, help="List contents of a directory")
    parser.add_argument("--delete-file", type=str, help="Delete a file")

    args = parser.parse_args()

    if args.create_dir:
        create_directory(args.create_dir)
    if args.create_file:
        create_file(args.create_file, args.file_content if args.file_content else "")
    if args.list_dir:
        list_directory(args.list_dir)
    if args.delete_file:
        delete_file(args.delete_file)


if __name__ == "__main__":
    main()
