"""
This file is used to crack the column transposition of the vigenere+ cipher
"""
import json
import math

from util import filestream
from util.progress_bar import print_progress_bar
from itertools import permutations
from collections import Counter
import heapq

code: str = filestream.load_file("codes/01-OPGAVE-viginereplus.txt")


class TopNStack:
    def __init__(self, max_elements: int):
        # Initialize an empty min-heap
        self.heap = []
        self.max_elements = max_elements

    def push(self, item, value):
        # Create a tuple (value, item) to store in the heap
        entry = (value, item)

        # Add the item to the heap
        if len(self.heap) < self.max_elements:
            # If heap has less than 10 items, push the new entry
            heapq.heappush(self.heap, entry)
        else:
            # If the heap has 10 items, push and pop in one step to maintain the top 10 values
            heapq.heappushpop(self.heap, entry)

    def get_top_n(self):
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


def get_columns(text: str, key_length: int) -> list:
    """
    Generates the columns of the transposition

    :param text: The text itself
    :param key_length: the length of the key
    :return: the columns
    """
    # Pad the text with * characters
    while len(text) % key_length != 0:
        text += "*"

    # Create the columns
    columns = ["" for _ in range(key_length)]

    # Divide the text into columns
    text_length = len(text)
    for i in range(text_length):
        columns[i % key_length] += text[i]
    return columns


def columns_to_text(columns: list) -> str:
    """
    Convert the columns to text

    :param columns: The columns
    :return: The text
    """
    result_text = ""

    # Concatenate the columns
    for column in columns:
        result_text += column

    # Remove * characters
    result_text = result_text.replace("*", "")
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
    :return: A dictionary with the three-letter patterns as keys and the number of occurrences as values.
    """
    # Use a sliding window to iterate through each three-character substring
    pattern_counts = Counter(text[i:i + 3] for i in range(len(text) - 2))

    # Return only the patterns that appear more than once
    return {pattern: count for pattern, count in pattern_counts.items() if count > 1}


if __name__ == "__main__":
    # For all the possible key lengths, get all the possible output texts
    stack = TopNStack(10000)
    for key_length in range(2, 11):
        print(key_length, ": ")
        columns = get_columns(code, key_length)
        permuted_columns = permutate_columns(columns)
        i = 0
        permutation_amount = len(permuted_columns)
        for permuted_columns in permuted_columns:
            text: str = columns_to_text(permuted_columns)
            three_letter_patterns: dict = find_three_letter_patterns(text)
            total_duplicates: int = sum(three_letter_patterns.values())
            item = tuple([key_length, text])
            stack.push(item, total_duplicates)

            # Update the progress bar every 0.1% of the total permutations
            if i % 10000 == 0:
                print_progress_bar(i, permutation_amount)

            i += 1
    results = stack.get_top_n()
    # write the data to a file
    with open("output.txt", "w") as file:
        file.write(json.dumps(stack.get_top_n()))
    print("Done")
