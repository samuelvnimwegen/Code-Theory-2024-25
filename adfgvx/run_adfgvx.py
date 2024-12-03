import os.path
import itertools

from adfgvx.hill_climb import HillClimbADFGVX
from util.filestream import load as load_file
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
    text, score = hill_climb.hill_climb()

    # Write the result and score to a file
    with open("adfgvx/results/result.txt", "w") as f:
        f.write(f"Score: {score}\n")
        f.write(text)
        f.close()


    """
    # Calculate transposition
    try:
        new_data, chi, key = get_original_transposition(data, key_length)
    except ValueError as e:
        print(e)
        return ""
    # Frequency analysis
    result = frequency_analysis(data, new_data, chi, key)
    return result
    """


if __name__ == '__main__':
    path = "codes/03-OPGAVE-adfgvx.txt"
    plain = solve_adfgvx(path, 10)
    # resulting key = (3, 1, 6, 8, 4, 2, 5, 0, 7)
    pass
