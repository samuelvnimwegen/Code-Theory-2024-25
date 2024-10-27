"""
In this file, we have the filestream methods
"""


def load_file(file_path: str) -> str:
    """
    Loads the file's content and turns it into a string
    :param file_path: the file path
    :return: the file content in string format
    """
    with open(file_path, 'r') as file:
        return file.read()


