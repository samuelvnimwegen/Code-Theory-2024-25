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
    """
    Get the n-grams of the text.

    :param text: the text
    :param n: the n
    :return: the n-grams
    """
    ngrams = dict()
    for i in range(len(text) - n + 1):
        ngram = text[i:i + n]
        ngram = ''.join(ngram)
        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1
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
    # Print the key, text (before and after transposition), frequencies of the text and frequencies of the closest language.
    print("Key found: " + str(key))
    print("Original Text: " + data_old)
    print("Text: " + data_new)
    frequencies = get_frequencies(data_new)
    print("Frequencies: " + str(frequencies))
    language = 0
    for i in range(len(chi)):
        if chi[i] < chi[language]:
            language = i
    print("Language: " + str(tables[language]))
    print("Language Selected: " + tables_names[language])
    # Split letters into pairs of 2
    text = [data_new[i:i + 2] for i in range(0, len(data_new), 2)]
    # Substitute the letters with the letters from the language with similar frequencies.
    substitute_monogram(text, frequencies, tables[language])
    # Perform n-gram analysis.
    ngram_analysis(text, 10, language)
    # Save this text.
    new_text = text.copy()
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
            text = new_text.copy()
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


def substitute_monogram(text: list[str], frequencies: dict[str, float], language: dict[str, float]):
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


def substitute(text: list[str], a: str, b: str):
    """
    Substitute a with b in the text.

    :param text: the text
    :param a: the letter to substitute
    :param b: the letter to substitute with
    """
    for i in range(len(text)):
        if text[i] == a:
            text[i] = b
        elif text[i] == b:
            text[i] = a


def ngram_analysis(text: list[str], n: int, language: int):
    from util.ngram_frequency_table import get_frequencies as get_expected_ngrams
    """
    Frequency analysis using ngrams

    :param text: the text
    :param n: the highest number of n-gram
    :param language: the index of the language
    :return:
    """
    languages = ["english", "french", "german", "dutch", "spanish", "italian"]
    language = languages[language]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if n == 1:
        return
    expected_frequencies = dict[str, float]()
    while n > 1:
        # Get expected bigrams
        get_expected_ngrams(language, n, expected_frequencies)
        if len(expected_frequencies) != 0:
            break
        # If returned frequencies are empty, decrease n
        if len(expected_frequencies) == 0:
            n -= 1
            continue
    if len(expected_frequencies) == 0:
        return
    # Simulated annealing
    ...
    # match n:
    #     case 2:
    #         frequencies = dict[str, float]()
    #         # Get the expected bigrams
    #         get_expected_ngrams(language, 2, frequencies)
    #         return
    #         # Hill climbing
    #         # TODO: Have to use something other than chi-squared value.
    #         old_chi = chi_squared(get_frequencies_ngrams(text, 2), bigrams[language], monogram=False)
    #         new_chi = old_chi + 1
    #         while new_chi != old_chi:
    #             for i in range(len(letters)):
    #                 for j in range(len(letters)):
    #                     if i == j:
    #                         continue
    #                     # Swap the letters
    #                     substitute(text, letters[i], letters[j])
    #                     # Calculate new chi-squared value
    #                     frequencies = get_frequencies_ngrams(text, 2)
    #                     chi = chi_squared(frequencies, bigrams[language], monogram=False)
    #                     if new_chi < chi:
    #                         new_chi = chi
    #                     else:
    #                         # Swap back
    #                         substitute(text, letters[i], letters[j])
    #         ...
    #         copy_bigrams = copy.deepcopy(bigrams)
    #         letters = []
    #         for i in range(len(ngrams)):
    #             # Get ngram from text
    #             ngram1 = list(ngrams.keys())[i]
    #             for j in range(len(copy_bigrams)):
    #                 ngram2 = list(bigrams[language].keys())[j]
    #                 # Check if the letters in n-gram correspond
    #                 num1 = []
    #                 num2 = []
    #                 l1 = []
    #                 l2 = []
    #                 for k in range(len(ngram1)):
    #                     # Index the letters so they'll be mapped together
    #                     if ngram1[k] not in num1:
    #                         num1.append(ngram1[k])
    #                     if ngram2[k] not in num2:
    #                         num2.append(ngram2[k])
    #                     # Add index to list
    #                     l1.append(num1.index(ngram1[k]))
    #                     l2.append(num2.index(ngram2[k]))
    #                 # If they are not the same that means we cannot substitute between them
    #                 # For example "ab" and "aa" or "aee" and "eae"
    #                 if l1 != l2:
    #                     continue
    #                 ...
    #     case _:
    #         raise NotImplementedError("{}-grams are not (yet) supported!".format(n))