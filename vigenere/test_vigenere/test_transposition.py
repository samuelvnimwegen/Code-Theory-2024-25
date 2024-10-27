"""
This file contains the tests for the transposition.py file
"""

from vigenere.transposition import get_column_length


def test_get_column_length():
    """
    Test the get column length method
    """
    # Legal pairs
    assert get_column_length(10, 5) == 2
    assert get_column_length(10, 3) == 4
    assert get_column_length(10, 2) == 5
    assert get_column_length(10, 1) == 10
    assert get_column_length(10, 10) == 1
    assert get_column_length(10, 11) == 1
    assert get_column_length(1, 1) == 1
    assert get_column_length(1, 2) == 1
    assert get_column_length(2, 1) == 2
    assert get_column_length(2, 2) == 1
    assert get_column_length(2, 3) == 1
    assert get_column_length(3, 2) == 2
    assert get_column_length(3, 3) == 1
    assert get_column_length(3, 4) == 1
    assert get_column_length(4, 3) == 2
    assert get_column_length(4, 4) == 1
    assert get_column_length(4, 5) == 1
    assert get_column_length(5, 4) == 2
    assert get_column_length(5, 5) == 1
    assert get_column_length(5, 6) == 1
    assert get_column_length(6, 5) == 2
    assert get_column_length(6, 6) == 1
    assert get_column_length(6, 7) == 1
    assert get_column_length(7, 6) == 2
    assert get_column_length(7, 7) == 1
    assert get_column_length(7, 8) == 1
    assert get_column_length(8, 7) == 2
    assert get_column_length(8, 8) == 1

    illegal_pairs = [(0, 0), (0, 1), (1, 0), (-1, 1), (1, -1)]
    for pair in illegal_pairs:
        try:
            get_column_length(pair[0], pair[1])
            assert False
        except AssertionError:
            assert True
