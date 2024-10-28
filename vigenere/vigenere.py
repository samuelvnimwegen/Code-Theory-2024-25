"""
This file is made to decypher a vigenere cipher
"""

import json
from util.progress_bar import print_progress_bar
from collections import Counter
from vigenere.transposition import find_three_letter_patterns, TopNStack
from util.letter_frequency_table import ENGLISH, DUTCH, ALL_LANGUAGE_FREQUENCIES, GERMAN, FRENCH, SPANISH, ITALIAN, \
    PORTUGUESE, TURKISH, SWEDISH, POLISH


def get_indices(text: str, segment: str):
    """
    Get the indices of a segment in a text.
    :param text: The text
    :param segment: the segment
    :return: The indices
    """
    indices = []
    segment_length = len(segment)
    for i in range(len(text)):
        if text[i:i + segment_length] == segment:
            indices.append(i)
    return indices


def get_index_spacing(text: str, segments: list[str]) -> list[int]:
    """
    Get the index spacing of segments in a text.
    :param text: The text
    :param segments: the segments
    :return: The list with total spacings
    """
    total_spacings = []
    for segment in segments:
        indices = get_indices(text, segment)
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                total_spacings.append(indices[j] - indices[i])
    return sorted(total_spacings)


def check_dividers(spacings: list[int], max_key_len: int = 10) -> dict[int, int]:
    """
    Check the dividers of the spacings

    :param spacings: The list with spacings
    :param max_key_len: The maximum key length
    :return: A dictionary with the key length and the number of dividers
    """
    dividers = {}
    for i in range(2, max_key_len + 1):
        dividers[i] = 0
        for spacing in spacings:
            if spacing % i == 0:
                dividers[i] += 1
    return dividers


def get_sequence_frequencies(input_file: str, output_file: str):
    # TODO: Write tests for this function
    """
    Get the frequencies of the dividers of the spacings

    :param input_file: The input file
    :param output_file: The output file
    """
    with open(input_file, "r") as file:
        data = json.load(file)

    frequencies = []
    i = 0
    length = len(data)
    for item in data:
        index = item[0]
        data = json.loads(item[1])
        keys = list(data["three_letter_patterns"].keys())
        spacings = get_index_spacing(segments=keys, text=data["text"])
        dividers = check_dividers(spacings)
        frequencies.append(dividers)
        i += 1
        if i % 100 == 0:
            print_progress_bar(i, length)

    with open(output_file, "w") as file:
        file.write(json.dumps(frequencies))


def print_frequencies() -> None:
    """
    Print the frequencies of the dividers
    :return: None
    """
    # TODO: Write tests for this function
    with open("vigenere/three-part-segments/distances_table.txt", "r") as file:
        data = json.load(file)

    maxes: dict = {}
    for freq_index in range(len(data)):
        frequency_dict = data[freq_index]
        for i in range(2, 11):
            if i not in maxes.keys() or frequency_dict[str(i)] > maxes[i]["frequencies"][str(i)]:
                maxes[i] = {
                    "frequencies": frequency_dict,
                    "frequency_index": freq_index
                }

    for max_key in maxes.keys():
        occurrences = maxes[max_key]["frequencies"][str(max_key)]

        print(f"{max_key}:", round(occurrences / 305 * 100, 2), "%, index:", maxes[max_key]["frequency_index"])


def most_used_letter(text: str) -> tuple[str, int]:
    """
    Find the most used letter in a string
    :param text: The text
    :return: A tuple with the most used letter and the count
    """
    # Get the frequency of each letter
    letter_counts = Counter(text)

    # Find the most common letter
    most_common_letter, count = letter_counts.most_common(1)[0]
    return most_common_letter, count


def alphabet_difference(char1: str, char2: str) -> str:
    """
    Calculate the difference between two letters in the alphabet
    :param char1: Character 1
    :param char2: Character 2
    :return: The character difference, for example, 'B' and 'F' would return 'E' because 'B' + 'E' = 'F'
    """
    # Convert letters to positions (0 for 'A', 4 for 'E', etc.)
    pos1 = ord(char1.upper()) - ord('A')
    pos2 = ord(char2.upper()) - ord('A')

    # Calculate difference and apply modulo 26
    difference = (pos2 - pos1) % 26

    # Convert position back to letter
    result_letter = chr(difference + ord('A'))
    return result_letter


def find_best_shift(segment, expected_frequencies) -> str:
    """
    Finds the best shift for a given frequency segment to minimize the chi-squared value
    compared to English letter frequencies.
    """
    # TODO: Write tests for this function
    # Get initial frequencies of the segment
    frequencies_segment = get_letter_frequencies(segment)
    best_xi_squared = float('inf')
    best_shift = 0

    for shift in range(26):
        # Shift frequencies by 'shift' amount and calculate χ² value
        shifted_frequencies = {
            chr((ord(letter) - ord('A') + shift) % 26 + ord('A')): frequency
            for letter, frequency in frequencies_segment.items()
        }
        xi_squared = get_xi_squared_value(shifted_frequencies, expected_frequencies)

        # Update if this shift has a lower χ² value
        if xi_squared < best_xi_squared:
            best_xi_squared = xi_squared
            best_shift = shift

    # Return the best shift letter
    best_shift_letter = chr(ord('A') + 26 - best_shift)
    return best_shift_letter


def get_key(cipher: str, key_len: int, language: dict) -> str:
    """
    Try to find the key value for a given key length

    :param language: The language
    :param cipher: The cipher
    :param key_len: The key length
    :return: The key value
    """
    key = ""
    for i in range(key_len):
        # Get the segment of all characters that are one key length apart
        segment = ""
        for j in range(i, len(cipher), key_len):
            segment += cipher[j]
        key_letter = find_best_shift(segment, language)
        key += key_letter
    return key


def decrypt_vigenere(cipher: str, key: str) -> str:
    """
    Fill in the key in the cipher

    :param cipher: The cipher
    :param key: The key
    :return: The filled in cipher
    """
    key_length = len(key)
    decrypted_text = ""
    for i, char in enumerate(cipher):
        # Get the position of the current cipher character and key character
        cipher_pos = ord(char) - ord('A')
        key_pos = ord(key[i % key_length]) - ord('A')

        # Decrypt by reversing the key's shift
        decrypted_char = chr(((cipher_pos - key_pos + 26) % 26) + ord('A'))
        decrypted_text += decrypted_char

    return decrypted_text


def get_letter_frequencies(text) -> dict[str, float]:
    """
    Get the letter frequencies of a text.
    :param text: The text
    :return: The letter frequencies
    """
    text_length = len(text)

    # Make a sorted list
    sorted_list = [(letter, letter_count) for letter, letter_count in Counter(text).items()]
    sorted_list.sort(key=lambda x: x[1], reverse=True)

    # Return it in dict format
    return {letter: round(letter_count / text_length * 100, 2) for letter, letter_count in sorted_list}


def get_xi_squared_value(frequencies, expected_frequencies) -> float:
    """
    Get the xi squared value of two frequency dictionaries
    :param frequencies: The frequencies
    :param expected_frequencies: The expected frequencies
    :return: The xi squared value
    """
    xi_squared = 0
    for letter in frequencies.keys():
        observed = frequencies[letter]
        expected = expected_frequencies[letter]
        xi_squared += ((observed - expected) ** 2) / expected
    return xi_squared


def solve_vigenere(crypt: str, key_len: int, language: dict) -> str:
    """
    Solve the vigenere cipher
    :param language: The language
    :param crypt: The cipher
    :param key_len: The key length
    :return: The solved cipher
    """
    # TODO Write tests for this function
    key = get_key(crypt, key_len, language)
    return decrypt_vigenere(crypt, key)


if __name__ == "__main__":
    with open("vigenere/three-part-segments/output_10k.txt", "r") as file:
        data = json.load(file)
    LANGUAGE = POLISH
    stack = TopNStack(1)
    max_val = 5400
    for i in range(max_val):
        item = data[0]
        for j in range(2, 11):
            key_len = j
            crypt = item[1][1]

            key = get_key(crypt, key_len, LANGUAGE)
            solved = decrypt_vigenere(crypt, key)
            frequencies = get_letter_frequencies(solved)
            min_xi = float("inf")
            xi_squared = get_xi_squared_value(frequencies, LANGUAGE)
            stack.push(json.dumps({
                "key": key,
                "solved": solved,
            }), -xi_squared)

        if i % 100 == 0:
            print_progress_bar(i, max_val)
    print(stack.get_top_n()[0])
    with open(f"vigenere/three-part-segments/solutions_polish.txt", "w") as file:
        file.write(json.dumps(stack.get_top_n()))
