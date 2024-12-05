import json
from pathlib import Path
from adfgvx.hill_climb import HillClimbADFGVX
from util.filestream import load as load_file, count_files_in_directory
from adfgvx.morse import decode as decode_morse
from adfgvx.column_transposition import get_original_transposition, reverse_transpose


def solve_adfgvx(path: str, max_key_length: int, dir: str = "adfgvx/results"):
    """
    Solve the ADFGVX cipher using a hill climb algorithm.

    :param path: The path to the file containing the ADFGVX cipher.
    :param max_key_length: The length of the key.
    :param dir: The directory to save the results to.
    """
    # Load the morse code from the file.
    morse = load_file(path)
    # Decode the morse code.
    data = decode_morse(morse)

    # Get the key
    key = get_original_transposition(data, max_key_length)
    # Result: key = (3, 1, 6, 8, 4, 2, 5, 0, 7)

    # Get all transpositions for the data.
    after_transpose = reverse_transpose(data, key)
    hill_climb = HillClimbADFGVX(after_transpose)

    # Get the result from the hill climb
    text, score, key = hill_climb.hill_climb()

    # Save the result to a file
    result = {
        "text": text,
        "score": score,
        "key": key
    }

    # Create directory if it doesn't exist
    Path(dir).mkdir(parents=True, exist_ok=True)
    # Count the number of files in the directory
    result_nr = count_files_in_directory(dir)

    # Write the result to a JSON file
    with open(f"{dir}/result{result_nr}.json", 'w') as file:
        json.dump(result, file, indent=4)

    print(f"Result saved to adfgvx/results/result{result_nr}.json")


if __name__ == '__main__':
    # https://fr.wikisource.org/wiki/Ars%C3%A8ne_Lupin_gentleman-cambrioleur/L%E2%80%99arrestation_d%E2%80%99Ars%C3%A8ne_Lupin
    # Polybius square key is equivalent to "ZBXQTCM01DV2GYRU345O6F789EWIKLAHSPNJ"
    # All numbers + w and k can be switched since these are not used in the text
    code_path = "codes/03-OPGAVE-adfgvx.txt"
    result_path = "adfgvx/results"
    solve_adfgvx(code_path, 10)
