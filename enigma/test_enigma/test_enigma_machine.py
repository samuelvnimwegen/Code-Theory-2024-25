"""
This file contains the tests for the enigma_machine.py file
"""

from enigma.enigma_machine import EnigmaMachine


def test_encrypt_letter():
    """
    Test the encrypt_letter method
    """

    # Test case 1: Basic identity rotor setup
    enigma_machine = EnigmaMachine(
        rotors=["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
        reflector="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        plugboard="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        rotor_positions=[0, 0, 0]
    )
    assert enigma_machine.encrypt_letter("A") == "A"
    assert enigma_machine.encrypt_letter("B") == "B"
    assert enigma_machine.encrypt_letter("C") == "C"

    # Test case 2: Simple rotor shift
    enigma_machine = EnigmaMachine(
        rotors=["BCDEFGHIJKLMNOPQRSTUVWXYZA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
        reflector="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        plugboard="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        rotor_positions=[0, 0, 0]
    )
    assert enigma_machine.encrypt_letter("A") == "A"
    assert enigma_machine.encrypt_letter("B") == "B"
    assert enigma_machine.encrypt_letter("Z") == "Z"

    # Test case 3: Rotor stepping behavior
    enigma_machine = EnigmaMachine(
        rotors=["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
        reflector="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        plugboard="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        rotor_positions=[25, 0, 0]
    )
    assert enigma_machine.encrypt_letter("A") == "A"  # First rotor should step after this

    # Test case 4: Complex rotor configuration
    enigma_machine = EnigmaMachine(
        rotors=["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"],
        reflector="YRUHQSLDPXNGOKMIEBFZCWVJAT",
        plugboard="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        rotor_positions=[0, 0, 0]
    )
    assert enigma_machine.encrypt_letter("A") == "M"
    assert enigma_machine.encrypt_letter("B") == "H"
    assert enigma_machine.encrypt_letter("C") == "F"
