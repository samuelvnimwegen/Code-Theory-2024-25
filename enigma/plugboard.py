"""
This file contains the plugboard class
"""


class Plugboard:
    """
    This class represents the plugboard of the enigma machine
    """

    def __init__(self, plugs: str):
        """
        Initializes the plugboard

        :param plugs: The plugs to use in the plugboard
        """
        assert plugs.isalpha(), "The plugs must be alphabetic characters"
        assert len(plugs) == 26, "The plugboard must cover all 26 letters of the alphabet"
        assert len(set(plugs)) == 26, "Each letter must be used exactly once in the plugboard"

        self.plugs: str = plugs

        # Turn the plugs into a dictionary for faster and easier access
        self.plugs_dict: dict = {}
        for i in range(26):
            self.plugs_dict[chr(i + 65)] = self.plugs[i]

    def get_corresponding_letter(self, letter) -> str:
        """
        Get the corresponding letter for a given letter

        :param letter: The letter to get the corresponding letter for
        :return: The corresponding letter
        """
        assert letter.isalpha(), "The letter must be an alphabetic character"
        assert letter.isupper(), "The letter must be an uppercase letter"
        assert len(letter) == 1, "The letter must be a single character"

        # If the letter is in the plug dictionary, return the corresponding letter
        return self.plugs_dict[letter]
