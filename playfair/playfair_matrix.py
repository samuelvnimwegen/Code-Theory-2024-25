import random
from playfair.utils import preconditions


class PlayfairMatrix:
    def __init__(self, keyword: str):
        assert preconditions.no_spaces_in_text(keyword)

        self.keyword = keyword.upper()      # Make it upper case
        self.matrix = [['' for _ in range(5)] for _ in range(5)]
        self.alpha_dictionary = dict()  # dictionary of each letter with tuple coordinates in 5x5 matrix
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J == I

        self.create_matrix()

    def create_matrix(self):
        used_letters = set()

        for i in range(len(self.keyword)):
            letter = self.keyword[i]
            if letter == "J":
                letter = "I"

            if letter in used_letters:
                continue

            row = i // 5
            column = i % 5
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

    def get_letter_coordinates(self, letter: str) -> (str, str):
        if letter in self.alpha_dictionary:
            coordinates = self.alpha_dictionary[letter]
            return coordinates[0], coordinates[1]

        raise ValueError(f"Requested letter does not exist in alphabet: {letter}")

    def get_letter(self, row: int, column: int) -> str:
        return self.matrix[row][column]



