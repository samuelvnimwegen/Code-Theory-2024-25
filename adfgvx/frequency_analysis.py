"""
This file contains the functions to perform frequency analysis on a text.
"""

def get_letter_frequencies(text) -> dict[str, float]:
    from collections import Counter
    """
    Get the letter combination frequencies of some text.

    :param text: The text
    :return: The letter frequencies
    """
    bigram_counts = Counter(text[i:i + 2] for i in range(0, len(text) - 1, 2))
    total = sum(bigram_counts.values())

    sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)
    return {k: round(100 * v / total, 2) for k, v in sorted_bigrams}



def loop_over_lowest_chi_squared(data: str, perms: list[tuple[int, ...]], transpositions: dict[tuple[int, ...], list[float]]):
    from util.letter_frequency_table import tables_names as languages
    """
    Loop over the key orders with the lowest chi-squared values.
    :param perms: All permutations for the key orders
    :param transpositions: The key orders with their corresponding chi-squared values
    :return:
    """
    lowest_done = []
    while True:
        if len(lowest_done) >= len(perms * len(languages)):
            break
            # Get the key order with the lowest chi-squared value.
        lowest = ((0,), float('inf'), 0)
        for key in perms:
            for chi in transpositions[key]:
                # If the chi-squared value is lower than the current lowest chi-squared value.
                if chi < lowest[1]:
                    # If the key order is already done, skip.
                    if (key, chi, transpositions[key].index(chi)) in lowest_done:
                        continue
                    # Set the new lowest chi-squared value.
                    lowest = (key, chi, transpositions[key].index(chi))
        # Add to lowest_done
        lowest_done.append(lowest)
        # Print the key order with the lowest chi-squared value.
        print("Key order with lowest chi-squared value: " + str(lowest[0]) + " with value: " + str(lowest[1]) + " for language: " + languages[lowest[2]])
        while True:
            # Print options
            print("Options:")
            print("1. Continue to next lowest chi-squared value")
            print("2. Try frequency analysis")
            print("3. Exit")
            choice = input("")
            # Continue to next lowest chi-squared value
            if choice == "1":
                break
            elif choice == "2":
                frequency_analysis(data, lowest)
            # Exit program
            elif choice == "3":
                return
            else:
                print("Invalid choice.")



def frequency_analysis(data: str, lowest: tuple[tuple[int, ...], float, int]):
    import copy
    from adfgvx.column_transposition import reverse_transpose as transpose
    from util.letter_frequency_table import tables
    # Transpose the text using the key order with the lowest chi-squared value.
    original_text = data
    text = transpose(data, lowest[0])
    # Print the text, frequencies of the text and frequencies of the closest language.
    print("Original Text: " + original_text)
    print("Text: " + text)
    frequencies = get_letter_frequencies(text)
    print("Frequencies: " + str(frequencies))
    print("Language: " + str(tables[lowest[2]]))
    # Split letters into pairs of 2
    text = [text[i:i + 2] for i in range(0, len(text), 2)]
    # Substitute the letters with the letters from the language with similar frequencies.
    for i in range(26):
        for j in range(len(text)):
            if text[j] == list(frequencies.keys())[i]:
                text[j] = list(tables[lowest[2]].keys())[i].lower()
    print("Options:")
    print("\"X Y\" - swaps X with Y")
    print("\"Exit\" - exits the frequency analysis")
    print("\"Reset\" - resets the text")
    while True:
        print("Text: " + ''.join(text))
        choice = input("")
        # Exit
        if choice == "Exit":
            break
        if choice == "Reset":
            text = transpose(data, lowest[0])
            text = [text[i:i + 2] for i in range(0, len(text), 2)]
            # Substitute the letters with the letters from the language with similar frequencies.
            for i in range(26):
                for j in range(len(text)):
                    if text[j] == list(frequencies.keys())[i]:
                        text[j] = list(tables[lowest[2]].keys())[i].lower()
            continue
        # Check if the choice is valid.
        if len(choice) != 3 or choice[1] != ' ' or choice[0] not in text or choice[2] not in text:
            print("Invalid choice.")
            continue
        # Swap the letters.
        for i in range(len(text)):
            if text[i] == choice[0]:
                text[i] = choice[2]
            elif text[i] == choice[2]:
                text[i] = choice[0]