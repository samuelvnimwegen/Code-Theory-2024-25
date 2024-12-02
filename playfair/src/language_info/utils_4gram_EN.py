"""
This file was a one time use to create the dictionary of english 4-grams and there probability
Also used to create the dictionary of the Frequency table for Playfair
"""
from playfair.src.language_info.letter_frequency_table import ENGLISH

total_4grams = 4224127912

dir_path: str = "playfair/src/language_info/"
gram_file: str = f"{dir_path}4grams.txt"


def create_dict_4grams():
    text = "\n\n"

    # Create dict
    text += "fourgram_en = {"

    # Add items
    with open(gram_file, "r") as file:
        for i, line in enumerate(file):
            text_line = line.strip()
            values = text_line.split(" ")
            gram = values[0]
            probability = values[1]
            if int(probability) < 10000:
                break
            text += f"\"{gram}\":{probability},\n"

    text = text[:-2]
    # Close dict
    text += "\n}"

    with open(f"{dir_path}four_grams_most_common.py", 'a') as file:
        file.write(text)

    file.close()


def sort_4grams():

    with open(gram_file, "r") as f:
        lines = f.readlines()

    sorted_lines = sorted(lines)
    with open(f"{dir_path}sorted_4grams.txt", "w") as f:
        f.writelines(sorted_lines)


def binary_search_4grams(target: str) -> int:
    """
    Use binary search to find the count in the sorted txt file
    :param target: the 4-gram
    :return: int: count value
    """
    with open(f"{dir_path}sorted_4grams.txt", "r") as f:
        lines = f.readlines()

    # Start on beginning and on the end
    left, right = 0, len(lines) - 1
    while left <= right:
        # Get the middle ground
        mid = (left + right) // 2
        line = lines[mid]
        gram, count = line.strip().split(" ")
        # If the target is not the middle: shift to the left or right half
        if gram == target:
            return int(count)
        elif gram < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0  # 4-gram not found


def create_playfair_freq_table():
    """
    Change the English Frequency Table to use in Playfair
    Add J frequency to the I's
    Remove the X's and re-normalise the frequencies
    :return: write the new frequency table to new file
    """
    # New frequency table
    new_freq_table = ENGLISH

    # Change all J's to I's
    new_freq_table['I'] += new_freq_table['J']
    new_freq_table.pop('J')

    # Remove the X from freq table
    new_freq_table.pop('X')

    # Renormalise
    total = sum(new_freq_table.values())
    for item in new_freq_table.items():
        new_freq_table[item[0]] = item[1] / total

    # Write the Table to a file
    with open(f"{dir_path}letter_freq_table_playfair.py", "w") as f:
        f.write("ENGLISH_PLAYFAIR = ")
        f.write(repr(new_freq_table))


if __name__ == '__main__':
    # create_dict_4grams()
    create_dict_4grams()






