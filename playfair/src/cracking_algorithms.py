import math
from random import random
from datetime import datetime
import time

from playfair.src.playfair import Playfair, generate_random_Playfair_matrix, create_random_modified_matrix


def simulated_annealing(ciphertext: str, scoring_fn, stop_score,
                        attempts: int = 1024,
                        temperature: float = 0.5, cooling_rate: float = 0.003,
                        restart_patience=256, start_key: None|str=None) -> (Playfair, float, str):
    """
    Simulated annealing algorithm to try and crack

    :source: https://www.oranlooney.com/post/playfair/
            https://www.youtube.com/watch?v=5ElAUPABh6U

    :param ciphertext: the ciphertext to decrypt
    :param attempts: maximum amounts to make
    :param temperature: the starting temperature     (values 0.5, 1 have been used in past)
    :param cooling_rate: rate to decrease temperature
    :param restart_patience: the time to restart from the best score known
    :param scoring_fn: the scoring function
    :param stop_score: stop algorithm after reaching better result than this score (better result = smaller than)
    :param start_key: possible starting key
    :return: the best key, with its score and used language
    """
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

    index = 0
    # the simulated annealing algorithm
    try:
        #for index in range(attempts):
        # Changed the algorithm: instead of trying max attempts, go find answer: answer might be good if score is lower than 0.35
        while best_score < stop_score:
        #while best_score < 0.99:  # Value to make it run indefinitely
            if index % 10000 == 0:
                # Every 10 000 attempts, check if we have passed the hour mark
                current_time = datetime.now().timestamp()
                passed_time_seconds = current_time - start_time
                hours, remainder = divmod(passed_time_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"Current elapsed time at index {index}: {hours}:{minutes}:{seconds} - current score: {best_score*100} %")
                # if passed_time_seconds > 3600:
                #     print("The algorithm has passed the one hour mark")
                #     raise KeyboardInterrupt

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
            delta_ratio = delta_score / temperature
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
        print(index, elapsed_time, best_key.keyword, f"{best_score*100}%", "Algorithm stopped/interrupted")

    end_time = datetime.now().timestamp()
    elapsed_time = end_time - start_time

    print(index, elapsed_time, best_key.keyword, f"{best_score * 100}%", "Algorithm finished")
    return best_key, best_score, best_key_language, elapsed_time

