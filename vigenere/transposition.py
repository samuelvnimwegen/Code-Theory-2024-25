"""
This file is used to crack the column transposition of the vigenere+ cipher
"""
import math
from util import filestream
code: str = filestream.load_file("codes/01-OPGAVE-viginereplus.txt")


def get_column_length(text_length: int, key_length: int) -> int:
    """
    Get the length of the columns of the transposition
    :param text_length: the length of the text
    :param key_length: the length of the key
    :return: the length of the column
    """
    assert key_length > 0
    assert text_length > 0
    return math.ceil(text_length / key_length)


if __name__ == "__main__":
    values: int = math.factorial(10)
    for i in range(values):
        print(i)


