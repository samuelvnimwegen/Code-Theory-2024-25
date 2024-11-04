"""
This file contains the reflector class
"""


class Reflector:
    """
    This class represents the reflector of the enigma machine
    """

    def __init__(self, reflector_wheel: str):
        """
        Initializes the reflector

        :param reflector_wheel: The reflector wheel to use
        """
        assert len(reflector_wheel) == 26, "The reflector wheel must be 26 characters long"
        assert len(set(reflector_wheel)) == 26, "Each letter must be used exactly once in the reflector wheel"
        self.reflector_wheel: str = reflector_wheel

        # Make a dictionary for faster access
        self.reflector_dict = {}
        for i in range(26):
            # Get the alphabet letter
            letter = chr(i + 65)

            # Get the letter at the index
            self.reflector_dict[letter] = reflector_wheel[i]

    def get_reflector_letter(self, letter: str) -> str:
        """
        Get the reflector letter for a given letter
        :param letter: The letter to get the reflector letter for
        :return: The reflector letter
        """
        assert letter.isalpha(), "The letter must be an alphabetic character"
        assert len(letter) == 1, "The letter must be a single character"
        return self.reflector_dict[letter]
