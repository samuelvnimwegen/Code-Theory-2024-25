"""
This module contains the filestream utility functions
"""

import os


def load(file_path: str) -> str:
    """
    Loads the file's content and turns it into a string

    :param file_path: the file path
    :return: the file content in string format
    """
    with open(file_path, 'r') as file:
        return file.read()


def count_files_in_directory(directory_path) -> int:
    """
    Count the number of files in a directory.
    :param directory_path: The path to the directory.
    :return: The number of files in the directory
    """
    try:
        return len([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])
    except FileNotFoundError:
        return "Directory not found"
    except PermissionError:
        return "Permission denied"
