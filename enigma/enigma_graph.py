"""
This file contains the EnigmaGraph class
"""


class EnigmaEdge:
    """
    This class represents an edge in the graph
    """

    def __init__(self, node1: str, node2: str, value: int):
        """
        Initializes the edge
        """
        self.node1: str = node1
        self.node2: str = node2
        self.value: str = value


class EnigmaGraph:
    """
    This class represents a graph
    """

    def __init__(self, crib: str, encrypted_text: str):
        """
        Initializes the graph
        """
        assert len(crib) <= len(encrypted_text), "The crib cannot be longer than the encrypted text"
        assert len(crib) > 0, "The crib cannot be empty"
        self.crib = crib
        self.encrypted_text = encrypted_text

        # Initialize the edges with keys of all capital letters
        self.edges: dict[str, list[EnigmaEdge]] = {}
        for i in range(26):
            self.edges[chr(i + 65)] = []

        # Create the graph
        self._create_graph()

    def _create_graph(self) -> None:
        """
        Creates the graph
        """
        for i in range(len(self.crib)):
            # Of the two letters, the one with the smallest ASCII value is the first node
            min_l = min(self.crib[i], self.encrypted_text[i])
            max_l = max(self.crib[i], self.encrypted_text[i])

            # Create the edge
            edge = EnigmaEdge(min_l, max_l, i + 1)
            self.edges[self.crib[i]].append(edge)
            self.edges[self.encrypted_text[i]].append(edge)
