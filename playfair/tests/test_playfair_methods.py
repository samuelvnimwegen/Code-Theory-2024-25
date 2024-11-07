import unittest
from playfair.src.utils.playfair_methods import *


class TestPlayfairMethods(unittest.TestCase):
    def test_splitting_text(self):
        """
        Test adding X's in the plaintext to gain correct pairs
        """
        expected_result = "AXARDRIXIKSKUNDEOXOK"

        text = "AARDRIJKSKUNDEOOK"
        text = replace_J_with_I(text)

        splitted_text = split_text_in_correct_pairs(text)
        self.assertEqual(expected_result, splitted_text)

    def test_swap_letters(self):
        """
        Swap two letters with x < y and y-x > 1, so there are letters in between them
        :return:
        """
        expected_result = "SPOT"

        text = "STOP"
        pos1 = 1  # T
        pos2 = 3  # P
        result = swap_two_letters(text, pos1, pos2)
        self.assertEqual(expected_result, result, "Not swapped correctly")

    def test_swap_letters_2(self):
        """
        Swap two letters with x > y and y-x > 1, so there are letters in between them
        :return:
        """
        expected_result = "SPOT"

        text = "STOP"
        pos1 = 3  # T
        pos2 = 1  # P
        result = swap_two_letters(text, pos1, pos2)
        self.assertEqual(expected_result, result, "Not swapped correctly")

    def test_swap_letters_3(self):
        """
        Swap two letters with x < y and y-x = 1, so there are letters in between them
        :return:
        """
        expected_result = "FORM"

        text = "FROM"
        pos1 = 1  # T
        pos2 = 2  # P
        result = swap_two_letters(text, pos1, pos2)
        self.assertEqual(expected_result, result, "Not swapped correctly")



if __name__ == '__main__':
    unittest.main()
