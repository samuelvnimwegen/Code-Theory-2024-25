"""
This file is used to load the letter frequencies for the French language.
"""


def load_french_frequencies(file_path: str = "adfgvx/language_files/french_frequencies.txt") -> dict[str, float]:
    """
    Load the letter frequencies for the French language.

    The original file is obtained from, this is an altered version:
    http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/french-letter-frequencies/

    :param file_path: The path to the file containing the letter frequencies
    :return: A dictionary containing the letter frequencies
    """
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split each line into letter and value
            letter, value = line.strip().split()
            if letter not in dictionary:
                dictionary[letter] = float(value)
            else:
                dictionary[letter] += float(value)

    # Sort the dictionary by value
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return dictionary


LETTER_FREQUENCIES_FR: dict[str, float] = load_french_frequencies()
TOTAL_LETTERS_FR: float = sum(LETTER_FREQUENCIES_FR.values())
