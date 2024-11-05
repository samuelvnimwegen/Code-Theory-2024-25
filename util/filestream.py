"""
This module contains the filestream utility functions
"""


def load(file_path: str) -> str:
    """
    Loads the file's content and turns it into a string

    :param file_path: the file path
    :return: the file content in string format
    """
    with open(file_path, 'r') as file:
        return file.read()