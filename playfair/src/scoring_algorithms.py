from collections import Counter
from math import log10

from playfair.src.language_info.letter_frequency_table import *
from playfair.src.language_info.most_common_words import *
from playfair.src.playfair import Playfair
from playfair.src.utils.utils import norm_2
from playfair.src.language_info.utils_4gram_EN import binary_search_4grams, total_4grams
from playfair.src.language_info.letter_freq_table_playfair import ENGLISH_PLAYFAIR

# Scoring algorithms to give a score to a decrypted text

# Idea:
# Use the frequency table to give a score and determine the language
        # For each of the 6 languages:
            # count frequency of letters (without X) and compare with expected frequency
# With the chosen language, use 500 most common words to give another score
        # for each common word, give point if present in text
# Take weighted average of both scores, but with increased weight for second score as common words are more powerful
# return score and used language


# No dutch: "DU": DUTCH as no 500 common words provided
languages = {
    "EN": (ENGLISH, EN),
    "SP": (SPANISH, SP),
    "GE": (GERMAN, GE),
    "FR": (FRENCH, FR),
    "IT": (ITALIAN, IT),
}


def score_frequencies(text: str) -> dict:
    """
    Calculate a score for the text for each language
    Use the expected and actual letter frequency. The higher the score, the better
    :param text: the text to score
    :return: dictionary with each language's score
    """
    X_count = text.count("X")
    total_count = len(text)

    score_language_dict = dict()

    for language in languages.keys():
        frequencies = languages[language][0]

        score = 100
        for letter in frequencies.keys():
            if letter == 'X' or letter == 'J':
                continue
            letter_count = text.count(letter)
            text_frequency = letter_count / (total_count - X_count)
            score = score - abs(text_frequency - frequencies[letter])

        score_language_dict[language] = score

    return score_language_dict


def score_common_word_count(text: str) -> dict:
    """
    Calculate a score for the text for each language
    Use the count of the most common words. The higher the score, the better
    :param text: the text to score
    :return: dictionary with each language's score
    """
    score_language_dict = dict()

    for language in languages.keys():
        common_words = languages[language][1]
        score = 0
        text_lower = text.lower()
        for word in common_words:
            if word in text_lower:
                #score += text_lower.count(word)
                score += 1

        score_language_dict[language] = score

    return score_language_dict


def score_weighted_average(cipher_text: str, cipher_obj: Playfair) -> (str, float):
    """
    Calculate a score for the decrypted text based on a weighted average of scoring using letter frequencies
    and scoring using presence common word.
    :param cipher_text: the text to decrypt
    :param cipher_obj: Object to use to decrypt the cipher text
    :return: score and detected language
    """
    decrypted_text = cipher_obj.decrypt(cipher_text)

    score_frequency_dict = score_frequencies(decrypted_text)
    score_common_words_dict = score_common_word_count(decrypted_text)

    score_language_dict = dict()
    for language in languages.keys():
        score_language_dict[language] = (score_frequency_dict[language] + (2*score_common_words_dict[language])) / 3

    sorted_dict = sorted(score_language_dict.items(), key=lambda item: item[1], reverse=True)

    first_item = sorted_dict[0]
    return first_item


def score_trigrams_count(cipher_text: str, cipher_obj: Playfair) -> (str, float):
    """
    Split the text in trigrams (triples) and count how many times each trigram appears.
    Each extra HIT (excl: 1 for presence) is counted in score.
    :param cipher_text: Text to decrypt
    :param cipher_obj: Cipher object to decrypt and then score the decrypted text
    :return: the score
    """
    # decrypted_text = cipher_obj.decrypt(cipher_text)
    #
    # text_lower = decrypted_text.lower()
    #
    # # Make length divisible by 3
    # text_lower += 'x' * (len(cipher_text) % 3)
    # # Create a set of unique trigrams
    # unique_trigrams: set[str] = {text_lower[i*3:i*3 + 3] for i in range(len(text_lower)//3)}
    #
    # score = 0
    # for trigram in unique_trigrams:
    #     if trigram in text_lower:
    #         score += text_lower.count(trigram) - 1
    #
    # percentage_score = score / (len(decrypted_text) // 3)
    #
    # return "no_language", percentage_score

    decrypted_text = cipher_obj.decrypt(cipher_text)
    text_lower = decrypted_text.lower()

    # Make length divisible by 3
    text_lower += 'x' * (len(cipher_text) % 3)
    # Create a set of unique trigrams
    trigrams: list[str] = [text_lower[i * 3:i * 3 + 3] for i in range(len(text_lower) // 3)]

    unique_trigrams: set[str] = {trigrams[i] for i in range(len(trigrams))}

    score = 0
    for trigram in unique_trigrams:
        score += trigrams.count(trigram) - 1

    percentage_score = score / (len(trigrams))
    print(f"triples count : {score}")
    print(f"aantal triples: {len(trigrams)}")

    return "no_language", percentage_score


def score_three_letter_patterns(cipher_text: str, cipher_obj: Playfair, decrypt_text=True) -> (str, float):
    """
    Decrypt the text using the cipher object.
    Find all three letter patterns in the decrypted text and count there appearance (if more than 1)
    :param cipher_text: Text to decrypt
    :param cipher_obj: Cipher object to decrypt the text (contains keyword)
    :param decrypt_text: boolean value if the text needs to be decrypted first
    :return: A percentage value of all appearances relative to the length of the text
    """
    text_to_score = cipher_text
    if decrypt_text:
        text_to_score = cipher_obj.decrypt(cipher_text)

    # Remove all X values (there could be actual X's in the plain text, but low frequency)
    text_no_x = text_to_score.replace("X", "")

    # use sliding window to find all three character substrings and count each
    three_letter_counts = Counter(text_no_x[i:i+3] for i in range(len(text_no_x) - 2))

    pattern_dict = {pattern: count for pattern, count in three_letter_counts.items() if count > 1}

    total_patterns = sum(pattern_dict.values())
    text_length = len(text_no_x)
    percentage = total_patterns / text_length
    return "no_language", percentage


def score_frequencies_english(cipher_text: str, cipher_obj: Playfair, decrypt_text=True) -> (str, float):
    """
    After meeting with Mr. Symens -> Plaintext is in English
    Frequencies are best scoring method
    :param cipher_text: Text to decrypt
    :param cipher_obj: Cipher object to decrypt the text (contains keyword)
    :param decrypt_text: boolean value if the text needs to be decrypted first
    :return: 1 - score: better score is higher than worse scores
    """
    text_to_score = cipher_text
    if decrypt_text:
        text_to_score = cipher_obj.decrypt(cipher_text)

    # Remove all X values (there could be actual X's in the plain text, but low frequency)
    # The X frequency is removed from the letter frequencies
    text_no_x = text_to_score.upper().replace("X", "")

    # Take for each letter the difference between the text frequency and the expected frequency
    letter_frequency_diff = []
    for letter, freq in ENGLISH_PLAYFAIR.items():
        if letter == 'X' or letter == 'J':
            continue
        letter_count = text_no_x.count(letter)
        text_frequency = letter_count / (len(text_no_x))
        expected_frequency = freq   # Divide by 100 to change percentage value to decimal value (0,100) range
        letter_frequency_diff.append(text_frequency - expected_frequency)

    # Take the second norm of the vector
    norm = norm_2(letter_frequency_diff)

    # Take difference from 1, so that better scores are higher than worse scores
    return "EN", 1-norm


def score_four_gram_statistics(cipher_text: str, cipher_obj: Playfair, decrypt_text=True) -> (str, float):
    """
    heuristic that uses 4-grams and their statistic probabilities in the English language
    :param cipher_text: Text to decrypt
    :param cipher_obj: Cipher object to decrypt the text (contains keyword)
    :param decrypt_text: boolean value if the text needs to be decrypted first. if False, the cipher text can be interpreted as Plaintext
    :return: language: str, score: float. The language is definitely English (EN)
    """
    # To prevent underflow with small float numbers, we'll work with log10
    prob_log = 0

    # If needed, decrypt the text
    text_to_score = cipher_text
    if decrypt_text:
        text_to_score = cipher_obj.decrypt(cipher_text)

    # Remove all X values (there could be actual X's in the plain text, but low frequency)
    text_no_x = text_to_score.upper().replace("X", "")

    # Last 3 indices not necessary, as we need 4grams of i, i+1, i+2, i+3
    for index in range(len(text_no_x) - 3):
        four_gram = text_no_x[index:index+4]

        # Get frequency count of the gram and calculate probability in log10
        count = binary_search_4grams(four_gram)
        probability = count / total_4grams
        if probability > 0:
            prob_log += log10(probability)

    return "EN", prob_log









