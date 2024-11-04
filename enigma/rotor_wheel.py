"""
This file contains the RotorWheel class
"""


class RotorWheel:
    """
    This class represents a rotor wheel of the enigma machine
    """

    def __init__(self, rotor_wheel: str | None = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", position: int | None = 0):
        """
        Initializes the rotor wheel

        :param rotor_wheel: The rotor wheel to use
        :param position: The position of the rotor wheel
        """
        assert rotor_wheel.isalpha(), "The rotor wheel must be an alphabetic string"
        assert len(rotor_wheel) == 26, "The rotor wheel must be 26 characters long"
        assert 0 <= position < 26, "The position must be between 0 and 25"

        self.rotor_wheel: str = rotor_wheel

        # Make a dictionary for faster access
        self.rotor_dict = {}
        for i in range(26):
            # Get the alphabet letter
            letter = chr(i + 65)

            # Get the letter at the index
            self.rotor_dict[letter] = rotor_wheel[i]

        self.position: int = position

    def get_alphabet_shift_perm(self, shift_factor: int) -> dict["str", "str"]:
        """
        Get the alphabet shift permutation for a given shift factor

        :param shift_factor: The shift factor.
        :return: The dictionary that is representing the shift permutation
        """

        # We find the positive modulo of the shift factor
        shift_factor = shift_factor % 26

        # We create a dictionary to store the shift permutation
        shift_permutation = {}
        for i in range(26):
            # Get the alphabet letter
            letter = chr(i + 65)

            # Get the letter at the index
            shift_permutation[letter] = chr((i + shift_factor) % 26 + 65)

        return shift_permutation

    def get_letter(self, letter: str, reverse: bool = False) -> str:
        """
        Get the letter for a given letter

        :param letter: The letter to get the letter for
        :param reverse: Whether to get the reverse letter
        :return: The letter
        """
        assert letter.isalpha(), "The letter must be an alphabetic character"
        assert len(letter) == 1, "The letter must be a single character"
        assert letter in self.rotor_dict, "The letter must be in the rotor wheel"

        # Calculate the shift dict
        shift_dict = self.get_alphabet_shift_perm(self.position)
        reverse_shift_dict = self.get_alphabet_shift_perm(-self.position)

        # Do the transformation normally
        if not reverse:
            transformed_letter = reverse_shift_dict[letter]
            transformed_letter = self.rotor_dict[transformed_letter]
            transformed_letter = shift_dict[transformed_letter]
        # Do the transformation in reverse
        else:
            transformed_letter = reverse_shift_dict[letter]
            inverted_rotor_dict = {v: k for k, v in self.rotor_dict.items()}
            transformed_letter = inverted_rotor_dict[transformed_letter]
            transformed_letter = shift_dict[transformed_letter]
        return transformed_letter

    def update_position(self) -> bool:
        """
        Update the position of the rotor wheel

        :return: Whether the rotor wheel has completed a full rotation
        """
        if self.position == 25:
            self.position = 0
            return True
        self.position = (self.position + 1) % 26
        return False
