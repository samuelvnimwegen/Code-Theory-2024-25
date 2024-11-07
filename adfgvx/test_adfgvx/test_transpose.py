"""
This file contains the tests for the transpose function in the column_transposition module.
"""

from adfgvx.column_transposition import reverse_transpose

def test_transpose1():
    """
    Test the transpose function with a trivial example.
    :return:
    """
    original_text = "Hello, World!"
    key = (0,)
    after_transpose = "Hello, World!"
    result = reverse_transpose(original_text, key)
    assert result == after_transpose, f"Expected {after_transpose} but got {result}"


def test_transpose2():
    """
    Test the transpose function with a simple example.
    :return:
    """
    original_text = "Hello, World!"
    key = (1, 0, 2)
    # _ substitutes a space
    # 1 0 2 -> 0 1 2
    # H e l -> e H l
    # l o , -> o l ,
    # _ W o -> W _ o
    # r l d -> l r d
    # !     ->   !
    # ==> eoWlHl r!l,od
    after_transpose = "eoWlHl r!l,od"
    result = reverse_transpose(after_transpose, key)
    assert result == original_text, f"Expected {original_text} but got {result}"


def test_transpose3():
    """
    Test the transpose function with an example from the lecture slides.
    :return:
    """
    after_transpose = "GVDAGDDFXGAFDXGXGGVXDVDXDXGXVXGDFGGGGAXAXGDDVG"
    # key = "WISKUNDE"
    key = (7, 2, 5, 3, 6, 4, 0, 1)
    original_text = "XAVGGDGDGFXGGXVDDDGVGDDFDXDXAXAXVGFDXGGGGXGVAX"
    result = reverse_transpose(after_transpose, key)
    assert result == original_text, f"Expected {original_text} but got {result}"


def test_transpose4():
    """
    Test the transpose function with an example from the lecture slides.
    :return:
    """
    # Expected gotten from https://www.boxentriq.com/code-breaking/columnar-transposition-cipher
    # original_text is just random letters from ["A", "D", "F", "G", "V", "X"]
    after_transpose = "DAAVAFFXFAVDVAGFFGXGFAADDXDFFDXAGFGAXVVDDFAGVXDFFDXGVGFXAXVAVGXGDAXFAVDVDXAVVVXFGGVFAADFDXADFGFDVVVGDFFVDGXAVGGXDAXVFXVFXDVDXAXAXAGAGGAAXXXGXXVDXXDXDDVFFDFDFAXVDAVXDDXAVGAXDAGDAAVVFFDGFVAAVDAVAAVFFFAF"
    # key = "TESTKEY"
    key = (4, 0, 3, 5, 2, 1, 6)
    original_text = "XDADXDDVADXVXAFAFXAAGXVDDVGDVAXXGFAFFADXGAXFDDGAVDXFVDXVVFGFAVFDAFFXVFXVDDFDDADVFADGXVVDVFFAAVFDAVXGGAVGAAFDXDVAGFFVXXVAGFDADDGXVAVFAGGDVVFVAFGXVDAAAXDXXAXAADFGVXDVXGVFXDGAGGFGXGVVFFXDXGFXAXFDAAAFVFAX"
    result = reverse_transpose(after_transpose, key)
    assert result == original_text, f"Expected {original_text} but got {result}"