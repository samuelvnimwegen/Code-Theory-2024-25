"""
This file contains the EnigmaMatrix class
"""
from copy import deepcopy

from enigma.enigma_graph import EnigmaGraph
from enigma.enigma_machine import EnigmaMachine


class EnigmaMatrix:
    """
    This class represents the matrix for the plugboard
    """

    def __init__(self, graph: EnigmaGraph):
        """
        Initializes the matrix
        """
        self.edges: list[list[list[tuple[int, int]]]] = [[[] for _ in range(26)] for _ in range(26)]
        self.connected_rows: set[tuple[int, int]] = set()
        self._add_default_edges()
        self._find_connected_rows(graph)
        self.l1: str = self.find_node_with_most_edges(graph)

    def _add_default_edges(self) -> None:
        """
        Adds the default edges to the matrix (A, B) <-> (B, A)
        """
        for i in range(26):
            for j in range(26):
                if i != j:
                    self.edges[i][j].append((j, i))

    def _find_connected_rows(self, enigma_graph: EnigmaGraph) -> None:
        """
        Finds the connected rows (L1, L3) <-> (L2, e_value(L3)) for every edge (L1, L2) with value e_value
        in the enigma graph.

        :param enigma_graph: The enigma graph
        """
        for letter in enigma_graph.edges:
            for enigma_edge in enigma_graph.edges[letter]:
                # Get the row indexes of the rows that the edge connects
                row1_index: int = self.capital_to_int(enigma_edge.node1)
                row2_index: int = self.capital_to_int(enigma_edge.node2)

                # Get the shift value of the edge
                shift_value = enigma_edge.value

                # Add the edge to the connected_rows list
                self.connected_rows.add((row1_index, row2_index, shift_value))

    @staticmethod
    def find_node_with_most_edges(enigma_graph: EnigmaGraph) -> str:
        """
        Finds the node with the most edges in the matrix
        :return:
        """
        max_values = 0
        max_node = None
        for key, value in enigma_graph.edges.items():
            if len(value) > max_values:
                max_values = len(value)
                max_node = key
        return max_node

    def try_rotor_configuration(self, rotor1: str, rotor2: str, rotor3: str, reflector: str) -> bool:
        """
        Tries to apply the enigma configuration to the matrix

        :param rotor1: The first rotor (the slowest rotor).
        :param rotor2: The second rotor (the middle rotor).
        :param rotor3: The third rotor (the fastest rotor).
        :param reflector: The reflector.
        :return: True if the configuration is valid, False otherwise
        """
        # Get a list of the connected rows
        connected_rows: list[tuple[int, int, int]] = list(self.connected_rows)

        # For each connected row, make an enigma machine with a corresponding rotor configuration
        enigma_machines: list[EnigmaMachine] = []

        # Create the enigma machines
        empty_conf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # This is an empty plugboard configuration
        for connected_row in connected_rows:
            # The shift value is the start position of the third rotor
            shift_value = connected_row[2]
            enigma_machine = EnigmaMachine(
                rotors=[rotor1, rotor2, rotor3],
                reflector=reflector,
                plugboard=empty_conf,
                rotor_positions=[0, 0, shift_value]
            )
            enigma_machines.append(enigma_machine)

        # Iterate over all the possible configurations of the enigma machines (26^3)
        possible_configurations = range(pow(26, 3))
        for x in possible_configurations:
            if x % 1000 == 0:
                print("Now trying configuration:", x)
            # Make of copy of the default edges
            edges: list[list[list[tuple[int, int]]]] = deepcopy(self.edges)

            # Now we add all the enigma machine configuration edges to the matrix
            for row_connection_index in range(len(connected_rows)):

                # Get the row connection
                row_connection: tuple[int, int, int] = connected_rows[row_connection_index]
                row1_index, row2_index, shift_value = row_connection

                # Get the enigma machine for the row connection
                enigma_machine: EnigmaMachine = enigma_machines[row_connection_index]

                # Iterate over all the columns for each row connection
                for col_index in range(26):
                    # Get the letter at index i in the alphabet
                    letter = self.int_to_capital(col_index)

                    # Encrypt the letter with the enigma machine
                    encrypted_letter = enigma_machine.encrypt_letter(letter)

                    # Get the index of the encrypted letter
                    encrypted_index = self.capital_to_int(encrypted_letter)

                    # Add the edge to the matrix
                    edges[row1_index][col_index].append((row2_index, encrypted_index))
                    edges[row2_index][encrypted_index].append((row1_index, col_index))

            # Check if the matrix is valid
            if self.is_valid(edges):
                print("iteration:", x)
                return True
        return False

    @staticmethod
    def capital_to_int(letter: str) -> int:
        """
        Converts a capital letter to an integer
        """
        return ord(letter) - 65

    @staticmethod
    def int_to_capital(number: int) -> str:
        """
        Converts an integer to a capital letter
        """
        return chr(number + 65)

    def is_valid(self, edges: list[list[list[tuple[int, int]]]]) -> bool:
        """
        Checks if the matrix is valid
        """
        conf_matrix = []
        for l2 in range(26):
            conf_matrix.append([False] * 26)

        # Start the BFS from the first node
        for l2 in range(26):
            queue = [(self.capital_to_int(self.l1), l2)]
            while len(queue) > 0:
                row, col = queue.pop(0)

                # If there are multiple positives in the row, return False
                if conf_matrix[row].count(True) > 1:
                    return False

                # If all the rows and columns have exactly one positive, return True
                all_rows_one_item: bool = all([row.count(True) == 1 for row in conf_matrix])
                all_cols_one_item: bool = all([col.count(True) == 1 for col in zip(*conf_matrix)])
                if all_rows_one_item and all_cols_one_item:
                    return True

                # If the edge is already in the matrix, continue
                if conf_matrix[row][col]:
                    continue

                # Mark the edge as visited
                conf_matrix[row][col] = True
                for edge in edges[row][col]:
                    queue.append(edge)
        return False
