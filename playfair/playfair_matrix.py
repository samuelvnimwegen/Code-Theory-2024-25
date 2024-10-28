from playfair.utils import preconditions


class PlayfairMatrix:
    def __init__(self, keyword: str):
        assert preconditions.no_spaces_in_text(keyword)
        assert preconditions.text_no_j(keyword)

        self.keyword = keyword
        self.matrix = [['' for _ in range(5)] for _ in range(5)]
        self.alpha_dictionary = dict()  # dictionary of each letter with tuple coordinates in 5x5 matrix
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J == I

        self.create_matrix()

    def create_matrix(self):
        used_letters = set()

        for i in range(len(self.keyword)):
            row = i // 5
            column = i % 5
            self.matrix[row][column] = self.keyword[i]
            self.alpha_dictionary[self.keyword[i]] = (row, column)
            used_letters.add(self.keyword[i])

        for letter in self.alphabet:
            if letter in used_letters:
                continue

            row = len(used_letters) // 5
            column = len(used_letters) % 5

            self.matrix[row][column] = letter
            self.alpha_dictionary[letter] = (row, column)
            used_letters.add(letter)


