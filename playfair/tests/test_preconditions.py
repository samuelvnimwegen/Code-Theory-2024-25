import unittest
from playfair.src.utils import preconditions


class TestPrecondition(unittest.TestCase):
    def test_legal_text_correct(self):
        """
        Test the precondition check that all characters are from the alphabet
        Correct
        """
        self.assertEqual(preconditions.text_only_alphabet("ABGDFDHYEBVDVDJEINEOSHSBDIDB"), True)

    def test_legal_text_correct_2(self):
        """
        Test the precondition check that all characters are from the alphabet
        Correct: combination uppercase and lowercase letters
        """
        self.assertEqual(preconditions.text_only_alphabet("ABGDFDHYahahhdhdVDJEINEOSHSBDIDB"),True)

    def test_legal_text_not_correct(self):
        """
        Test the precondition check that all characters are from the alphabet
        Not correct: numbers in the text
        """
        self.assertEqual(preconditions.text_only_alphabet("ABGDFDHYEBVDVDJEINEOSH15BDIDB"), False)

    def test_no_J_correct(self):
        """
        Test the precondition check that there is NO character J
        Correct
        """
        self.assertEqual(preconditions.text_no_j("IIIIIIIIIIIIIIAHHDBHEBEVSY"), True)

    def test_no_J_not_correct(self):
        """
        Test the precondition check that there is NO character J
        Not correct: J in the text
        """
        self.assertEqual(preconditions.text_no_j("IIIIIIIIIJIIIIAHHDBHEBEVSY"), False)

    def test_no_repeated_letters_correct(self):
        """
        Test the precondition check that there are no repeated letters in keyword
        Correct
        """
        self.assertEqual(preconditions.keyword_no_double_letter("WISKUNDE"), True)

    def test_no_repeated_letters_not_correct(self):
        """
        Test the precondition check that there are no repeated letters in keyword
        Not correct: Double A
        """
        self.assertEqual(preconditions.keyword_no_double_letter("AARDRIJKSKUNDE"), False)

    def test_no_spaces_correct(self):
        """
        Test the precondition check that there are no spaces allowed in text or keyword
        Correct
        """
        self.assertEqual(preconditions.no_spaces_in_text("HEYTHISISATEXT"), True)

    def test_no_spaces_not_correct(self):
        """
        Test the precondition check that there are no spaces allowed in text or keyword
        Not correct: spaces
        """
        self.assertEqual(preconditions.no_spaces_in_text("HEY THIS IS A TEXT"), False)

    def test_no_spaces_not_correct_2(self):
        """
        Test the precondition check that there are no spaces allowed in text or keyword
        Not correct: double spaces
        """
        self.assertEqual(preconditions.no_spaces_in_text("HEY  THIS     IS A TEXT"), False)


if __name__ == '__main__':
    unittest.main()
