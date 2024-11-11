"""
This module contains the functions to perform a column transposition and calculate Chi-squared values
"""

from adfgvx.frequency_analysis import get_letter_frequencies


def get_transposition_chi_values(text: str, keys: list[tuple[int, ...]]) -> dict[tuple[int, ...], list[float]]:
    from util.progress_bar import print_progress_bar as pb
    from util.letter_frequency_table import tables
    """
    Transpose the text using the keys and calculate 

    :param text: the text to be transposed
    :param keys: the list of key orders
    :return: the key orders with their corresponding chi-squared values
    """
    transpositions = {}
    for iteration, key in enumerate(keys):
        # Get transposition
        transposed = reverse_transpose(text, key)
        # Calculate Frequencies
        frequencies = get_letter_frequencies(transposed)
        # Calculate Chi-Squared value
        chi_values = [get_xi_squared_value(frequencies, table) for table in tables]
        transpositions[key] = chi_values
        if iteration % 10000 == 0:
            pb(iteration, len(keys))
    return transpositions


def reverse_transpose(text, key: tuple[int, ...]) -> str:
    """
    Transpose the text using the key

    :param text: The text
    :param key: The key
    :return: The transposed text
    """
    text_len = len(text)
    amount_of_keys = len(key)

    # Calculate the number of characters in each column
    base_length = text_len // amount_of_keys
    remainder = text_len % amount_of_keys

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


def get_xi_squared_value(frequencies, expected_frequencies) -> float:
    """
    Get the xi squared value of two frequency dictionaries

    :param frequencies: The frequencies
    :param expected_frequencies: The expected frequencies
    :return: The xi squared value
    """
    xi_squared = sum(((observed - expected) ** 2) / expected for observed, expected in zip(frequencies.values(), expected_frequencies.values()))
    return xi_squared