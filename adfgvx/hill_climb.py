"""
This module contains the functions to perform a hill climb.
"""
import math
from random import randint

from adfgvx.language_files.load_quad_grams_fr import FR_QUAD_GRAM_DICT, FR_TOTAL_QUAD_GRAMS
from playfair.src.language_info.load_quad_grams import EN_QUAD_GRAM_DICT, EN_TOTAL_QUADGRAMS
from adfgvx.language_files.load_french_frequencies import LETTER_FREQUENCIES_FR


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

        self.frequency_filled_in_ciphertext = ""

        self.score = float('inf')

        self.top_cipher = ""
        self.top_score = float('-inf')

    def frequency_substitution(self) -> None:
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

        # Sort the pairs by frequency in the pairs_text
        sorted_pairs = sorted(possible_chars_pairs, key=lambda pair: self.cipher_text.count(pair), reverse=True)

        # Get the most used letters also sorted by frequency
        letters = list(LETTER_FREQUENCIES_FR.keys())
        letters = sorted(letters, key=lambda letter: LETTER_FREQUENCIES_FR[letter], reverse=True)

        # Replace the pairs with the most used letters in the same order
        for i, pair in enumerate(sorted_pairs):
            self.cipher_text = self.cipher_text.replace(pair, letters[i])

        # Remove the spaces
        self.cipher_text = self.cipher_text.replace(" ", "")
        self.frequency_filled_in_ciphertext = self.cipher_text

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
            if quad_gram in EN_QUAD_GRAM_DICT:
                # We use the log to prevent the score from becoming too small
                score += math.log(EN_QUAD_GRAM_DICT[quad_gram] / EN_TOTAL_QUADGRAMS)
            else:
                # If the quad gram is not in the dictionary, we add a penalty
                score += math.log(0.01 / EN_TOTAL_QUADGRAMS)
        return score

    def randomly_alter_ciphertext(self) -> None:
        """
        Randomly alter the ciphertext by swapping two characters.
        """
        # Randomly select two letters
        letter1 = chr(65 + randint(0, 25))
        letter2 = chr(65 + randint(0, 25))

        # Swap the letters
        self.cipher_text = self.cipher_text.replace(letter1, "!")
        self.cipher_text = self.cipher_text.replace(letter2, letter1)
        self.cipher_text = self.cipher_text.replace("!", letter2)

    def hill_climb(self) -> tuple[str, float, str]:
        """
        Perform a hill climb to find the best Ciphertext.
        """
        print("Starting hill climb, abort the program with CTRL+C or using the button on your IDE to get the "
              "current best result of the below listed results:")
        self.frequency_substitution()
        self.score = self.get_score()

        self.top_score = self.score
        self.top_cipher = self.cipher_text
        iterations_since_last_change = 0

        try:
            # Perform the hill climb for 1000 iterations
            while True:
                # Save the old cipher text
                old_cipher_text = self.cipher_text

                # Randomly alter the ciphertext
                self.randomly_alter_ciphertext()

                # Save the score of the new cipher text
                new_score = self.get_score()

                # If the new score is better, update the best test
                if new_score > self.score:
                    self.score = new_score
                    iterations_since_last_change = 0

                else:
                    # If the new score is not better, revert the changes
                    self.cipher_text = old_cipher_text

                    # If we have not found a better score for 5000 iterations, return the current best cipher
                    if iterations_since_last_change > 5000:
                        # Save the current score
                        if self.score > self.top_score:
                            self.top_score = self.score
                            self.top_cipher = old_cipher_text
                            print("Top score:", self.top_score, "Top cipher:", self.top_cipher)

                        # Scramble the text, keeping 'E' unchanged
                        self.cipher_text = self.frequency_filled_in_ciphertext
                        self.score = float('-inf')
                        iterations_since_last_change = 0

                    # If the score is better than the top score, update the top score and top cipher
                    iterations_since_last_change += 1

        # If the user interrupts the program, return the current best cipher
        except KeyboardInterrupt:
            # Get the key
            top_key: str = self.get_key()

            # If the user interrupts the program, return the current best cipher
            return self.top_cipher, self.top_score, top_key

    def get_key(self) -> str:
        """
        Get the key from the cipher text.
        :return: The key
        """
        pair_text = self.pairs_text

        # Get the list of pairs
        pairs = [pair_text[i:i + 2] for i in range(0, len(pair_text), 2)]

        items = "ADFGVX"
        total_key = "_" * 26
        i = 0
        for item1 in items:
            for item2 in items:
                total_item: str = item1 + item2

                # Get the first index of the pair
                try:
                    index: int = pairs.index(total_item)

                # If the pair is not in the cipher text, continue
                except ValueError:
                    i += 1
                    continue

                # Get the letter in the cipher text with the same index
                letter: str = self.top_cipher[index]

                # Update the key
                total_key = total_key[:i] + letter + total_key[i + 1:]

                i += 1
        return total_key
