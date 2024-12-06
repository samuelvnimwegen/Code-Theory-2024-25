"""
This file loads the quad grams for the French language.

The quad gram file itself was obtained from:
http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/french-letter-frequencies/
"""

import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize the text by removing accents and other diacritics.
    :param text: The text to normalize
    :return: The normalized text
    """
    # Normalize the text to NFD (Canonical Decomposition) form
    normalized = unicodedata.normalize('NFD', text)

    # Remove all combining marks (accents)
    stripped = ''.join(c for c in normalized if not unicodedata.combining(c))
    return stripped


def load_quad_grams_fr(file_path="adfgvx/language_files/french_quadgrams.txt") -> dict[str, int]:
    """
    Load the quad grams for the French language.
    """
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split each line into word and value
            word, value = line.strip().split()
            word = normalize_text(word)
            dictionary[word] = int(value)
    return dictionary


FR_QUAD_GRAM_DICT: dict[str, int] = load_quad_grams_fr()
FR_TOTAL_QUAD_GRAMS: int = sum(FR_QUAD_GRAM_DICT.values())
