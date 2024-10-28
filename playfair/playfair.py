from utils import preconditions


class Playfair:
    def __init__(self, keyword: str):
        self.keyword = keyword

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the plaintext using Playfair with the keyword in the class object
        :param plaintext: text to encrypt
        :return: ciphertext/encrypted plaintext
        """
        assert preconditions.text_only_alphabet(plaintext)
        assert preconditions.text_no_j(plaintext)
        assert preconditions.no_spaces_in_text(plaintext)

        ciphertext = plaintext

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

