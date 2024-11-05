"""
This file contains the tests for the decode function in the decode_morse module.
"""

from adfgvx.decode_morse import decode

def test_decode1():
    """
    Test the decode function with every supported character.
    :return:
    """
    code = ".-/-../..-./--./...-/-..-"
    expected = 'ADFGVX'
    result = decode(code)
    assert result == expected, f"Expected {expected} but got {result}"


def test_decode2():
    """
    Test the decode function with an unsupported (' ') seperator.
    :return:
    """
    code = ".- -.."
    try:
        result = decode(code)
        assert False, f"Expected an AssertionError but got {result}"
    except AssertionError:
        pass


def test_decode3():
    """
    Test the decode function with an unsupported ('.') character.
    :return:
    """
    code = ".-/-../..-./--./...-/-..-/./-.."
    try:
        result = decode(code)
        assert False, f"Expected an AssertionError but got {result}"
    except AssertionError:
        pass