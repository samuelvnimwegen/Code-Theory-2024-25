import copy
import itertools
from util.filestream import load as load_file
from adfgvx.decode_morse import decode as decode_morse
from util.letter_frequency_tables import tables as tables
from adfgvx.column_transposition import transpose as transpose
from util.letter_frequency_tables import tables_names as languages
from adfgvx.column_transposition import get_letter_frequencies as get_letter_frequencies
from adfgvx.column_transposition import get_transposition_chi_values as get_transposition_chi_values

if __name__ == '__main__':
    # Load the morse code from the file.
    morse = load_file('codes/03-OPGAVE-adfgvx.txt')
    # Decode the morse code.
    data = decode_morse(morse)
    # Get all permutations for a key of max length 10. (And remove ordered permutations except first)
    print("Generating permutations...")
    perms = [perm for i in range(1, 11) for perm in itertools.permutations(range(i)) if list(perm) != sorted(perm)]
    perms.insert(0, (0,))
    print("Generated " + str(len(perms)) + " permutations.")
    # Get all transpositions for the data.
    print("Transposing data...")
    transpositions = get_transposition_chi_values(data, perms)
    # transpositions = {(0,): [3,4,5,6,7,8],
    #                   (1,0): [1,2,3,4,5,6],
    #                   (1,0,2): [2,3,4,5,6,7],
    #                   (2,1,0): [4,5,6,7,8,9]}
    # perms = [(0,), (1,0), (1,0,2), (2,1,0)]
    lowest_done = []
    while True:
        if len(lowest_done) >= len(perms*len(languages)):
            break
        # Get the key order with the lowest chi-squared value.
        lowest = ((0,), float('inf'), 0)
        for key in perms:
            for chi in transpositions[key]:
                # If the chi-squared value is lower than the current lowest chi-squared value.
                if chi < lowest[1]:
                    # If the key order is already done, skip.
                    if (key, chi, transpositions[key].index(chi)) in lowest_done:
                        continue
                    # Set the new lowest chi-squared value.
                    lowest = (key, chi, transpositions[key].index(chi))
        # Add to lowest_done
        lowest_done.append(lowest)
        # Print the key order with the lowest chi-squared value.
        print("Key order with lowest chi-squared value: " + str(lowest[0]) + " with value: " + str(lowest[1]) + " for language: " + languages[lowest[2]])
        while True:
            # Print options
            print("Options:")
            print("1. Continue to next lowest chi-squared value")
            print("2. Try frequency analysis")
            print("3. Exit")
            choice = input("")
            # Continue to next lowest chi-squared value
            if choice == "1":
                break
            elif choice == "2":
                # Transpose the text using the key order with the lowest chi-squared value.
                original_text = transpose(data, lowest[0])
                text = copy.deepcopy(original_text)
                # Print options
                print("Options:")
                print("XX/x. A valid pair of letters to swap with the latter letter")
                print("x/XX. A valid pair of letters to swap with the former letter (revert)")
                print("Exit")
                while True:
                    # Print the text, frequencies of the text and frequencies of the closest language.
                    print("Original Text: " + original_text)
                    print("Text: " + text)
                    print("Frequencies: " + str(get_letter_frequencies(text)))
                    print("Language: " + str(tables[lowest[2]]))
                    choice = input("")
                    # Exit
                    if choice == "Exit":
                        break
                    # Check if the choice is a valid pair of letters to swap with the latter letter.
                    elif len(choice) == 4 and (choice[1] == '/' or choice[2] == '/'):
                        if choice[1] == '/':
                            # Swap the latter letter with the former letter.
                            text = text.replace(choice[0], choice[2]+choice[3])
                        elif choice[2] == '/':
                            # Swap the former letter with the latter letter.
                            text = text.replace(choice[0]+choice[1], choice[3])
                        else:
                            print("Invalid choice.")
                    else:
                        print("Invalid choice.")
            # Exit program
            elif choice == "3":
                exit()
            else:
                print("Invalid choice.")