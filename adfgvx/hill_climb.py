"""
This module contains the functions to perform a hill climb.
"""


class HillClimbADFGVX:
    """
    This class contains the functions to perform a hill climb.
    """
    def __init__(self, pairs_text: str):
        """
        Initialize the HillClimbADFGVX object.

        :param pairs_text: The text to be decrypted in pairs
        """
        # The text to be decrypted in pairs
        self.pairs_text = pairs_text

        self.cipher_text = ""

        self.best_test = ""
        self.best_score = float('inf')

    def random_substitution(self) -> None:
        """
        Substitute each pair in the text with a corresponding pair in the key, but give the most common pair the
        letter E as value.
        """
        # Split the text per 2 characters
        possible_chars_pairs: set[str] = set([self.pairs_text[i:i + 2] for i in range(0, len(self.pairs_text), 2)])
        assert len(possible_chars_pairs) <= 26, 'Too many characters'

        # Make a cipher text by replacing the pairs with the corresponding letter (A-Z)
        self.cipher_text = self.pairs_text
        for i, pair in enumerate(possible_chars_pairs):
            self.cipher_text = self.cipher_text.replace(pair, chr(65 + i))

        # Find the most common letter
        most_common_letter = max(set(self.cipher_text), key=self.cipher_text.count)

        # Swap the most common letter with E
        temp_char = "@"
        self.cipher_text = self.cipher_text.replace(most_common_letter, temp_char)
        self.cipher_text = self.cipher_text.replace("E", most_common_letter)
        self.cipher_text = self.cipher_text.replace(temp_char, "E")













