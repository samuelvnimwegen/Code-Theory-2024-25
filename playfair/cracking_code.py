
from playfair.src.utils.utils import get_file_content, create_file_name, write_result
from playfair.src.cracking_algorithms import simulated_annealing
from playfair.src.scoring_algorithms import score_weighted_average, score_trigrams_count, score_three_letter_patterns
from playfair.src.playfair import Playfair


if __name__ == '__main__':
    text_to_crack = get_file_content('codes/02-OPGAVE-playfair.txt')
    key, score, language, elapsed_time = simulated_annealing(text_to_crack, score_three_letter_patterns)

    original_text = key.decrypt(text_to_crack)
    print(original_text)

    # Write result to a file
    filename = create_file_name("02-OPGAVE-playfair", "playfair/results/")
    write_result(filename, key.keyword, original_text)



