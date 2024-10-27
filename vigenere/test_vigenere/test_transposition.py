"""
This file contains the tests for the transposition.py file
"""

from vigenere.transposition import (get_column_length, get_columns, columns_to_text, permutate_columns,
                                    find_three_letter_patterns)


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

    # Illegal pairs
    illegal_pairs = [(0, 0), (0, 1), (1, 0), (-1, 1), (1, -1)]
    for pair in illegal_pairs:
        try:
            get_column_length(pair[0], pair[1])
            assert False
        except AssertionError:
            assert True


def test_get_columns():
    """
    Test the get_columns method
    """
    # From example 1.7 p25 of the course book
    cols = get_columns("sendarmouredcartoheadquarters", 9)
    assert cols == ["srer", "eeas", "ndd*", "dcq*", "aau*", "rra*", "mtr*", "oot*", "uhe*"]


def test_columns_to_text():
    """
    Test the columns to text method
    """
    # From example 1.7 p25 of the course book
    cols = ["srer", "eeas", "ndd*", "dcq*", "aau*", "rra*", "mtr*", "oot*", "uhe*"]

    # Permute the columns
    permuted_cols = [cols[0], cols[2], cols[4], cols[1], cols[3], cols[5], cols[6], cols[8], cols[7]]

    text = columns_to_text(permuted_cols)
    assert text == "srernddaaueeasdcqrramtruheoot"


def test_permutate_columns():
    """
    Test the permutate columns method
    """
    cols = ["aaa", "bbb", "ccc"]
    perms = permutate_columns(cols)
    assert perms == [
        ["aaa", "bbb", "ccc"],
        ["aaa", "ccc", "bbb"],
        ["bbb", "aaa", "ccc"],
        ["bbb", "ccc", "aaa"],
        ["ccc", "aaa", "bbb"],
        ["ccc", "bbb", "aaa"]
    ]


def test_find_three_letter_patterns():
    """
    Test the find three letter patterns method
    """
    text = "abcabcabcabc"
    patterns = find_three_letter_patterns(text)
    assert patterns == {
        "abc": 4,
        "bca": 3,
        "cab": 3
    }
    text = "abcabcabcab"
    patterns = find_three_letter_patterns(text)
    assert patterns == {
        "abc": 3,
        "bca": 3,
        "cab": 3
    }
