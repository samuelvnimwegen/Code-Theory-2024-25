"""
This file contains the EnigmaMatrix class
"""
import sys
from copy import deepcopy
from datetime import datetime
from enigma.enigma_graph import EnigmaGraph
from enigma.enigma_machine import EnigmaMachine


class EnigmaMatrix:
    """
    This class represents the matrix for the plugboard
    """

    def __init__(self, graph: EnigmaGraph, auto_setup: bool = True):
        """
        Initializes the matrix
        """
        self.edges: list[list[list[tuple[int, int]]]] = [[[] for _ in range(26)] for _ in range(26)]
        self.connected_rows: set[tuple[int, int]] = set()
        self.plug_matrix_solution: list[list[bool]] = []
        if auto_setup:
            self.add_default_edges()
            self.find_connected_rows(graph)
            self.l1: str = self.find_node_with_most_edges(graph)

    def add_default_edges(self) -> None:
        """
        Adds the default edges to the matrix (A, B) <-> (B, A)
        """
        for i in range(26):
            for j in range(26):
                if i != j:
                    self.edges[i][j].append((j, i))

    def find_connected_rows(self, enigma_graph: EnigmaGraph) -> None:
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

    def try_rotor_choice(self, rotor1: str, rotor2: str, rotor3: str, reflector: str,
                         insta_return: bool = False) -> list[dict[str, str]]:
        """
        Tries to apply the enigma configuration to the matrix

        :param rotor1: The first rotor (the slowest rotor).
        :param rotor2: The second rotor (the middle rotor).
        :param rotor3: The third rotor (the fastest rotor).
        :param reflector: The reflector.
        :param insta_return: Whether to return the first valid configuration
        :return: True if the configuration is valid, False otherwise
        """
        # Get a list of the connected rows
        connected_rows: list[tuple[int, int, int]] = list(self.connected_rows)

        # Make the enigma machines
        enigma_machines: list[EnigmaMachine] = self.make_enigma_machines(rotor1, rotor2, rotor3, reflector,
                                                                         connected_rows)

        # Iterate over all the possible configurations of the enigma machines (26^3)
        solutions = []
        conf_range = range(pow(26, 3))
        last_time = datetime.now()
        for it in conf_range:
            if it % 25 == 0 and it != 0:
                current_time = datetime.now()
                iteration_time: int = (current_time - last_time).total_seconds()
                intervals_left: int = (pow(26, 3) - it) / 25
                configuration = f"Now trying configuration: {it} / 17576 for current rotor choice"
                estimate = (f"Estimated time left for current rotor choice: "
                            f"{round(intervals_left * iteration_time, 1)} seconds")

                print(f"\r{configuration} | {estimate}", end="")

                last_time = current_time

            # Make of copy of the default edges
            edges: list[list[list[tuple[int, int]]]] = deepcopy(self.edges)

            # Now we add all the enigma machine configuration edges to the matrix
            for i in range(len(connected_rows)):
                # Get the row connection
                row_connection: tuple[int, int, int] = connected_rows[i]
                row1_index, row2_index, shift_value = row_connection

                # Get the enigma machine for the row connection
                enigma_machine: EnigmaMachine = enigma_machines[i]

                # Connect the rows
                edges = self.connect_rows(row1_index, row2_index, enigma_machine, edges)

            # Check if the matrix is valid
            if self.is_valid(edges)[0]:
                conf: dict = self.return_configuration(it, self.is_valid(edges)[1], rotor1, rotor2, rotor3)
                solutions.append(conf)
                print("*" * 50)
                print("Found a valid configuration")
                print("*" * 50)
                if insta_return:
                    return solutions

            # Update the rotor positions
            for enigma_machine in enigma_machines:
                enigma_machine.update_rotor_positions()
        return solutions

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

    @staticmethod
    def make_enigma_machines(
        rotor1: str,
        rotor2: str,
        rotor3: str,
        reflector: str,
        connected_rows: list
    ) -> list[EnigmaMachine]:
        """
        Makes an enigma machine with the given rotor and reflector configuration
        """
        enigma_machines = []
        empty_conf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for connected_row in connected_rows:
            shift_value = connected_row[2]
            enigma_machine = EnigmaMachine(
                rotors=[rotor1, rotor2, rotor3],
                reflector=reflector,
                plugboard=empty_conf,
                rotor_positions=[0, 0, shift_value]
            )
            enigma_machines.append(enigma_machine)
        return enigma_machines

    def connect_rows(
        self,
        row1_index: int,
        row2_index: int,
        enigma_machine: EnigmaMachine,
        edges: list[list[list[tuple[int, int]]]]
    ) -> list[list[list[tuple[int, int]]]]:
        """
        Connects two rows in the matrix
        """
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
        return edges

    def is_valid(self, edges: list[list[list[tuple[int, int]]]]) -> tuple[bool, list[list[bool]]]:
        """
        Checks if the matrix is valid
        """
        conf_matrix = []
        for row in range(26):
            conf_matrix.append([False] * 26)

        # Start the BFS from the first node
        row_items: list[int] = [i for i in range(26)]
        l1_index = self.capital_to_int(self.l1)
        while len(row_items) > 0:
            l2_index: int = row_items.pop(0)
            queue = [(l1_index, l2_index)]
            loop_conf_matrix = deepcopy(conf_matrix)

            # Add a counter, from the moment we hit 25, we can start checking for solutions
            addition_counter = 0
            while len(queue) > 0:
                row, col = queue.pop(0)

                # If the edge is already in the matrix, continue
                if loop_conf_matrix[row][col]:
                    continue

                # Mark the edge as visited
                loop_conf_matrix[row][col] = True
                addition_counter += 1

                # If the edge is not in the matrix, add it to the queue
                for edge in edges[row][col]:
                    queue.append(edge)

            # If all the rows and columns have exactly one positive, return True
            all_rows_one_item: bool = all([row.count(True) <= 1 for row in loop_conf_matrix])
            all_cols_one_item: bool = all([col.count(True) <= 1 for col in zip(*loop_conf_matrix)])

            # There should be at least 10 edges in the matrix
            if all_rows_one_item and all_cols_one_item and addition_counter > 10:
                return True, loop_conf_matrix
            else:
                # Pop all the true items in the row of l1
                for i in range(26):
                    if loop_conf_matrix[l1_index][i] and i in row_items:
                        row_items.pop(row_items.index(i))

        return False, None

    @staticmethod
    def return_configuration(
        iterations: int,
        edges_matrix: list[list[bool]],
        rotor1: str,
        rotor2: str,
        rotor3: str,
    ) -> dict[str, str]:
        """
        Returns the configuration of the enigma machine
        """
        # Since we start counting from 1 while making the graph, we need to add 1 to the iterations
        iterations += 1

        # Get the rotor configuration
        slow_rotor = chr(iterations // (26 ** 2) + 65)
        rest = iterations % (26 ** 2)
        middle_rotor = chr(rest // 26 + 65)
        rest = rest % 26
        fast_rotor = chr(rest % 26 + 65)
        rotor_config: str = slow_rotor + middle_rotor + fast_rotor

        # Get the plugboard configuration
        conf_dict = {}
        for i in range(26):
            for j in range(26):
                if edges_matrix[i][j]:
                    conf_dict[chr(i + 65)] = chr(j + 65)

        # Now make the plugboard string
        for i in range(26):
            if chr(i + 65) not in conf_dict:
                conf_dict[chr(i + 65)] = chr(i + 65)

        plugboard_str = ""
        for i in range(26):
            if chr(i + 65) in conf_dict:
                plugboard_str += conf_dict[chr(i + 65)]
            else:
                plugboard_str += chr(i + 65)

        return {
            "rotor_config": rotor_config,
            "plugboard": plugboard_str,
            "rotor_slow": rotor1,
            "rotor_middle": rotor2,
            "rotor_fast": rotor3,
        }
