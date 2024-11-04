"""
This file contains the tests for the rotor_wheel.py file
"""

from enigma.rotor_wheel import RotorWheel


def test_get_letter():
    """
    Test the get_letter method
    """
    # Tests with the default rotor wheel that does no operation (and does not change per rotation)
    rotor_wheel = RotorWheel("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0)
    assert rotor_wheel.get_letter("A") == "A"
    assert rotor_wheel.get_letter("Z") == "Z"

    rotor_wheel = RotorWheel("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)
    assert rotor_wheel.get_letter("A") == "A"
    assert rotor_wheel.get_letter("B") == "B"
    assert rotor_wheel.get_letter("C") == "C"

    rotor_wheel = RotorWheel("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25)
    assert rotor_wheel.get_letter("A") == "A"
    assert rotor_wheel.get_letter("B") == "B"

    # Tests with a rotor wheel that shifts the letters by 3 (still does not change per rotation)
    rotor_wheel = RotorWheel("DEFGHIJKLMNOPQRSTUVWXYZABC", 0)
    assert rotor_wheel.get_letter("A") == "D"
    assert rotor_wheel.get_letter("B") == "E"
    assert rotor_wheel.get_letter("C") == "F"
    assert rotor_wheel.get_letter("D") == "G"

    rotor_wheel = RotorWheel("DEFGHIJKLMNOPQRSTUVWXYZABC", 1)
    assert rotor_wheel.get_letter("A") == "D"
    assert rotor_wheel.get_letter("B") == "E"
    assert rotor_wheel.get_letter("C") == "F"
    assert rotor_wheel.get_letter("D") == "G"

    assert rotor_wheel.get_letter("D", reverse=True) == "A"
    assert rotor_wheel.get_letter("E", reverse=True) == "B"

    # Tests with a rotor wheel that changes the letters A and B (does change per rotation)
    rotor_wheel = RotorWheel("BACDEFGHIJKLMNOPQRSTUVWXYZ", 0)
    assert rotor_wheel.get_letter("A") == "B"
    assert rotor_wheel.get_letter("B") == "A"
    assert rotor_wheel.get_letter("C") == "C"

    assert rotor_wheel.get_letter("B", reverse=True) == "A"
    assert rotor_wheel.get_letter("C", reverse=True) == "C"

    # Now the rotor wheel is rotated by 1, letters "A" and "Z" should now be swapped
    rotor_wheel = RotorWheel("BACDEFGHIJKLMNOPQRSTUVWXYZ", 1)
    assert rotor_wheel.get_letter("A") == "Z"
    assert rotor_wheel.get_letter("Z") == "A"
    assert rotor_wheel.get_letter("B") == "B"
    assert rotor_wheel.get_letter("C") == "C"


def test_get_alphabet_shift_perm():
    """
    Test the get_alphabet_shift_perm method
    """
    rotor_wheel = RotorWheel()
    shift = get_alphabet_shift_perm(0)
    assert shift["A"] == "A"
    assert shift["Z"] == "Z"

    rotor_wheel = RotorWheel()
    shift = get_alphabet_shift_perm(1)
    assert shift["A"] == "B"
    assert shift["B"] == "C"
    assert shift["Z"] == "A"

    rotor_wheel = RotorWheel()
    shift = get_alphabet_shift_perm(-1)
    assert shift["A"] == "Z"
    assert shift["B"] == "A"


def test_update_position():
    """
    Test the update_position method
    """
    # It should not complete a full rotation
    rotor_wheel = RotorWheel()
    assert not rotor_wheel.update_position()
    assert rotor_wheel.position == 1

    # From 0 to 25, the position should be updated without completing a full rotation
    rotor_wheel = RotorWheel()
    for i in range(25):
        assert not rotor_wheel.update_position()
        assert rotor_wheel.position == i + 1

    # When the position is 25, it should complete a full rotation
    assert rotor_wheel.update_position()
    assert rotor_wheel.position == 0
