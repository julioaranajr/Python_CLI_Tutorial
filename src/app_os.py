"""OS module functions."""

import os


def create_directory(path):
    """
    Create a directory if it doesn't exist.

    :param path: Path of the directory to create.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        return f"Directory '{path}' created."
    else:
        return f"Directory '{path}' already exists."


def delete_directory(path):
    """
    Delete a directory if it exists.

    :param path: Path of the directory to delete.
    """
    if os.path.exists(path):
        os.rmdir(path)
        return f"Directory '{path}' deleted."
    else:
        return f"Directory '{path}' does not exist."


def list_directory(path):
    """
    List the contents of a directory.

    :param path: Path of the directory to list.
    """
    if os.path.exists(path):
        return os.listdir(path)
    else:
        return f"Directory '{path}' does not exist."


def create_file(path):
    """
    Create a file if it doesn't exist.

    :param path: Path of the file to create.
    """
    if not os.path.exists(path):
        with open(path, "w") as file:
            file.write("")
        return f"File '{path}' created."
    else:
        return f"File '{path}' already exists."


def delete_file(path):
    """
    Delete a file if it exists.

    :param path: Path of the file to delete.
    """
    if os.path.exists(path):
        os.remove(path)
        return f"File '{path}' deleted."
    else:
        return f"File '{path}' does not exist."


def help():
    """
    Display the help message.

    Available functions:
    - create_directory(path): Create a directory if it doesn't exist.
    - delete_directory(path): Delete a directory if it exists.
    - list_directory(path): List the contents of a directory.
    - create_file(path): Create a file if it doesn't exist.
    - delete_file(path): Delete a file if it exists.
    """
    return help.__doc__


if __name__ == "__main__":
    print(create_directory("test"))
    print(create_directory("test"))
    print(delete_directory("test"))
    print(delete_directory("test"))
    print(list_directory("test"))
    print(create_file("test.txt"))
    print(create_file("test.txt"))
    print(delete_file("test.txt"))
    print(delete_file("test.txt"))
    print(list_directory("test"))
    print(help())
