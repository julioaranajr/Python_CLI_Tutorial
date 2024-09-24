"""CMD CLI application with basic file and directory management commands."""

import cmd
import os


class PythonCLI(cmd.Cmd):
    """CMD CLI Class with basic file and directory management commands."""

    prompt = "Python CLI >>"
    intro = 'Welcome to Python CLI. Type "help" for available commands.'

    def __init__(self):
        """Initialize the PythonCLI class."""
        super().__init__()
        self.current_directory = os.getcwd()

    def do_clear(self, line):
        """Clear the screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def do_list(self, line):
        """List files and directories in the current directory."""
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)

    def do_create_dir(self, directory):
        """Create a new directory in the current directory."""
        new_dir = os.path.join(self.current_directory, directory)
        try:
            os.mkdir(new_dir)
            print(f"Directory '{directory}' created in {self.current_directory}")
        except Exception as e:
            print(f"Error: {e}")

    def do_change_dir(self, directory):
        """Change the current directory."""
        new_dir = os.path.join(self.current_directory, directory)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_directory = new_dir
            print(f"Current directory changed to {self.current_directory}")
        else:
            print(f"Directory '{directory}' does not exist.")

    def do_create_file(self, filename):
        """Create a new text file in the current directory."""
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, "w", encoding="utf-8") as new_file:
                print(f"File '{filename}' created in {self.current_directory}")
        except Exception as e:
            print(f"Error: {e}")

    def do_write_file(self, line):
        """Write to an existing text file in the current directory."""
        filename, content = line.split(" ", 1)
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, "a") as existing_file:
                existing_file.write(content + "\n")
                print(f"Content written to '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_read_file(self, filename):
        """Read the contents of a text file in the current directory."""
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, "r") as existing_file:
                print(existing_file.read())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_file(self, filename):
        """Delete a file in the current directory."""
        file_path = os.path.join(self.current_directory, filename)
        try:
            os.remove(file_path)
            print(f"File '{filename}' deleted from {self.current_directory}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_parent_dir(self, line):
        """Move to the parent directory."""
        self.current_directory = os.path.dirname(self.current_directory)
        print(f"Current directory changed to {self.current_directory}")

    def do_add_path(self, path):
        """Add a path to the current directory."""
        new_path = os.path.join(self.current_directory, path)
        if os.path.exists(new_path):
            self.current_directory = new_path
            print(f"Current directory changed to {self.current_directory}")
        else:
            print(f"Path '{path}' does not exist.")

    def do_show_path(self, line):
        """Display the current directory path."""
        print(self.current_directory)

    def do_keyword_search(self, keyword):
        """Search for files and directories containing a keyword."""
        matches = []
        for root, dirs, files in os.walk(self.current_directory):
            for file in files:
                if keyword in file:
                    matches.append(os.path.join(root, file))
            for directory in dirs:
                if keyword in directory:
                    matches.append(os.path.join(root, directory))
        if matches:
            for match in matches:
                print(match)
        else:
            print(f"No files or directories found containing '{keyword}'")

    def do_sys_version(self, line):
        """Display the Python version."""
        print(f"Python {sys.version}")

    def do_os_version(self, line):
        """Display the OS version."""
        print(f"OS: {os.name}")

    def do_os_info(self, line):
        """Display information about the operating system."""
        print(f"OS: {os.name}")
        print(f"OS Release: {os.uname().release}")
        print(f"OS Version: {os.uname().version}")
        print(f"OS Machine: {os.uname().machine}")
        print(f"OS System: {os.uname().sysname}")
        print(f"OS Node: {os.uname().nodename}")

    def do_neofetch(self, line):
        """Display system information using Neofetch."""
        os.system("neofetch")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    def do_help(self, line):
        """Display available commands with 'help' or detailed help with 'help <cmd>'."""
        super().do_help(line)

    def postcmd(self, stop, line):
        print()  # Add an empty line for better readability
        return stop


if __name__ == "__main__":
    PythonCLI().cmdloop()
