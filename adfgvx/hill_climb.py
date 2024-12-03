"""
This module contains the functions to perform a hill climb.
"""
import math
from random import randint

from adfgvx.language_files.load_quad_grams_fr import FR_QUAD_GRAM_DICT, FR_TOTAL_QUAD_GRAMS


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

        self.score = float('inf')

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

        # Put a space between each pair
        pairs = [self.cipher_text[i:i + 2] for i in range(0, len(self.cipher_text), 2)]
        self.cipher_text = " ".join(pairs)

        # Replace each pair with a letter (A-Z)
        for i, pair in enumerate(possible_chars_pairs):
            self.cipher_text = self.cipher_text.replace(pair, chr(65 + i))

        # Remove spaces
        self.cipher_text = self.cipher_text.replace(" ", "")

        # Find the most common letter
        most_common_letter = max(set(self.cipher_text), key=self.cipher_text.count)

        # Swap the most common letter with E
        temp_char = "!"
        self.cipher_text = self.cipher_text.replace(most_common_letter, temp_char)
        self.cipher_text = self.cipher_text.replace("E", most_common_letter)
        self.cipher_text = self.cipher_text.replace(temp_char, "E")

    def get_score(self) -> float:
        """
        Score the current cipher text using quad grams.
        For this, we use a logarithmic scale to prevent the score from becoming too small.

        :return: The score of the current cipher text
        """
        score = 0
        for i in range(len(self.cipher_text) - 4):
            quad_gram = self.cipher_text[i:i + 4]

            # If the quad_gram is in the dictionary, we add the score
            if quad_gram in FR_QUAD_GRAM_DICT:
                # We use the log to prevent the score from becoming too small
                score += math.log(FR_QUAD_GRAM_DICT[quad_gram] / FR_TOTAL_QUAD_GRAMS)
            else:
                # If the quad gram is not in the dictionary, we add a penalty
                score += math.log(0.5 / FR_TOTAL_QUAD_GRAMS)
        return score

    def randomly_alter_ciphertext(self) -> None:
        """
        Randomly alter the ciphertext by swapping two characters.
        """
        # Randomly select two letters
        letter1 = chr(65 + randint(0, 25))
        letter2 = chr(65 + randint(0, 25))

        # Never change E
        if letter1 == "E" or letter2 == "E":
            return

        # Swap the letters
        self.cipher_text = self.cipher_text.replace(letter1, "!")
        self.cipher_text = self.cipher_text.replace(letter2, letter1)
        self.cipher_text = self.cipher_text.replace("!", letter2)

    def hill_climb(self) -> tuple[str, float]:
        """
        Perform a hill climb to find the best Ciphertext.
        """
        self.random_substitution()
        self.score = self.get_score()
        iterations_since_last_change = 0

        top_score = self.score
        top_cipher = self.cipher_text

        try:
            # Perform the hill climb for 1000 iterations
            while True:
                # Save the old cipher text
                old_cipher_text = self.cipher_text

                # Randomly alter the ciphertext
                for i in range(randint(1, 40)):
                    self.randomly_alter_ciphertext()

                # Save the score of the new cipher text
                new_score = self.get_score()

                # If the new score is better, update the best test
                if new_score > self.score:
                    self.score = new_score
                    print("New best score: ", self.score)
                    print("New best cipher: ", self.cipher_text)
                else:
                    # If the new score is not better, revert the changes
                    self.cipher_text = old_cipher_text


        except KeyboardInterrupt:
            # If the user interrupts the program, return the current best cipher
            return top_cipher, top_score
