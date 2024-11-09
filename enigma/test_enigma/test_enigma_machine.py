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
    assert enigma_machine.encrypt_letter("A") == "U"
    assert enigma_machine.encrypt_letter("B") == "E"
    assert enigma_machine.encrypt_letter("C") == "J"


def test_enigma_machine_from_course():
    """
    Test the enigma machine from the course
    """

    enigma_machine = EnigmaMachine(
        rotors=["ABDYEFGHIJKLMNOPQRSTUVWXCZ", "ACJDEFGHIBKLMNOPQRSXUTWVYZ", "XBAVEFGHIJRLMDOPCZSTUNWQYK"],
        reflector="ARCDEFGHIJKLMNOPQBSTUVWXYZ",
        plugboard="PBMDEFGHIJKLCNOAQRSWUVTXYZ",
        rotor_positions=[1, 4, 23]
    )

    assert enigma_machine.encrypt_letter("P", update_rotors=True) == "W"
    assert enigma_machine.encrypt_letter("A", update_rotors=True) == "C"


def test_encrypt_text():
    """
    Test the encrypt_text method
    """
    enigma_machine = EnigmaMachine(
        rotors=["ABDYEFGHIJKLMNOPQRSTUVWXCZ", "ACJDEFGHIBKLMNOPQRSXUTWVYZ", "XBAVEFGHIJRLMDOPCZSTUNWQYK"],
        reflector="ARCDEFGHIJKLMNOPQBSTUVWXYZ",
        plugboard="PBMDEFGHIJKLCNOAQRSWUVTXYZ",
        rotor_positions=[1, 4, 23]
    )

    assert enigma_machine.encrypt_text("PA") == "WC"


def test_decrypt_text():
    """
    Test the decrypt_text method
    """
    enigma_machine = EnigmaMachine(
        rotors=["ABDYEFGHIJKLMNOPQRSTUVWXCZ", "ACJDEFGHIBKLMNOPQRSXUTWVYZ", "XBAVEFGHIJRLMDOPCZSTUNWQYK"],
        reflector="ARCDEFGHIJKLMNOPQBSTUVWXYZ",
        plugboard="PBMDEFGHIJKLCNOAQRSWUVTXYZ",
        rotor_positions=[1, 4, 23]
    )

    assert enigma_machine.decrypt_text("WC") == "PA"


def test_encrypt_website():
    """
    Test the encrypt method with the website example
    """
    enigma_machine = EnigmaMachine(
        rotors=["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"],
        reflector="YRUHQSLDPXNGOKMIEBFZCWVJAT",
        plugboard="PBMDEFGHIJKLCNOAQRSWUVTXYZ",
        rotor_positions=[0, 0, 0]
    )

    assert enigma_machine.encrypt_text("THISISATEST") == "QPCRAXMAXZC"


def test_update_rotor_positions():
    """
    Test the update_rotor_positions method
    """
    enigma_machine = EnigmaMachine(
        rotors=["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"],
        reflector="YRUHQSLDPXNGOKMIEBFZCWVJAT",
        plugboard="PBMDEFGHIJKLCNOAQRSWUVTXYZ",
        rotor_positions=[0, 0, 0]
    )

    for i in range(26):
        enigma_machine.update_rotor_positions()

    assert enigma_machine.rotor2.position == 1
    assert enigma_machine.rotor3.position == 0
    assert enigma_machine.rotor1.position == 0

    for i in range(26 ** 2):
        enigma_machine.update_rotor_positions()

    assert enigma_machine.rotor2.position == 1
    assert enigma_machine.rotor3.position == 0
    assert enigma_machine.rotor1.position == 1


def test_encrypt_letter_2():
    """
    Test the encrypt_letter method with a different rotor configuration
    """
    enigma_machine = EnigmaMachine(
        rotors=["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"],
        reflector="YRUHQSLDPXNGOKMIEBFZCWVJAT",
        plugboard="BADCFEHGJILKNMPORQTSVUXWZY",
        rotor_positions=[0, 0, 17],
    )
    encrypted_letter = enigma_machine.encrypt_letter("M")
    assert encrypted_letter == "I"
