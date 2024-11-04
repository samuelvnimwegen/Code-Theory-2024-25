"""
This file is made to decypher an enigma cipher
"""

from enigma.enigma_solver import EnigmaSolver


def solve_enigma() -> None:
    """
    Solve the enigma cipher
    """

    rotor0 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotor3 = "THEQUICKBROWNFXJMPSVLAZYDG"
    rotor4 = "XANTIPESOKRWUDVBCFGHJLMQYZ"

    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    crib = "DEOPGAVEVOORENIGMA"
    encrypted_text = ("TUMGMTTJDSEJXVEIJSWULHAFYJEYYMDFXCOVHHUSBMLBGTXUJOTUUTHPTQQYEWVIEHWIKDXGXWPQGWHJNKGJCYLUBYUEWYO"
                      "KZPGDCRIRNIHNPXCQYRGNKOCYRRJSOLQQJOWXHMGOGWGIIWUEGOQTROTAVWNKWCDVRSMURYIDKJFZXCANLEIBRKGWHHDLHH"
                      "DBFWFVEGSSJVVDTVQBPACLTPZGXLMJRKZWHNZCVVDDNWSTGLTQGGBRTRTSXSGRKHCQUNIAQNHJKPIETGQMRSLJHFBUQUC"
                      "CNDKQZLLOCBKOJDGSRXTFVJCOAWXIZSZVVLLFWUJCWKIEBYSTEQMGDMTSDTHDYHHUYTKRYPNOEJTUSNXZTYLTDBOEEXZW"
                      "PEITOBZNCPJKTZLDFLVXHLZYSWQKIOVPTRUJFGGLCCCYKKVHKMTRKXARQGC")
    variables = {
        "rotor0": rotor0,
        "rotor1": rotor1,
        "rotor2": rotor2,
        "rotor3": rotor3,
        "rotor4": rotor4,
        "reflector": reflector,
        "crib": crib,
        "encrypted_text": encrypted_text,
    }

    x = EnigmaSolver()
    x.solve(variables)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve_enigma()
    print(f"Runtime: {round(time.time() - start_time, 3)} seconds")
