"""
This file contains the functions to perform frequency analysis on a text.
"""
import itertools


def get_frequencies(text) -> dict[str, float]:
    from collections import Counter
    """
    Get the letter combination frequencies of some text.

    :param text: The text
    :return: The letter frequencies
    """
    assert len(text) % 2 == 0, "Text length must be even"

    ngram_counts = Counter(text[i:i + 2] for i in range(0, len(text) - 1, 2))
    total = sum(ngram_counts.values())

    sorted_bigrams = sorted(ngram_counts.items(), key=lambda x: x[1], reverse=True)
    return {k: round(100 * v / total, 2) for k, v in sorted_bigrams}


def chi_squared(frequencies: dict[str, float], language: dict[str, float]) -> float:
    """
    Calculate the chi-squared value for the frequencies of the text and the frequencies of a language.

    :param frequencies: The frequencies of the text
    :param language: The frequencies of the language
    :return: The chi-squared value
    """
    # No numbers in text.
    if len(frequencies) > 26:
        return float('inf')
    # letter differs in frequencies and language
    sum_chi = float(0)
    for i in range(len(frequencies)):
        bigram = list(frequencies.keys())[i]
        letter = list(language.keys())[i]
        sum_chi += ((frequencies[bigram] - language[letter]) ** 2) / language[letter]
    return round(sum_chi, 2)


def frequency_analysis(data_old: str, data_new: str, chi: list[float], key: tuple[int, ...]) -> str:
    from util.letter_frequency_table import tables, tables_names
    """
    Perform frequency analysis on the text.

    :param data_old: the text before transposition
    :param data_new: the text after transposition
    :param chi: the chi-squared values for each language
    :param key: the key used for transposition
    :return:
    """
    # Print the text, frequencies of the text and frequencies of the closest language.
    print("Key found: " + str(key))
    print("Original Text: " + data_old)
    print("Text: " + data_new)
    frequencies = get_frequencies(data_new)
    print("Frequencies: " + str(frequencies))
    lowest = 0
    for i in range(len(chi)):
        if chi[i] < chi[lowest]:
            lowest = i
    print("Language: " + str(tables[lowest]))
    print("Language Selected: " + tables_names[lowest])
    # Split letters into pairs of 2
    text = [data_new[i:i + 2] for i in range(0, len(data_new), 2)]
    # Substitute the letters with the letters from the language with similar frequencies.
    substitute(text, frequencies, tables[lowest])
    text_substituted = text.copy()
    print("Options:")
    print("\"X Y\" - swaps X with Y")
    print("\"Exit\" - exits the frequency analysis")
    print("\"Reset\" - resets the text")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        print("Text: " + ''.join(text))
        choice = input("")
        # Exit
        if choice == "Exit":
            return ''.join(text)
        if choice == "Reset":
            text = text_substituted.copy()
            continue
        # Check if the choice is valid.
        if len(choice) != 3 or choice[1] != ' ' or choice[0] not in alphabet or choice[2] not in alphabet:
            print("Invalid choice.")
            continue
        if choice[0] not in text and choice[2] not in text:
            print("Invalid choice.")
            continue
        # Swap the letters.
        for i in range(len(text)):
            if text[i] == choice[0]:
                text[i] = choice[2]
            elif text[i] == choice[2]:
                text[i] = choice[0]


def substitute(text: list[str], frequencies: dict[str, float], language: dict[str, float]):
    """
    Substitute the monograms in the text.

    :param text: the text to substitute
    :param frequencies: the frequencies of the text
    :param language: the frequencies of the monograms in the language
    :return:
    """
    for i in range(len(frequencies)):
        letter = list(language.keys())[i].lower()
        for j in range(len(text)):
            if text[j] == list(frequencies.keys())[i]:
                text[j] = letter