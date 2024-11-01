"""
This file is used to crack the column transposition of the vigenere+ cipher
"""
import math
import heapq

from math import factorial
from itertools import permutations
from collections import Counter
from util.progress_bar import print_progress_bar


class TopNStack:
    """
    A stack that only keeps the top n elements
    """
    def __init__(self, max_elements: int):
        # Initialize an empty min-heap
        self.heap = []
        self.max_elements = max_elements

    def push(self, item, value) -> None:
        """
        Push an item with a value to the heap
        :param item: The item to push
        :param value: The value of the item, used for sorting
        :return: None
        """
        # Create a tuple (value, item) to store in the heap
        entry = (value, item)

        # Add the item to the heap
        if len(self.heap) < self.max_elements:
            # If heap has less than 10 items, push the new entry
            heapq.heappush(self.heap, entry)
        else:
            # If the heap has 10 items, push and pop in one step to maintain the top 10 values
            heapq.heappushpop(self.heap, entry)

    def get_top_n(self) -> list:
        """
        Get the top n items from the heap
        :return: The top n items
        """
        # Return the items sorted by value in descending order
        return sorted(self.heap, reverse=True)


def get_column_length(text_length: int, key_length: int) -> int:
    """
    Get the length of the columns of the transposition
    :param text_length: the length of the text
    :param key_length: the length of the key
    :return: the length of the column
    """
    assert key_length > 0
    assert text_length > 0
    return math.ceil(text_length / key_length)


def get_all_poss_columns(text: str, key_length: int) -> list[list[str]]:
    """
    Generates the columns of the text based on the length of the possible columns

    :param text: The text itself
    :param key_length: the length of the key
    :return: the columns
    """
    # Get the length of the columns
    base_column_length = len(text) // key_length
    nr_cols_with_extra = len(text) % key_length

    def get_col_length(index: int) -> int:
        """
        Get the length of the column
        :param index: The index of the column
        :return: The length of the column
        """
        return base_column_length + 1 if index < nr_cols_with_extra else base_column_length

    # Calculate all the possible index permutations of the columns
    possible_index_permutation = list(range(key_length))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
    all_index_permutations = [list(p) for p in permutations(possible_index_permutation)]

    # Get all the possible column permutations
    all_permutations = []
    for index_permutation in all_index_permutations:
        temp_text = text
        columns = [""] * key_length

        # Fill the columns in order of the permutation indices
        for col_nr in index_permutation:
            col_length = get_col_length(col_nr)
            columns[col_nr] = temp_text[:col_length]
            temp_text = temp_text[col_length:]
        all_permutations.append(columns)

    return all_permutations


def columns_to_text(columns: list) -> str:
    """
    Convert the columns to text

    :param columns: The columns
    :return: The text
    """
    result_text = ""

    # All full rows
    base_col_length = min(len(col) for col in columns)
    for i in range(base_col_length):
        for col in columns:
            if i >= len(col):
                pass
            result_text += col[i]

    # The last row is sometimes not full
    for col in columns:
        if len(col) > base_col_length:
            result_text += col[-1]
    return result_text


def permutate_columns(columns: list) -> list:
    """
    This function makes permutations of the columns to get all possible combinations

    :param columns: The columns
    :return: The permuted columns
    """
    return [list(p) for p in permutations(columns)]


def find_three_letter_patterns(text) -> dict:
    """
    Find all three-letter patterns that appear more than once in the text.
    :param text: The text itself.
    :return: A dictionary with the three-letter patterns as keys and the number
    of occurrences as values.
    """
    # Use a sliding window to iterate through each three-character substring
    pattern_counts = Counter(text[i:i + 3] for i in range(len(text) - 2))

    # Return only the patterns that appear more than once
    return {pattern: count for pattern, count in pattern_counts.items() if count > 1}


def solve_column_transposition(cipher: str, max_key_length: int) -> list:
    """
    Decrypt the cipher using a column transposition
    :param cipher: The cipher
    :param max_key_length: The max length of the key
    :return: The decrypted text
    """

    stack = TopNStack(50)

    # Values for the progress bar
    i = 0
    total_column_count = sum(factorial(i) for i in range(2, max_key_length + 1))

    for key_length in range(2, max_key_length + 1):
        # Get the columns
        columns = get_all_poss_columns(cipher, key_length)

        for column in columns:
            text = columns_to_text(column)

            # Get the three-letter patterns
            three_letter_patterns: dict = find_three_letter_patterns(text)
            total_duplicates: int = sum(three_letter_patterns.values())

            # If the current solution is better than the best solution, update the best solution
            stack.push(text, (total_duplicates, key_length))

            # Print the progress every once in a while
            if i % 1000 == 0:
                print_progress_bar(i, total_column_count)
            i += 1

    # While the difference between an option and the next best solution is less than 10%,
    # keep adding
    solutions = stack.get_top_n()
    prev_solution = solutions[0]
    results = []
    for solution in solutions:
        if prev_solution[0][0] / solution[0][0] < 1.10:
            results.append(solution[1])
            prev_solution = solution
        else:
            break
    return results
