import math
from random import random
from datetime import datetime
import time

from playfair.src.playfair import Playfair, generate_random_Playfair_matrix, create_random_modified_matrix


def simulated_annealing(ciphertext: str, scoring_fn,
                        output_file: str,
                        transitions: int = 50000,
                        temperature: float = 0.5, cooling_rate: float = 0.003,
                        restart_patience=256, start_key: None|str=None) -> (Playfair, float, str):
    """
    Simulated annealing algorithm to try and crack

    :source: https://www.oranlooney.com/post/playfair/
    https://github.com/damiannolan/simulated-annealing-playfair-cipher-breaker/blob/master/README.md
            https://www.youtube.com/watch?v=5ElAUPABh6U

    :param ciphertext: the ciphertext to decrypt
    :param transitions: amounts to make in one loop
    :param temperature: the starting temperature     (values 0.5, 1 have been used in past)
    :param cooling_rate: rate to decrease temperature
    :param restart_patience: the time to restart from the best score known
    :param scoring_fn: the scoring function
    :param stop_score: stop algorithm after reaching better result than this score (better result = smaller than)
    :param start_key: possible starting key
    :param output_file: the output file to where the progress should be sent
    :return: the best key, with its score and used language
    """
    print_start(output_file)

    # Get the start time
    start_time = datetime.now().timestamp()

    if start_key is None:
        # Generate first random key and calculate its score
        current_key: Playfair = generate_random_Playfair_matrix()
    else:
        # Use given starting key (used in testing)
        current_key: Playfair = Playfair(start_key)

    current_language, current_score = scoring_fn(ciphertext, current_key)

    # Initialise the best variables
    best_key: Playfair = current_key
    best_score = current_score
    best_key_language = current_language
    time_since_best = 0

    # This is used in other algorithm
    other_temp = 10

    index = 0
    # the simulated annealing algorithm
    try:
        #while temperature > 0.001:
        for temp in range(other_temp, 0, -1):
            for trans in range(transitions):
                # Create new key by altering the current key
                alternated_key: Playfair = create_random_modified_matrix(current_key)
                # calculate the score
                language, score = scoring_fn(ciphertext, alternated_key)

                # If score is better, replace current key and go again
                # if current_score > best_score:
                #     best_score = current_score
                #     best_key = current_key
                #     best_key_language = current_language
                #     time_since_best = 0
                #
                #     continue

                # If score is worse -> accept with certain probability
                delta_score = score - current_score
                #delta_ratio = delta_score / temperature
                delta_ratio = delta_score / temp
                if abs(delta_ratio) > 100:
                    delta_ratio = math.copysign(1, delta_ratio)
                acceptance_rate = math.exp(delta_ratio)
                # generate random value between 0 and 1, if value smaller than probability, accept
                if random() < acceptance_rate:
                    current_score = score
                    current_key = alternated_key
                    current_language = language

                    # If better than best_score, update time to 0, otherwise increase by 1
                    if current_score > best_score:
                        best_score = current_score
                        best_key = current_key
                        best_key_language = current_language
                        time_since_best = 0

                        print_progress(output_file, index, start_time, best_key, ciphertext, best_score)

                    else:
                        time_since_best += 1
                        if time_since_best > restart_patience:
                            time_since_best = 0
                            current_score = best_score
                            current_key = best_key
                            current_language = best_key_language

                # at the end, decrease temperature with cooling rate
                temperature *= 1 - cooling_rate
                index += 1

    except KeyboardInterrupt:
        end_time = datetime.now().timestamp()
        elapsed_time = end_time - start_time

        myPrint("-------------------------------------------------------------------------------------", output_file)
        myPrint("Algorithm Stopped/interrupted", output_file)
        print_progress(output_file, index, start_time, best_key, ciphertext, best_score)
        return best_key, best_score, best_key_language, elapsed_time

    end_time = datetime.now().timestamp()
    elapsed_time = end_time - start_time

    myPrint("-------------------------------------------------------------------------------------", output_file)
    myPrint("Algorithm Finished", output_file)
    print_progress(output_file, index, start_time, best_key, ciphertext, best_score)
    return best_key, best_score, best_key_language, elapsed_time


def print_progress(filename: str, index: int, start_time: float, key: Playfair, decrypt_text: str, score: float):
    """
    Print the current progress
    """
    print_str = f"{index}\t\t"

    # Time needed
    current_time = datetime.now().timestamp()
    passed_time_seconds = current_time - start_time
    hours, remainder = divmod(passed_time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print_str += f"{hours}:{minutes}:{seconds}\t"

    # Key used
    key_word = key.matrix_obj.get_matrix_as_string()
    print_str += f"{key_word}\t"

    # Start from resulting plaintext
    plaintext = key.decrypt(decrypt_text)
    print_str += f"{plaintext[:40]}...\t"

    # Score
    percentage = 100 * score
    print_str += f"{percentage}%"

    myPrint(print_str, filename)


def print_start(filename: str):
    """
    Print the start line of file
    """
    myPrint("Index\t\t|Time Needed\t\t\t\t|Key\t\t\t\t\t\t|Plaintext\t\t\t\t\t\t\t\t|Score", filename)


def myPrint(text: str, filename: str):
    """
    Print to file and console
    """

    with open(filename, 'a') as file:
        file.write(text + '\n')

    file.close()
    print(text)
