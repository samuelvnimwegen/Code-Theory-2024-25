import unittest
from playfair.utils.playfair_methods import *


class TestPlayfairMethods(unittest.TestCase):
    def test_splitting_text(self):
        """
        Test adding X's in the plaintext to gain correct pairs
        """
        expected_result = "AXARDRIXJKSKUNDEOXOK"

        splitted_text = split_text_in_correct_pairs("AARDRIJKSKUNDEOOK")
        self.assertEqual(splitted_text, expected_result)


if __name__ == '__main__':
    unittest.main()
