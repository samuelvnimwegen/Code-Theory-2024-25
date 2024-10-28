import unittest
from playfair import playfair_matrix


class TestPlayfairMatrix(unittest.TestCase):
    def test_create_matrix(self):
        expected_result = [['P', 'A', 'L', 'M', 'E'],
                           ['R', 'S', 'T', 'O', 'N'],
                           ['B', 'C', 'D', 'F', 'G'],
                           ['H', 'I', 'K', 'Q', 'U'],
                           ['V', 'W', 'X', 'Y', 'Z']]

        playf_matrix = playfair_matrix.PlayfairMatrix('PALMERSTON')
        self.assertEqual(playf_matrix.matrix, expected_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
