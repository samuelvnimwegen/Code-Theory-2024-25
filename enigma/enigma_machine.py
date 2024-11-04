"""
This file contains the enigma machine class
"""
from enigma.rotor_wheel import RotorWheel
from enigma.reflector import Reflector
from enigma.plugboard import Plugboard


class EnigmaMachine:
    """
    This class represents the enigma machine
    """

    def __init__(self, rotors: list[str], reflector: str, plugboard: str, rotor_positions: list[int]):
        """
        Initializes the enigma machine
        """
        self.rotor1 = RotorWheel(rotors[0], rotor_positions[0])
        self.rotor2 = RotorWheel(rotors[1], rotor_positions[1])
        self.rotor3 = RotorWheel(rotors[2], rotor_positions[2])
        self.reflector = Reflector(reflector)
        self.plugboard = Plugboard(plugboard)

    def encrypt_letter(self, letter: str, update_rotors: bool = False) -> str:
        """
        Encrypts a single letter
        :param letter: a single letter to encrypt
        :param update_rotors: whether to update the rotor positions after encrypting the letter
        :return: The encrypted letter
        """
        assert letter.isalpha(), "The letter must be an alphabetic character"
        assert letter.isupper(), "The letter must be an uppercase letter"
        assert len(letter) == 1, "The letter must be a single character"

        # Pass the letter through the plugboard
        letter = self.plugboard.get_corresponding_letter(letter)

        # Pass the letter through the rotors
        letter = self.rotor3.get_letter(letter)
        letter = self.rotor2.get_letter(letter)
        letter = self.rotor1.get_letter(letter)

        # Pass the letter through the reflector
        letter = self.reflector.get_reflector_letter(letter)

        # Pass the letter back through the rotors
        letter = self.rotor1.get_letter(letter, reverse=True)
        letter = self.rotor2.get_letter(letter, reverse=True)
        letter = self.rotor3.get_letter(letter, reverse=True)

        # Pass the letter back through the plugboard
        letter = self.plugboard.get_corresponding_letter(letter)

        # Update the rotor positions, if needed
        if update_rotors:
            self.update_rotor_positions()

        return letter

    def update_rotor_positions(self):
        """
        Update the rotor positions
        """
        # Update the rotor positions, if the first rotor updates, update the second rotor if the second rotor updates,
        # update the third rotor
        if self.rotor3.update_position():
            if self.rotor2.update_position():
                self.rotor1.update_position()

    def encrypt_text(self, text: str, reset_position_after: bool = True) -> str:
        """
        Encrypts a text
        :param text: The text to encrypt
        :param reset_position_after: Whether to reset the rotor positions after encrypting the text
        :return: The encrypted text
        """
        assert text.isalpha(), "The text must be alphabetic characters"
        assert text.isupper(), "The text must be uppercase letters"

        # Save the rotor positions
        rotor_positions = [self.rotor1.position, self.rotor2.position, self.rotor3.position]

        encrypted_text = ""
        for letter in text:
            encrypted_text += self.encrypt_letter(letter, update_rotors=True)

        # Reset rotor positions
        if reset_position_after:
            self.rotor1.position = rotor_positions[0]
            self.rotor2.position = rotor_positions[1]
            self.rotor3.position = rotor_positions[2]
        return encrypted_text

    def decrypt_text(self, text: str, reset_position_after: bool = True) -> str:
        """
        Decrypts a text
        :param text: The text to decrypt
        :param reset_position_after: Whether to reset the rotor positions after decrypting the text
        :return: The decrypted text
        """
        return self.encrypt_text(text)
