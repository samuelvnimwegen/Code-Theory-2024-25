
from language_info.letter_frequency_table import *
from language_info.most_common_words import *
from ..playfair.playfair import Playfair

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
        frequencies = languages[language]

        score = 0
        for letter in frequencies.keys():
            if letter == 'X' or letter == 'J':
                continue
            letter_count = text.count(letter)
            text_frequency = letter_count / (total_count - X_count)
            score -= abs(text_frequency - frequencies[letter][0])

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
        for word in common_words:
            if word in text:
                score += 1

        score_language_dict[language] = score

    return score_language_dict


def score_weighted_average(cipher_text: str, cipher_obj: Playfair) -> (float, str):
    decrypted_text = cipher_obj.decrypt(cipher_text)

    score_frequency_dict = score_frequencies(decrypted_text)
    score_common_words_dict = score_common_word_count(decrypted_text)

    score_language_dict = dict()
    for language in languages.keys():
        score_language_dict[language] = (score_frequency_dict[language] + (2*score_common_words_dict[language])) / 3

    sorted_dict = dict(sorted(score_language_dict.items(), key=lambda item: item[1], reverse=True))

    first_item = next(iter(sorted_dict.items()))
    return first_item




