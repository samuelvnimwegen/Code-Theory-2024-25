"""
This file contains the functions to perform frequency analysis on a text.
"""


def get_frequencies(text: str) -> dict[str, float]:
    from collections import Counter
    """
    Get the letter combination frequencies of some text.

    :param text: The text
    :return: The letter frequencies
    """
    assert len(text) % 2 == 0, "Text length must be even"

    bigram_counts = Counter(text[i:i + 2] for i in range(0, len(text) - 1, 2))
    total = sum(bigram_counts.values())

    sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)
    return {k: round(100 * v / total, 2) for k, v in sorted_bigrams}


def get_frequencies_ngrams(text: list[str], n: int) -> dict[str, float]:
    from collections import Counter
    """
    Get the n-grams of the text.

    :param text: the text
    :param n: the n
    :return: the n-grams
    """
    ngrams = [''.join(text[i:i + n]) for i in range(0, len(text) - n + 1)]
    ngrams = dict(Counter(ngrams))
    total = sum(ngrams.values())
    # Return the percentages, sorted
    return {k: round(100 * v / total, 2) for k, v in sorted(ngrams.items(), key=lambda x: x[1], reverse=True)}


def chi_squared(frequencies: dict[str, float], language: dict[str, float], monogram=True) -> float:
    """
    Calculate the chi-squared value for the frequencies of the text and the frequencies of a language.

    :param frequencies: The frequencies of the text
    :param language: The frequencies of the language
    :param monogram: Whether we are looking at monograms or not.
    :return: The chi-squared value
    """
    # No numbers in text.
    if monogram:
        if len(frequencies) > 26:
            return float('inf')
    # letter differs in frequencies and language
    sum_chi = float(0)
    for i in range(len(frequencies)):
        bigram = list(frequencies.keys())[i]
        letter = list(language.keys())[i]
        sum_chi += ((frequencies[bigram] - language[letter]) ** 2) / language[letter]
    return round(sum_chi, 2)
