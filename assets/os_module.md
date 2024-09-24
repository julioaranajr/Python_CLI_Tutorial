# OS Module in Python

The `os` module in Python provides a way of using operating system dependent functionality. The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.

## Importing the OS Module

To use the `os` module, you need to import it first. Here is how you can do it:

```python
import os
```

## Commonly Used Functions

Here are some of the commonly used functions in the `os` module:

### `os.name`

The `os.name` attribute provides the name of the operating system dependent module imported. The following are the possible values for `os.name`:

- `posix`: This value is returned on Unix-based operating systems like Linux and macOS.
- `nt`: This value is returned on Windows operating systems.

e.g.

```python
import os

print(os.name)
```

### `os.getcwd()`

The `os.getcwd()` function returns the current working directory of the Python script.

e.g.

```python
import os

print(os.getcwd())
```

### `os.chdir(path)`

The `os.chdir(path)` function changes the current working directory to the specified path.

e.g.

```python
import os

os.chdir('/path/to/directory')
```

### `os.listdir(path)`

The `os.listdir(path)` function returns a list of all the files and directories in the specified path.

e.g.

```python

import os

print(os.listdir('/path/to/directory'))
```

### `os.mkdir(path)`

The `os.mkdir(path)` function creates a new directory at the specified path.

e.g.

```python
import os

os.mkdir('/path/to/directory')
```

### `os.makedirs(path)`

The `os.makedirs(path)` function creates a new directory at the specified path, including any necessary parent directories.

e.g.

```python
import os

os.makedirs('/path/to/directory')
```

### `os.remove(path)`

The `os.remove(path)` function removes the file at the specified path.

e.g.

```python
import os

os.remove('/path/to/file')
```

### `os.rmdir(path)`

The `os.rmdir(path)` function removes the directory at the specified path.

e.g.

```python
import os

os.rmdir('/path/to/directory')
```

### `os.removedirs(path)`

The `os.removedirs(path)` function removes the directory at the specified path, including any parent directories if they are empty.

e.g.

```python
import os

os.removedirs('/path/to/directory')
```

### `os.rename(src, dst)`

The `os.rename(src, dst)` function renames the file or directory at the source path to the destination path.

e.g.

```python
import os

os.rename('/path/to/src', '/path/to/dst')
```

### `os.path.exists(path)`

The `os.path.exists(path)` function returns `True` if the file or directory at the specified path exists, and `False` otherwise.

e.g.

```python
import os

print(os.path.exists('/path/to/file'))
```

### `os.path.isfile(path)`

The `os.path.isfile(path)` function returns `True` if the path is a file, and `False` otherwise.

e.g.

```python
import os

print(os.path.isfile('/path/to/file'))
```

### `os.path.isdir(path)`

The `os.path.isdir(path)` function returns `True` if the path is a directory, and `False` otherwise.

e.g.

```python
import os

print(os.path.isdir('/path/to/directory'))
```

### `os.path.join(path1, path2, ...)`

The `os.path.join(path1, path2, ...)` function joins one or more path components intelligently. The function returns a new path string.

e.g.

```python
import os

path = os.path.join('/path/to', 'directory', 'file.txt')
print(path)
```

### `os.path.split(path)`

The `os.path.split(path)` function splits the path into a pair `(head, tail)` where `tail` is the last pathname component and `head` is everything leading up to that.

e.g.

```python
import os

head, tail = os.path.split('/path/to/file.txt')
print(head)
print(tail)
```

### `os.path.splitext(path)`

The `os.path.splitext(path)` function splits the path into a pair `(root, ext)` where `ext` is the extension and `root` is everything leading up to that.

e.g.

```python
import os

root, ext = os.path.splitext('/path/to/file.txt')
print(root)
print(ext)
```

### `os.path.basename(path)`

The `os.path.basename(path)` function returns the last component of the path.

e.g.

```python
import os

print(os.path.basename('/path/to/file.txt'))
```

### `os.path.dirname(path)`

The `os.path.dirname(path)` function returns the directory component of the path.

e.g.

```python
import os

print(os.path.dirname('/path/to/file.txt'))
```

### `os.path.abspath(path)`

The `os.path.abspath(path)` function returns the absolute path of the specified path.

e.g.

```python
import os

print(os.path.abspath('/path/to/file.txt'))
```

### `os.path.relpath(path, start)`

The `os.path.relpath(path, start)` function returns a relative path from the start path to the specified path.

e.g.

```python
import os

print(os.path.relpath('/path/to/file.txt', '/path/to'))
```

### `os.path.getsize(path)`

The `os.path.getsize(path)` function returns the size of the file at the specified path in bytes.

e.g.

```python
import os

print(os.path.getsize('/path/to/file.txt'))
```

### `os.path.getmtime(path)`

The `os.path.getmtime(path)` function returns the last modification time of the file at the specified path.

e.g.

```python
import os

print(os.path.getmtime('/path/to/file.txt'))
```

### `os.path.getctime(path)`

The `os.path.getctime(path)` function returns the creation time of the file at the specified path.

e.g.

```python
import os

print(os.path.getctime('/path/to/file.txt'))
```

### `os.linesep`

The `os.linesep` attribute provides the line separator used in text files. The following are the possible values for `os.linesep`:

- `\r`: This value is returned on Mac operating systems.
- `\n`: This value is returned on Unix-based operating systems like Linux and macOS.
- `\r\n`: This value is returned on Windows operating systems.

e.g.

```python
import os

print(os.linesep)
```

### `os.system(command)`

The `os.system(command)` function executes the command in a subshell.

e.g.

```python
import os

os.system('ls -la')

# or

os.system('mkdir files')
```

### `os.environ`

The `os.environ` attribute provides a mapping object representing the environment variables of the current process.

e.g.

```python
import os

print(os.environ)

#or

print(os.environ['HOME'])

```

### `os.getenv(key, default=None)`

The `os.getenv(key, default=None)` function returns the value of the environment variable with the specified key. If the key is not found, the function returns the default value.

e.g.

```python
import os

print(os.getenv('HOME'))

# or

print(os.environ['HOME'])
```

### `os.putenv(key, value)`

The `os.putenv(key, value)` function sets the value of the environment variable with the specified key.

e.g.

```python
import os

os.putenv('KEY', 'VALUE')

# or

os.environ['KEY'] = 'VALUE'
```

### `os.unsetenv(key)`

The `os.unsetenv(key)` function unsets the environment variable with the specified key.

e.g.

```python

import os

os.unsetenv('KEY')

# or

del os.environ['KEY']
```

# Example

Here is an example that demonstrates how to use the `os` module to list all the files and directories in the current working directory:

```python
import os

for item in os.listdir(os.getcwd()):
    print(item)
```

This will print the names of all the files and directories in the current working directory.
