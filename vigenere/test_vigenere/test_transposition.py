"""
This file contains the tests for the transposition.py file
"""

from vigenere.transposition import (get_column_length, get_all_poss_columns, columns_to_text, permutate_columns,
                                    find_three_letter_patterns, solve_column_transposition)


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
    cipher = "123456"
    columns = get_all_poss_columns(cipher, 2)
    assert columns == [['123', '456'], ['456', '123']]

    cipher = "1234567"
    columns = get_all_poss_columns(cipher, 2)
    assert columns == [['1234', '567'], ['4567', '123']]

    cipher = "12345678"
    columns = get_all_poss_columns(cipher, 3)
    assert columns == [['123', '456', '78'], ['123', '678', '45'], ['456', '123', '78'],
                       ['678', '123', '45'], ['345', '678', '12'], ['678', '345', '12']]


def test_columns_to_text():
    """
    Test the columns to text method
    """
    cols = ['TSTEEICWIDRISDO', 'HATHLSTOWBYFWNR', 'ITOOLFIROESTOOK', 'SESWTUOKUVAHUT', 'ISEWHNNSLEDILW']
    text = columns_to_text(cols)
    assert text == "THISISATESTTOSEEHOWWELLTHISFUNCTIONWORKSIWOULDBEVERYSADIFTHISWOULDNOTWORK"


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


def test_column_transposition():
    """
    Test the column transposition method
    """
    text = "THISISATESTTOSEEHOWWELLTHISFUNCTIONWORKSIWOULDBEVERYSADIFTHISWOULDNOTWORK"

    # An example that has no permutation
    cipher = "TSTEEICWIDRISDOHATHLSTOWBYFWNRITOOLFIROESTOOKSESWTUOKUVAHUTISEWHNNSLEDILW"
    result = solve_column_transposition(cipher, 5)
    assert text in result

    # An example that has no permutation
    cipher = ("HEELNOURTLRSOWSOIEDWTISHTCRLYHDKSOWSOIEDWTISHTCRLYHDKASEFNWVIOWTTELUWOEFUOITWIISBASOHEELNOURTLRASEFNW"
              "VIOWSTOHTKDSINTTELUWOEFUOISHTCRLYHDKASEFNWVIOWSTOHTKDSINSTOHTKDSINTTELUWOEFUOITWIISBASOITWIISBASOHE"
              "ELNOURTLRSOWSOIEDWT")
    text = ("THISISATESTTOSEEHOWWELLTHISFUNCTIONWORKSIWOULDBEVERYSADIFTHISWOULDNOTWORKTHISISATESTTOSEEHOWWELLTHISFUN"
            "CTIONWORKSIWOULDBEVERYSADIFTHISWOULDNOTWORKTHISISATESTTOSEEHOWWELLTHISFUNCTIONWORKSIWOULDBEVERYSADI"
            "FTHISWOULDNOTWORK")
    result = solve_column_transposition(cipher, 7)
    assert text in result
