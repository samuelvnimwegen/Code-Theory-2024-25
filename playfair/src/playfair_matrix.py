import copy
import math
import random
from .utils import preconditions


class PlayfairMatrix:
    def __init__(self, keyword: str, matrix_size=25):

        assert preconditions.no_spaces_in_text(keyword)
        assert matrix_size <= 25
        assert preconditions.is_perfect_square(matrix_size)

        self.matrix_size_sqrt = int(math.sqrt(matrix_size))

        self.keyword = keyword.upper()      # Make it upper case
        self.matrix = [['' for _ in range(self.matrix_size_sqrt)] for _ in range(self.matrix_size_sqrt)]
        self.alpha_dictionary = dict()  # dictionary of each letter with tuple coordinates in 5x5 matrix
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J == I
        self.letters_used: set[str] = set()

        self.create_matrix()

    def create_matrix(self):
        """
        Create a matrix.
        Also keep which letters are eventually used in the matrix (necessary for testing with smaller matrices)
        """
        used_letters: set[str] = set()

        for i in range(len(self.keyword)):
            letter = self.keyword[i]
            if letter == "J":
                letter = "I"

            if letter in used_letters:
                continue

            row = i // self.matrix_size_sqrt
            column = i % self.matrix_size_sqrt
            self.matrix[row][column] = letter
            self.alpha_dictionary[letter] = (row, column)
            used_letters.add(letter)

        for letter in self.alphabet:
            if letter in used_letters:
                continue

            row = len(used_letters) // 5
            column = len(used_letters) % 5

            self.matrix[row][column] = letter
            self.alpha_dictionary[letter] = (row, column)
            used_letters.add(letter)

        self.letters_used = used_letters

    def get_letter_coordinates(self, letter: str) -> (str, str):
        """
        Get the coordinates in the matrix of the requested letter
        :return: tuple of the coordinates: (row, column index)
        """
        if letter in self.alpha_dictionary:
            coordinates = self.alpha_dictionary[letter]
            return coordinates[0], coordinates[1]

        raise ValueError(f"Requested letter does not exist in alphabet: {letter}")

    def get_letter(self, row: int, column: int) -> str:
        """
        Get the letter in the matrix with the given coordinates
        :param row: row index
        :param column: column index
        :return: the letter
        """
        assert 0 <= row < self.matrix_size_sqrt
        assert 0 <= column < self.matrix_size_sqrt

        return self.matrix[row][column]

    def get_matrix_as_string(self) -> str:
        """
        Get the matrix as a string.
        :return: a string of uppercase letters
        """
        string = ""
        for row in self.matrix:
            for column in row:
                string += column.upper()

        return string





