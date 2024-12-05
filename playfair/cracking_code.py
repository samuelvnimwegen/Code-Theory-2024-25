
from playfair.src.utils.utils import get_file_content, create_file_names, write_result
from playfair.src.cracking_algorithms import simulated_annealing
from playfair.src.scoring_algorithms import score_weighted_average, score_trigrams_count, score_three_letter_patterns, score_frequencies_english, score_quad_gram_count
from playfair.src.playfair import Playfair


def cracking(text_to_crack: str, heuristic, dir_path: str = "playfair/results/", test=False, start_key: str | None = None) -> (str, str):
    """
    Try to crack the text using Playfair
    :return: keyword, plaintext
    """

    # Create filename
    name_file = "02-OPGAVE-playfair"
    if test:
        name_file = "02-TEST-playfair"
        dir_path = "playfair/results_test/"
    filename, progress_file, index_file = create_file_names(name_file, dir_path)

    # Try to crack the ciphertext
    key, score, language, elapsed_time = simulated_annealing(text_to_crack, heuristic, start_key=start_key,
                                                             output_file=progress_file)

    original_text = key.decrypt(text_to_crack)
    print(original_text)

    # Write result to a file
    write_result(filename, key.keyword, original_text, elapsed_time, score)

    return key.keyword, original_text


if __name__ == '__main__':
    text_to_crack = get_file_content('codes/02-OPGAVE-playfair.txt')
    output_file = "playfair/results/big_loop/"

    cracking(text_to_crack, score_quad_gram_count, output_file)




