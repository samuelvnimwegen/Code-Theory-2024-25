"""
This is the EnigmaSolver class.
"""
import itertools

from enigma.enigma_graph import EnigmaGraph
from enigma.enigma_matrix import EnigmaMatrix


class EnigmaSolver:
    """
    This class represents the enigma solver
    """

    def solve(self, variables: dict) -> str:
        """
        Cracks an enigma code
        :return: The solution
        """
        rotor0 = variables["rotor0"]
        rotor1 = variables["rotor1"]
        rotor2 = variables["rotor2"]
        rotor3 = variables["rotor3"]
        rotor4 = variables["rotor4"]
        reflector = variables["reflector"]
        crib = variables["crib"]
        encrypted_text = variables["encrypted_text"]

        enigma_graph = EnigmaGraph(crib, encrypted_text)
        enigma_matrix = EnigmaMatrix(enigma_graph)

        # Try all rotor configurations
        rotor_configurations = self.get_rotor_possibilities([rotor0, rotor1, rotor2, rotor3, rotor4])
        i = 0
        for rotor_configuration in rotor_configurations:
            print("Now trying rotor configuration:", i)
            rotor1, rotor2, rotor3 = rotor_configuration
            if enigma_matrix.try_rotor_configuration(rotor1, rotor2, rotor3, reflector):
                print(f"{rotor1} {rotor2} {rotor3}")
                return

        print("No solution found")
        return

    @staticmethod
    def get_rotor_possibilities(rotors: list[str]) -> list[list[str]]:
        """
        Get all possible rotor configurations
        """
        # Get all permutations of exact length 3
        permutations_length_3: list[list[str]] = list(itertools.permutations(rotors, 3))

        return permutations_length_3
