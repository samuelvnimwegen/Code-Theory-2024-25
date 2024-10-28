from playfair_matrix import PlayfairMatrix
from utils import preconditions, playfair_methods


class Playfair:
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.matrix_obj = PlayfairMatrix(keyword)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using Playfair with the keyword in the class object
        :param plaintext: text to encrypt
        :return: ciphertext/encrypted plaintext
        """
        assert preconditions.text_only_alphabet(plaintext)
        assert preconditions.text_no_j(plaintext)
        assert preconditions.no_spaces_in_text(plaintext)

        # First add X values to split text into correct digrams/duo's
        splitted_text = playfair_methods.split_text_in_correct_pairs(plaintext)






        ciphertext = splitted_text

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

        plaintext = ciphertext

        assert preconditions.text_only_alphabet(plaintext)
        assert preconditions.text_no_j(plaintext)
        assert preconditions.no_spaces_in_text(plaintext)

        return plaintext

