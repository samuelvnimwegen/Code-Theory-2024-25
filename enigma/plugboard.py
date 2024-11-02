"""
This file contains the plugboard class
"""


class Plugboard:
    """
    This class represents the plugboard of the enigma machine
    """
    def __init__(self, plugs: list[tuple[str, str]]):
        """
        Initializes the plugboard

        :param plugs: The plugs to use in the plugboard
        """
        self.plugs: list = plugs

        # Turn the plugs into a dictionary for faster and easier access
        self.plugs_dict: dict = {}
        for plug in plugs:
            self.plugs_dict[plug[0]] = plug[1]
            self.plugs_dict[plug[1]] = plug[0]

    def get_corresponding_letter(self, letter) -> str:
        """
        Get the corresponding letter for a given letter

        :param letter: The letter to get the corresponding letter for
        :return: The corresponding letter
        """
        assert letter.isalpha(), "The letter must be an alphabetic character"
        assert len(letter) == 1, "The letter must be a single character"

        # If the letter is in the plug dictionary, return the corresponding letter
        if letter in self.plugs_dict:
            return self.plugs_dict[letter]
        return letter


