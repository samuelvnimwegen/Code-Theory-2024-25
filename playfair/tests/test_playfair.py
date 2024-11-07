import unittest

from playfair.src.playfair import Playfair, generate_random_Playfair_matrix, create_random_modified_matrix
from playfair.src.utils.general_values import alphabet


def every_letter_in_key(playfair_obj: Playfair) -> bool:
    """
    Check if every letter of alphabet is in key/playfair matrix
    :param playfair_obj: the playfair object with key
    :return: True/False
    """
    for letter in alphabet:
        if letter not in playfair_obj.keyword:
            return False
    return True


class TestPlayfair(unittest.TestCase):
    def test_encrypting(self):
        expected_result = "AWTIZGGLWCMPHQ"

        playfair_obj = Playfair("PALMERSTONE")

        encryption = playfair_obj.encrypt("WISKUNDEISLEUK")

        self.assertEqual(encryption, expected_result, "Encryption did not match expected result")

    def test_encrypting_2(self):
        expected_result = "LWPSBTKWKQTIZGGLTYTQ"

        playfair_obj = Playfair("PALMERSTONE")
        encryption = playfair_obj.encrypt("AARDRIJKSKUNDEOOK")

        self.assertEqual(encryption, expected_result, "Encryption did not match expected result")

    def test_decrypting(self):
        expected_result = "WISKUNDEISLEUK"

        playfair_obj = Playfair("PALMERSTONE")
        decryption = playfair_obj.decrypt("AWTIZGGLWCMPHQ")

        self.assertEqual(decryption, expected_result, "Decryption did not match expected result")

    def test_decrypting_2(self):
        expected_result = "AXARDRIXIKSKUNDEOXOK"

        playfair_obj = Playfair("PALMERSTONE")
        decryption = playfair_obj.decrypt("LWPSBTKWKQTIZGGLTYTQ")

        self.assertEqual(decryption, expected_result, "Decryption did not match expected result")

    def test_random_matrix(self):
        random_playfair_matrix: Playfair = generate_random_Playfair_matrix()

        key_has_25_letters = len(random_playfair_matrix.keyword) == 25
        self.assertEqual(True, every_letter_in_key(random_playfair_matrix), "Not every alphabet letter in random key")
        self.assertEqual(True, key_has_25_letters, "Key has more then 25 letters.")

    def test_random_modified_matrix(self):
        playfair_obj = Playfair(alphabet)
        random_playfair_matrix: Playfair = create_random_modified_matrix(playfair_obj)

        key_has_25_letters = len(random_playfair_matrix.keyword) == 25
        self.assertEqual(True, every_letter_in_key(random_playfair_matrix), "Not every alphabet letter in random key")
        self.assertEqual(True, key_has_25_letters, "Key has more then 25 letters.")


if __name__ == '__main__':
    unittest.main()
