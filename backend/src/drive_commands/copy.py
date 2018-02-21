"""
Copy a file or folder from source into the specified targets.
"""


def file(data):
    """
    Copy the file into targets.

    Should maintain permissions and file metadata.
    """
    raise NotImplementedError


def folder(data):
    """
    Copy the whole folder recursively into targets.
    """
    raise NotImplementedError
