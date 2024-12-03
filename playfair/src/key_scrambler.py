"""
This file contains the key_scrambler class which is used to scramble the key in the simulated_annealing algorithm.
"""
import random


class KeyScrambler:
    """
    Class for scrambling the key in the simulated_annealing algorithm.
    """

    def scramble_key(self, key: str) -> str:
        """
        Scramble the key using one of the following methods:
        :param key: The key to scramble
        :return: The scrambled key
        """
        i = random.randint(0, 100)
        if i < 90:
            return self.key_swap_chars(key, random.choice(key), random.choice(key))
        elif i < 92:
            return self.key_reverse(key)
        elif i < 94:
            return self.key_swap_columns(key, random.randint(0, 4), random.randint(0, 4))
        elif i < 96:
            return self.key_swap_rows(key, random.randint(0, 4), random.randint(0, 4))
        elif i < 98:
            return self.key_flip_columns(key)
        else:
            return self.key_flip_rows(key)

    @staticmethod
    def key_swap_chars(key: str, char1: str, char2: str) -> str:
        """
        Swap occurrences of two characters in the key, maintaining their order.
        """
        # Split the key by `char1`, replace `char2` with `char1` in each segment, and join with `char2`.
        segments = key.split(char1)
        swapped_segments = [segment.replace(char2, char1) for segment in segments]
        return char2.join(swapped_segments)

    @staticmethod
    def key_reverse(key: str) -> str:
        """
        Reverse the entire key.
        """
        return key[::-1]  # Python slice notation for reversing strings.

    @staticmethod
    def key_swap_columns(key: str, col1: int, col2: int) -> str:
        """
        Swap two columns in the 5x5 Playfair cipher matrix.
        """
        # Convert the key into a list for mutable operations.
        key_list = list(key)
        for row in range(5):
            # Calculate indices for the columns to swap.
            idx1 = row * 5 + col1
            idx2 = row * 5 + col2
            # Swap the characters in the specified columns.
            key_list[idx1], key_list[idx2] = key_list[idx2], key_list[idx1]
        return ''.join(key_list)

    @staticmethod
    def key_swap_rows(key: str, row1: int, row2: int) -> str:
        """
        Swap two rows in the 5x5 Playfair cipher matrix.
        """
        # Convert the key into a list for mutable operations.
        key_list = list(key)
        for col in range(5):
            # Calculate indices for the rows to swap.
            idx1 = row1 * 5 + col
            idx2 = row2 * 5 + col
            # Swap the characters in the specified rows.
            key_list[idx1], key_list[idx2] = key_list[idx2], key_list[idx1]
        return ''.join(key_list)

    @staticmethod
    def key_flip_columns(key: str) -> str:
        """
        Flip the columns in the 5x5 Playfair cipher matrix.
        """
        # Convert the key to a 5x5 matrix.
        matrix = [list(key[i:i + 5]) for i in range(0, len(key), 5)]
        for col in range(5):
            # Flip the column by swapping top and bottom rows.
            for row in range(2):  # Only need to loop through half the rows.
                opposite_row = 4 - row
                matrix[row][col], matrix[opposite_row][col] = matrix[opposite_row][col], matrix[row][col]
        return ''.join(''.join(row) for row in matrix)

    @staticmethod
    def key_flip_rows(key: str) -> str:
        """
        Flip the rows in the 5x5 Playfair cipher matrix.
        """
        # Convert the key to a 5x5 matrix.
        matrix = [list(key[i:i + 5]) for i in range(0, len(key), 5)]
        for row in range(5):
            # Flip the row by swapping left and right columns.
            for col in range(2):  # Only need to loop through half the columns.
                opposite_col = 4 - col
                matrix[row][col], matrix[row][opposite_col] = matrix[row][opposite_col], matrix[row][col]
        return ''.join(''.join(row) for row in matrix)
