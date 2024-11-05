"""
This file contains the tests for the transpose function in the column_transposition module.
"""

from adfgvx.column_transposition import transpose

def test_transpose1():
    """
    Test the transpose function with a trivial example.
    :return:
    """
    text = "Hello, World!"
    key = (0,)
    expected = "Hello, World!"
    result = transpose(text, key)
    assert result == expected, f"Expected {expected} but got {result}"


def test_transpose2():
    """
    Test the transpose function with a simple example.
    :return:
    """
    text = "Hello, World!"
    key = (1, 0)
    expected = "el,WrdHlo ol!"
    result = transpose(text, key)
    assert result == expected, f"Expected {expected} but got {result}"


def test_transpose3():
    """
    Test the transpose function with an example from the lecture slides.
    :return:
    """
    text = "XAVGGDGDGFXGGXVDDDGVGDDFDXDXAXAXVGFDXGGGGXGVAX"
    key = "WISKUNDE"
    key = (7, 2, 5, 3, 6, 4, 0, 1)
    expected = "GVDAGDDFXGAFDXGXGGVXDVDXDXGXVXGDFGGGGAXAXGDDVG"
    result = transpose(text, key)
    assert result == expected, f"Expected {expected} but got {result}"