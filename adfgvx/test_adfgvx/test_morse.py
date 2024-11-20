"""
This file contains the tests for the decode function in the decode_morse module.
"""

from adfgvx.morse import decode, encode

def test_morse1():
    """
    Test the decode function with every supported character.
    :return:
    """
    code = ".-/-../..-./--./...-/-..-"
    expected = 'ADFGVX'
    result = decode(code)
    assert result == expected, f"Expected {expected} but got {result}"
    result = encode(expected)
    assert result == code, f"Expected {code} but got {result}"


def test_morse2():
    """
    Test the decode function with an unsupported (' ') seperator.
    :return:
    """
    code = ".- -.."
    try:
        result = decode(code)
    except AssertionError:
        return
    assert False, f"Expected an AssertionError but got {result}"


def test_morse3():
    """
    Test the decode function with an unsupported ('.') character.
    :return:
    """
    code = ".-/-../..-./--./...-/-..-/./-.."
    try:
        result = decode(code)
    except AssertionError:
        return
    assert False, f"Expected an AssertionError but got {result}"
