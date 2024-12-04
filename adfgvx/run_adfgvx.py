import os.path
import itertools
import json
from adfgvx.hill_climb import HillClimbADFGVX
from util.filestream import load as load_file, count_files_in_directory
from adfgvx.morse import decode as decode_morse
from adfgvx.frequency_analysis import frequency_analysis
from adfgvx.column_transposition import get_original_transposition, reverse_transpose


def solve_adfgvx(path: str, key_length: int) -> str:
    # Load the morse code from the file.
    morse = load_file(path)
    # Decode the morse code.
    data = decode_morse(morse)

    # Get all transpositions for the data.
    after_transpose = reverse_transpose(data, (3, 1, 6, 8, 4, 2, 5, 0, 7))
    hill_climb = HillClimbADFGVX(after_transpose)

    # Get the result from the hill climb
    text, score, key = hill_climb.hill_climb()

    # Save the result to a file
    result = {
        "text": text,
        "score": score,
        "key": key
    }

    # Count the number of files in the directory
    result_nr = count_files_in_directory("adfgvx/results")

    # Write the result to a JSON file
    with open(f"adfgvx/results/result{result_nr}.json", 'w') as file:
        json.dump(result, file, indent=4)

    print(f"Result saved to adfgvx/results/result{result_nr}.json")


if __name__ == '__main__':
    path = "codes/03-OPGAVE-adfgvx.txt"
    plain = solve_adfgvx(path, 10)
    # resulting key = (3, 1, 6, 8, 4, 2, 5, 0, 7)
    pass
