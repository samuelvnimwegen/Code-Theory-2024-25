"""
This file is made to decypher a vigenere cipher
"""
import json
from vigenere.transposition import solve_column_transposition
from vigenere.vigenere import solve_vigenere


def solve_vigenere_plus_column() -> None:
    """
    Solve the vigenere plus column transposition cipher
    """
    with open("codes/01-OPGAVE-viginereplus.txt", "r", encoding="utf-8") as file:
        code = file.read()

    # Solve the column transposition
    column_transposition_solutions: list = solve_column_transposition(cipher=code, max_key_length=7)

    # Solve the vigenere cipher
    solutions = []
    for column_ciphertext in column_transposition_solutions:
        solution = solve_vigenere(cipher=column_ciphertext, max_key_len=10)
        solutions.append(solution)
        print(solution)

    with open("solutions/01-OPGAVE-vigenereplus.txt", "w", encoding="utf-8") as file:
        file.write(json.dumps(solutions, indent=4))


if __name__ == "__main__":
    solve_vigenere_plus_column()
