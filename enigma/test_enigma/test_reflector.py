"""
This file contains the tests for the reflector.py file
"""

from enigma.reflector import Reflector


def test_get_reflector_letter():
    """
    Test the get_reflector_letter method
    """
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    assert reflector.get_reflector_letter("A") == "Y"
    assert reflector.get_reflector_letter("B") == "R"
    assert reflector.get_reflector_letter("C") == "U"
    assert reflector.get_reflector_letter("Y") == "A"

    # Check for all letters that the reflector is symmetric
    for i in range(26):
        letter = chr(i + 65)
        assert reflector.get_reflector_letter(reflector.get_reflector_letter(letter)) == letter
