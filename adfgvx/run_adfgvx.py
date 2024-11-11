import copy
import itertools

from util.filestream import load as load_file
from adfgvx.decode_morse import decode as decode_morse
from adfgvx.frequency_analysis import loop_over_lowest_chi_squared
from adfgvx.column_transposition import get_transposition_chi_values


if __name__ == '__main__':
    # Load the morse code from the file.
    morse = load_file('codes/03-OPGAVE-adfgvx.txt')
    # Decode the morse code.
    data = decode_morse(morse)
    # Get all permutations for a key of max length 10. (And remove ordered permutations except first)
    print("Generating permutations...")
    perms = [perm for i in range(1, 11) for perm in itertools.permutations(range(i)) if list(perm) != sorted(perm)]
    # perms = [(2, 0, 1)]
    perms.insert(0, (0,))
    print("Generated " + str(len(perms)) + " permutations.")
    # Get all transpositions for the data.
    print("Transposing data...")
    transpositions = get_transposition_chi_values(data, perms)
    # transpositions = {(0,): [500, 500, 500, 500, 500, 500], (2, 0, 1): [0, 2, 23, 4, 5, 6]}
    loop_over_lowest_chi_squared(data, perms, transpositions)