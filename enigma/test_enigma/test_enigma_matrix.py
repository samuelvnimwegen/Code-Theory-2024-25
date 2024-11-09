"""
This file contains the tests for enigma_matrix.py
"""
from enigma.enigma_machine import EnigmaMachine
from enigma.enigma_matrix import EnigmaMatrix, EnigmaGraph


def test_enigma_add_default_edges():
    """
    This function tests the setup of the enigma matrix with the default edges
    """
    enigma_matrix = EnigmaMatrix(EnigmaGraph("HELLO", "HELLO"), auto_setup=False)

    assert enigma_matrix.edges == [[[] for _ in range(26)] for _ in range(26)]
    assert enigma_matrix.connected_rows == set()

    enigma_matrix.add_default_edges()

    assert len(enigma_matrix.edges) == 26
    for i in range(26):
        assert len(enigma_matrix.edges[i]) == 26

    for i in range(26):
        for j in range(26):
            if i != j:
                assert enigma_matrix.edges[i][j] == [(j, i)]
            else:
                assert enigma_matrix.edges[i][j] == []


def test_enigma_find_connected_rows():
    """
    This function tests the find_connected_rows method
    """
    graph = EnigmaGraph("KEINEZUSAETZEZUMVORBERIQT", "DAEDAQOZSIQMMKBILGMPWHAIV")
    enigma_matrix = EnigmaMatrix(graph, auto_setup=False)
    enigma_matrix.find_connected_rows(graph)

    # Check if the amount of connected rows is equal to the amount of graph edges
    amount_of_connected_rows = len(enigma_matrix.connected_rows)
    amount_of_graph_edges = sum([len(graph.edges[letter]) for letter in graph.edges]) // 2
    assert amount_of_connected_rows == amount_of_graph_edges

    # Check if the connected rows are correct
    def generate_tuple(letter1, letter2, value):
        smaller_letter = min(letter1, letter2)
        larger_letter = max(letter1, letter2)
        return enigma_matrix.capital_to_int(smaller_letter), enigma_matrix.capital_to_int(larger_letter), value

    # Check a few connected rows
    assert generate_tuple("L", "V", 17) in enigma_matrix.connected_rows
    assert generate_tuple("V", "T", 25) in enigma_matrix.connected_rows
    assert generate_tuple("I", "A", 23) in enigma_matrix.connected_rows


def find_node_with_most_edges():
    """
    This function tests the find_node_with_most_edges method
    """
    graph = EnigmaGraph("KEINEZUSAETZEZUMVORBERIQT", "DAEDAQOZSIQMMKBILGMPWHAIV")
    enigma_matrix = EnigmaMatrix(graph, auto_setup=False)

    assert enigma_matrix.find_node_with_most_edges(graph) == "E"

    graph = EnigmaGraph("KEINEZUSAETZEZUMVORBERIQT", "DAEDAQOZSIQMMKBILGMPWHAIV")
    enigma_matrix = EnigmaMatrix(graph)
    assert enigma_matrix.l1 == "E"


def test_capital_to_int():
    """
    This function tests the capital_to_int method
    """
    assert EnigmaMatrix.capital_to_int("A") == 0
    assert EnigmaMatrix.capital_to_int("Z") == 25
    assert EnigmaMatrix.capital_to_int("E") == 4
    assert EnigmaMatrix.capital_to_int("L") == 11


def test_int_to_capital():
    """
    This function tests the int_to_capital method
    """
    assert EnigmaMatrix.int_to_capital(0) == "A"
    assert EnigmaMatrix.int_to_capital(25) == "Z"
    assert EnigmaMatrix.int_to_capital(4) == "E"
    assert EnigmaMatrix.int_to_capital(11) == "L"


def test_make_enigma_machines():
    """
    This function tests the make_enigma_machines method
    """
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    connected_rows = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4), (4, 5, 5), (5, 6, 6), (6, 7, 7), (7, 8, 8)]
    enigma_machines = EnigmaMatrix.make_enigma_machines(rotor1, rotor2, rotor3, reflector, connected_rows)

    # Check if the number of enigma machines is correct and if the rotor wheels are correct
    assert len(enigma_machines) == len(connected_rows)
    for enigma_machine in enigma_machines:
        assert enigma_machine.rotor1.rotor_wheel == rotor1
        assert enigma_machine.rotor2.rotor_wheel == rotor2
        assert enigma_machine.rotor3.rotor_wheel == rotor3
        assert enigma_machine.reflector.reflector_wheel == reflector

    # Check if the rotor positions are correct
    for i in range(len(enigma_machines)):
        assert enigma_machines[i].rotor1.position == 0
        assert enigma_machines[i].rotor2.position == 0
        assert enigma_machines[i].rotor3.position == i + 1


def test_connect_rows():
    """
    This function tests the connect_rows method
    """
    # Create an empty enigma matrix
    edges = [[[] for _ in range(26)] for _ in range(26)]

    # Create an enigma machine with the example rotor wheels and reflector
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    enigma_machine = EnigmaMatrix.make_enigma_machines(rotor1, rotor2, rotor3, reflector, [(0, 1, 1)])[0]

    # Connect the rows
    enigma_matrix = EnigmaMatrix(EnigmaGraph("KEINEZUSAETZEZUMVORBERIQT", "DAEDAQOZSIQMMKBILGMPWHAIV"),
                                 auto_setup=False)
    edges = enigma_matrix.connect_rows(0, 1, enigma_machine, edges)

    # Check if the edges are correct
    for col in range(len(edges)):
        # Check if they are connected mirrored
        connection = edges[0][col]
        con_r, con_c = connection[0]
        assert edges[1][con_c][0] == (0, col)

        # Check if the distance is correct
        assert enigma_machine.encrypt_letter(enigma_matrix.int_to_capital(col)) == enigma_matrix.int_to_capital(con_c)


def test_is_valid():
    """
    This function tests the is_valid method
    """
    edges = [[[] for _ in range(26)] for _ in range(26)]

    # Create a connected diagonal
    for i in range(26):
        next_index = (i + 1) % 26
        edges[i][i] = [(next_index, next_index)]

    # Check if the matrix is valid
    enigma_matrix = EnigmaMatrix(EnigmaGraph("KEINEZUSAETZEZUMVORBERIQT", "DAEDAQOZSIQMMKBILGMPWHAIV"), auto_setup=True)
    assert enigma_matrix.is_valid(edges)[0]

    # Now for an invalid matrix, where the solution is a line from top left to the bottom left
    edges = [[[] for _ in range(26)] for _ in range(26)]
    for i in range(26):
        next_index = (i + 1) % 26
        edges[i][0] = [(next_index, 0)]

    # Check if the matrix is invalid
    assert not enigma_matrix.is_valid(edges)[0]


def test_try_rotor_configuration_default():
    """
    This function tests the try_rotor_configuration method.
    This test is for the default configuration with an empty plugboard
    """
    # First a test for an empty plugboard and default configuration (0, 0, 1)
    graph = EnigmaGraph("DEOPGAVEVOORENIGMA", "KFUIYUYXIBVEJPDJSX")
    enigma_matrix = EnigmaMatrix(graph)
    rotors = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    plugboard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    test_e_m = EnigmaMachine(rotors, reflector, plugboard, [0, 0, 1])
    encrypted_text = test_e_m.encrypt_text("DEOPGAVEVOORENIGMA")
    assert encrypted_text == "KFUIYUYXIBVEJPDJSX"

    assert enigma_matrix.try_rotor_configuration("AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                                 "BDFHJLCPRTXVZNYEIWGAKMUSQO", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                                                 insta_return=True)


def test_try_rotor_configuration_custom_plugboard():
    """
    This function tests the try_rotor_configuration method.
    This test is for a default configuration with a custom plugboard
    """
    # Now a test for a non-empty plugboard and default configuration (0, 0, 1)
    graph = EnigmaGraph("DEOPGAVEVOORENIGMA", "VFSTJGYUFHDPSKHDIC")
    enigma_matrix = EnigmaMatrix(graph)
    rotors = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    # Plugboard with A and B for every pair of 2 letters
    plugboard = "BADCFEHGJILKNMPORQTSVUXWZY"
    test_e_m = EnigmaMachine(rotors, reflector, plugboard, [0, 0, 1])
    encrypted_text = test_e_m.encrypt_text("DEOPGAVEVOORENIGMA")
    assert encrypted_text == "VFSTJGYUFHDPSKHDIC"

    # Check if the rotor configuration is valid
    assert enigma_matrix.try_rotor_configuration("AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                                 "BDFHJLCPRTXVZNYEIWGAKMUSQO", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                                                 insta_return=True)


def test_try_rotor_configuration_custom_rotors():
    """
    This function tests the try_rotor_configuration method.
    This test is for a custom configuration with a custom plugboard
    """
    # Now a test for a non-empty plugboard and custom configuration (0, 0, 5)
    graph = EnigmaGraph("DEOPGAVEVOORENIGMA", "EYLLTKORSUXVWLMHGX")
    enigma_matrix = EnigmaMatrix(graph)
    rotors = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    # Plugboard with A and B for every pair of 2 letters
    plugboard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    test_e_m = EnigmaMachine(rotors, reflector, plugboard, [0, 0, 5])
    encrypted_text = test_e_m.encrypt_text("DEOPGAVEVOORENIGMA")
    assert encrypted_text == "EYLLTKORSUXVWLMHGX"

    # Check if the rotor configuration is valid
    assert enigma_matrix.try_rotor_configuration("AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                                 "BDFHJLCPRTXVZNYEIWGAKMUSQO", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                                                 insta_return=True)


def test_try_rotor_configuration_custom():
    """
    This function tests the try_rotor_configuration method.
    This test is for a custom configuration with a custom plugboard
    """
    # Now a test for a non-empty plugboard and custom configuration (0, 0, 5)
    graph = EnigmaGraph("DEOPGAVEVOORENIGMA", "EHXIRPCCPMUYYSLHCN")
    enigma_matrix = EnigmaMatrix(graph)
    rotors = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    # Plugboard with A and B for every pair of 2 letters
    plugboard = "BADCFEHGJILKNMPORQTSVUXWZY"
    test_e_m = EnigmaMachine(rotors, reflector, plugboard, [0, 0, 5])
    encrypted_text = test_e_m.encrypt_text("DEOPGAVEVOORENIGMA")
    assert encrypted_text == "EHXIRPCCPMUYYSLHCN"

    # Check if the rotor configuration is valid
    assert enigma_matrix.try_rotor_configuration("AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                                                 "BDFHJLCPRTXVZNYEIWGAKMUSQO", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                                                 insta_return=True)


def test_return_configuration():
    """
    This function tests the return_configuration method
    """
    # Create the plugboard
    plug_matrix = [[False for _ in range(26)] for _ in range(26)]
    for i in range(26):
        plug_matrix[i][i] = True

    # Create the rotor configuration
    rotors = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]

    # test the return configuration
    configuration = EnigmaMatrix.return_configuration(13673, plug_matrix, rotors[0], rotors[1], rotors[2])

    # Check the rotor config
    rotor_conf = configuration["rotor_config"]
    slow = ord(rotor_conf[0]) - 65
    middle = ord(rotor_conf[1]) - 65
    fast = ord(rotor_conf[2]) - 65

    # Check if the configuration is correct (+1 because we start at 1 while making the graph)
    assert slow * 26 ** 2 + middle * 26 + fast == 13673 + 1

    # Check the plugboard
    assert configuration["plugboard"] == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert configuration["rotor_slow"] == rotors[0]
    assert configuration["rotor_middle"] == rotors[1]
    assert configuration["rotor_fast"] == rotors[2]
