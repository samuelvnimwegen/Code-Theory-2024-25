"""
This module contains the functions to perform a column transposition.
"""


def get_original_transposition(text: str, key_length: int) -> tuple[int, ...]:
    from adfgvx.frequency_analysis import get_frequencies
    from adfgvx.frequency_analysis import chi_squared
    from util.letter_frequency_table import tables
    import itertools
    """
    Calculates all column transpositions and returns the best result using chi-squared analysis.
    We know there will be 1 transposition that stands out by having at most 26 different characters.
    Chi-squared analysis will return infinity for more than 26 characters and we will skip these transpositions.

    :param text: the text to be transposed
    :param key_length: the length of the key
    :return: the original transposition and the chi-squared values
    """
    for i in range(1, key_length + 1):
        print(f"Calculating transpositions for key length {i}.")
        # Get permutations of i numbers from 0 to i
        keys = list(itertools.permutations(range(i)))
        for key in keys:
            # Get transposition
            normal = reverse_transpose(text, key)
            # Get frequencies of text
            frequencies = get_frequencies(normal)
            # Calculate chi-squared value
            chi = [chi_squared(frequencies, table) for table in tables]
            # Chi-squared function will return infinity if there are more than 26 characters
            if not any([c == float('inf') for c in chi]):
                print(f"Transposition key found: {key}")
                return key
    raise ValueError('No transpositions found for max length: ' + str(key_length))


def reverse_transpose(text, key: tuple[int, ...]) -> str:
    """
    Reverse the transposition the text using the key

    :param text: The transposed text
    :param key: The key
    :return: The original text
    """
    text_len = len(text)
    amount_of_keys = len(key)

    # Calculate the number of characters in each column
    base_length = text_len // amount_of_keys
    remainder = text_len % amount_of_keys

    # Get the amount of letters for each part of the key
    amount_of_letters = {key[i]: base_length + (1 if i < remainder else 0) for i in range(amount_of_keys)}

    transposed_list = [''] * amount_of_keys
    for i in range(amount_of_keys):
        # Get first amount_of_letters[i] characters from string
        transposed_list[i] = text[0:amount_of_letters[i]]
        # Remove first amount_of_letters[i] characters from string
        text = text[amount_of_letters[i]:]

    # Build transposed string
    transposed = []
    for i in range(text_len // amount_of_keys + 1):
        for j in key:
            if i < len(transposed_list[j]):
                transposed.append(transposed_list[j][i])
    return ''.join(transposed)
