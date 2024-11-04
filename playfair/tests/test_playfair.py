import unittest
from playfair import playfair


class TestPlayfair(unittest.TestCase):
    def test_encrypting(self):
        expected_result = "AWTIZGGLWCMPHQ"

        playfair_obj = playfair.Playfair("PALMERSTONE")
        encryption = playfair_obj.encrypt("WISKUNDEISLEUK")

        self.assertEqual(encryption, expected_result, "Encryption did not match expected result")

    def test_encrypting_2(self):
        expected_result = "LWPSBTKWKQTIZGGLTYTQ"

        playfair_obj = playfair.Playfair("PALMERSTONE")
        encryption = playfair_obj.encrypt("AARDRIJKSKUNDEOOK")

        self.assertEqual(encryption, expected_result, "Encryption did not match expected result")

    def test_decrypting(self):
        expected_result = "WISKUNDEISLEUK"

        playfair_obj = playfair.Playfair("PALMERSTONE")
        decryption = playfair_obj.decrypt("AWTIZGGLWCMPHQ")

        self.assertEqual(decryption, expected_result, "Decryption did not match expected result")

    def test_decrypting_2(self):
        expected_result = "AXARDRIXIKSKUNDEOXOK"

        playfair_obj = playfair.Playfair("PALMERSTONE")
        decryption = playfair_obj.decrypt("LWPSBTKWKQTIZGGLTYTQ")

        self.assertEqual(decryption, expected_result, "Decryption did not match expected result")

    def test_random_matrix(self):
        random_playfair_matrix = playfair.generate_random_Playfair_matrix()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
