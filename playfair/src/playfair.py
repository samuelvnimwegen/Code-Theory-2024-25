import random
from copy import copy

from playfair.src.playfair_matrix import PlayfairMatrix
from playfair.src.utils import preconditions, playfair_methods


class Playfair:
    def __init__(self, keyword: str, matrix_size=25):
        self.keyword = keyword.upper()
        self.matrix_obj = PlayfairMatrix(keyword, matrix_size)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using Playfair with the keyword in the class object
        :param plaintext: text to encrypt
        :return: ciphertext/encrypted plaintext
        """
        assert preconditions.text_only_alphabet(plaintext)
        assert preconditions.no_spaces_in_text(plaintext)

        # Replace every J with a I
        plaintext_no_J = playfair_methods.replace_J_with_I(plaintext)

        # First add X values to split text into correct digrams/duo's
        splitted_text = playfair_methods.split_text_in_correct_pairs(plaintext_no_J)

        replaced_text = ""
        for i in range(len(splitted_text)//2):
            letter_1 = splitted_text[i*2]
            letter_2 = splitted_text[i*2 + 1]

            # Add new pair letters to string
            replaced_text += playfair_methods.replace_pairs(letter_1, letter_2, self.matrix_obj)

        ciphertext = replaced_text

        # Check some post conditions
        assert preconditions.text_only_alphabet(ciphertext)
        assert preconditions.text_no_j(ciphertext)
        assert preconditions.no_spaces_in_text(ciphertext)

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the ciphertext using Playfair with the keyword in the class object
        :param ciphertext: text to decrypt
        :return: plaintext/original text
        """
        assert preconditions.text_only_alphabet(ciphertext)
        assert preconditions.text_no_j(ciphertext)
        assert preconditions.no_spaces_in_text(ciphertext)

        # Only decrypt
        replaced_text = ""
        for i in range(len(ciphertext)//2):
            letter_1 = ciphertext[i*2]
            letter_2 = ciphertext[i*2 + 1]

            # Add new pair letters to string
            replaced_text += playfair_methods.replace_pairs(letter_1, letter_2, self.matrix_obj, False)

        plaintext = replaced_text

        # Check some post conditions
        assert preconditions.text_only_alphabet(plaintext)
        assert preconditions.text_no_j(plaintext)
        assert preconditions.no_spaces_in_text(plaintext)

        return plaintext


def generate_random_Playfair_matrix() -> Playfair:
    """
    Generate a random Playfair matrix
    :return: a Playfair matrix object
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Convert the alphabet into a list
    letters = list(alphabet)
    # Shuffle the letters randomly
    random.shuffle(letters)

    key_string = "".join(letters)
    return Playfair(key_string)


def create_random_modified_matrix(parent_matrix: Playfair) -> Playfair:
    """
    Create a random modified version of the given Playfair matrix
    :param parent_matrix: the matrix to modify
    :return: playfair modified matrix
    """
    key = parent_matrix.matrix_obj.get_matrix_as_string()

    # Get 2 random letter positions in keyword and swap them
    key_length = pow(parent_matrix.matrix_obj.matrix_size_sqrt, 2)
    pos1, pos2 = random.sample(range(key_length), 2)

    new_key = playfair_methods.swap_two_letters(key, pos1, pos2)

    return Playfair(new_key)








