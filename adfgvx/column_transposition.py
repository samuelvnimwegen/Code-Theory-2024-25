"""
This module contains the function to perform a column transposition and calculate Chi-squared values
"""


def get_transposition_chi_values(text: str, keys: list[tuple[int, ...]]) -> dict[tuple[int, ...], list[float]]:
    from util.progress_bar import print_progress_bar as pb
    from util.letter_frequency_tables import tables
    """
    Transpose the text using the keys and calculate 

    :param text: the text to be transposed
    :param keys: the list of key orders
    :return: the key orders with their corresponding chi-squared values
    """
    transpositions = dict()
    iteration = 0
    for key in keys:
        # Get transposition
        transposed = transpose(text, key)
        # Calculate Frequencies
        frequencies = get_letter_frequencies(transposed)
        # Calculate Chi-Squared value
        chi_values = []
        for table in tables:
            xi_squared = get_xi_squared_value(frequencies, table)
            chi_values.append(xi_squared)
        transpositions[key] = chi_values
        if iteration % 10000 == 0:
            pb(iteration, len(keys))
        iteration += 1
    return transpositions


def transpose(text, key: tuple[int, ...]) -> str:
    """
    Transpose the text using the key

    :param text: The text
    :param key: The key
    :return: The transposed text
    """
    transposed_list = ["" for _ in range(len(key))]
    # Add the text to the right column
    for i, char in enumerate(text):
        transposed_list[i % len(key)] += char
    # Add the columns
    transposed = str()
    for i in range(len(key)):
        index = key.index(i)
        transposed += transposed_list[index]
    return transposed


def get_letter_frequencies(text) -> dict[str, float]:
    from collections import Counter
    """
    Get the letter combination frequencies of some text.

    :param text: The text
    :return: The letter frequencies
    """
    text_length = len(text)/2
    text = [text[i:i+2] for i in range(0, len(text) - 1, 2)]
    # Sort the occurences
    occurences = list(Counter(text).items())
    occurences.sort(key=lambda x: x[1], reverse=True)

    # Return it in dict format
    return {letter: round(letter_count / text_length * 100, 2) for letter, letter_count in occurences}


def get_xi_squared_value(frequencies, expected_frequencies) -> float:
    """
    Get the xi squared value of two frequency dictionaries

    :param frequencies: The frequencies
    :param expected_frequencies: The expected frequencies
    :return: The xi squared value
    """
    # Calculate for 10 highest frequencies
    xi_squared = 0
    for i in range(10):
        observed = frequencies[list(frequencies.keys())[i]]
        expected = expected_frequencies[list(expected_frequencies.keys())[i]]
        xi_squared += ((observed - expected) ** 2) / expected
    return xi_squared