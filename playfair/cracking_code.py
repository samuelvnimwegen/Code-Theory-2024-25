
from playfair.src.utils.utils import get_file_content, create_file_name, write_result
from playfair.src.cracking_algorithms import simulated_annealing
from playfair.src.scoring_algorithms import score_weighted_average, score_trigrams_count, score_three_letter_patterns, score_frequencies_english
from playfair.src.playfair import Playfair


def cracking(text_to_crack: str, test=False, start_key: str | None = None) -> (str, str):
    """
    Try to crack the text using Playfair
    :return: keyword, plaintext
    """

    key, score, language, elapsed_time = simulated_annealing(text_to_crack, score_frequencies_english, 0.95, start_key=start_key)

    original_text = key.decrypt(text_to_crack)
    print(original_text)

    # Write result to a file
    name_file = "02-OPGAVE-playfair"
    dir_path = "playfair/results/"
    if test:
        name_file = "02-TEST-playfair"
        dir_path = "playfair/results_test/"
    filename = create_file_name(name_file, dir_path)
    write_result(filename, key.keyword, original_text, elapsed_time, score)

    return key.keyword, original_text


if __name__ == '__main__':
    text_to_crack = get_file_content('codes/02-OPGAVE-playfair.txt')
    cracking(text_to_crack)




