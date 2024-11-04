from datetime import datetime
import sys
sys.path.append('..')
from playfair.playfair import *
from playfair.scoring_algorithms import score_weighted_average


def simulated_annealing(ciphertext: str, attempts: int = 1024,
                              temperature: float = 0.5, cooling_rate: float = 0.003,
                              restart_patience=256) -> tuple[str, float, str]:
    """
    Simulated annealing algorithm to try and crack

    :source: https://www.oranlooney.com/post/playfair/
            https://www.youtube.com/watch?v=5ElAUPABh6U

    :param ciphertext: the ciphertext to decrypt
    :param attempts: maximum amounts to make
    :param temperature: the starting temperature
    :param cooling_rate: rate to decrease temperature
    :param restart_patience: the time to restart from the best score known
    :return: the best key, with its score and used language
    """
    # Generate first random key and calculate its score
    current_key: Playfair = generate_random_Playfair_matrix()
    current_score, current_language = score_weighted_average(ciphertext, current_key)

    # Initialise the best variables
    best_key: Playfair = current_key
    best_score = current_score
    time_since_best = 0
    language = current_language

    # the simulated annealing algorithm
    try:
        for index in range(attempts):
            # Create new key by altering the current key

            # calculate the score

            # If score is better, replace current key and go again
            # If score is worse -> accept with certain probability
            # probability = exp(-delta/temperature)
            # generate random value between 0 and 1, if value smaller than probability, accept
            #
            # If better then best_score, update time to 0, otherwise increase by 1
            # at the end, decrease temperature with cooling rate
            return

    except KeyboardInterrupt:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(index, time, best_key, best_score, "Algorithm stopped due to keyboard interrupt")

    return best_key, best_score