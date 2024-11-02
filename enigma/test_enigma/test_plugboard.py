"""
This file contains the tests for the plugboard.py file
"""

from enigma.plugboard import Plugboard


def test_get_corresponding_letter():
    """
    Test the get_corresponding_letter method
    """
    # Test with a simple example
    plugboard = Plugboard([("A", "B"), ("C", "D")])
    assert plugboard.get_corresponding_letter("A") == "B"
    assert plugboard.get_corresponding_letter("B") == "A"
    assert plugboard.get_corresponding_letter("C") == "D"
    assert plugboard.get_corresponding_letter("D") == "C"

    # Test with a more complex example
    plugboard = Plugboard([("A", "B"), ("C", "D"), ("E", "F"), ("G", "H")])
    assert plugboard.get_corresponding_letter("A") == "B"
    assert plugboard.get_corresponding_letter("B") == "A"
    assert plugboard.get_corresponding_letter("C") == "D"
    assert plugboard.get_corresponding_letter("D") == "C"
    assert plugboard.get_corresponding_letter("E") == "F"
    assert plugboard.get_corresponding_letter("F") == "E"
    assert plugboard.get_corresponding_letter("G") == "H"
    assert plugboard.get_corresponding_letter("H") == "G"
    assert plugboard.get_corresponding_letter("I") == "I"
    assert plugboard.get_corresponding_letter("J") == "J"
    assert plugboard.get_corresponding_letter("K") == "K"
    assert plugboard.get_corresponding_letter("L") == "L"
    assert plugboard.get_corresponding_letter("M") == "M"
    assert plugboard.get_corresponding_letter("N") == "N"
    assert plugboard.get_corresponding_letter("O") == "O"
    assert plugboard.get_corresponding_letter("P") == "P"
    assert plugboard.get_corresponding_letter("Q") == "Q"
    assert plugboard.get_corresponding_letter("R") == "R"
    assert plugboard.get_corresponding_letter("S") == "S"
    assert plugboard.get_corresponding_letter("T") == "T"
    assert plugboard.get_corresponding_letter("U") == "U"
