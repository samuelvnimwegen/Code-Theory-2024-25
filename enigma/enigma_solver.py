"""
This is the EnigmaSolver class.
"""
import itertools
import json

from enigma.enigma_graph import EnigmaGraph
from enigma.enigma_machine import EnigmaMachine
from enigma.enigma_matrix import EnigmaMatrix

from util.progress_bar import print_progress_bar


class EnigmaSolver:
    """
    This class represents the enigma solver
    """

    def __init__(self, variables: dict):
        self.rotor0 = variables["rotor0"]
        self.rotor1 = variables["rotor1"]
        self.rotor2 = variables["rotor2"]
        self.rotor3 = variables["rotor3"]
        self.rotor4 = variables["rotor4"]
        self.reflector = variables["reflector"]
        self.crib = variables["crib"]
        self.encrypted_text = variables["encrypted_text"]
        self.results = []

    def save_correct_configurations(self) -> str:
        """
        Cracks an enigma code
        :return: The solution
        """
        enigma_graph = EnigmaGraph(self.crib, self.encrypted_text)
        enigma_matrix = EnigmaMatrix(enigma_graph)

        # Try all rotor configurations
        rotor_configurations = self.get_rotor_possibilities([self.rotor0, self.rotor1, self.rotor2, self.rotor3,
                                                             self.rotor4])
        i = 0
        total_results = []
        for rotor_configuration in rotor_configurations:
            print("Now trying rotor choice:", i + 1, "out of", 60)
            print_progress_bar(i, 60)
            rotor1, rotor2, rotor3 = rotor_configuration

            results: list = enigma_matrix.try_rotor_choice(rotor1, rotor2, rotor3, self.reflector)
            if len(results) > 0:
                print(f"{rotor1} {rotor2} {rotor3}")
                total_results += results
            i += 1

        # Save the results
        self.results = total_results
        return

    @staticmethod
    def get_rotor_possibilities(rotors: list[str]) -> list[list[str]]:
        """
        Get all possible rotor configurations
        """
        # Get all permutations of exact length 3
        permutations_length_3: list[list[str]] = list(itertools.permutations(rotors, 3))

        return permutations_length_3

    def load_and_decrypt_solutions(self) -> list[dict]:
        """
        Decrypts the solutions
        """
        # Load the results
        results = self.results

        sols = []
        for result in results:
            rotor1 = result["rotor_slow"]
            rotor2 = result["rotor_middle"]
            rotor3 = result["rotor_fast"]
            reflector = self.reflector
            plugboard = result["plugboard"]
            rotor_positions: str = result["rotor_config"]
            rotor_positions = [ord(x) - 65 for x in rotor_positions]

            enigma_machine = EnigmaMachine(rotors=[rotor1, rotor2, rotor3], reflector=reflector, plugboard=plugboard,
                                           rotor_positions=rotor_positions)
            decrypted_text = enigma_machine.decrypt_text(self.encrypted_text)
            print(decrypted_text)
            result["decrypted_text"] = decrypted_text
            sols.append(result)

        with open("solutions/solutions_enigma_with_decryption.txt", "w") as file:
            json.dump(sols, file, indent=4)
        print("The solutions have been saved in solutions/solutions_enigma_with_decryption.txt")
        return sols
