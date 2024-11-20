"""
This file contains the tests for the EnigmaGraph class
"""

from enigma.enigma_graph import EnigmaGraph, EnigmaEdge


def test_enigma_graph():
    """
    Tests the EnigmaGraph class
    """
    # Example from the course
    crypt_text = "DAEDAQOZSIQMMKBILGMPWHAIV"
    crib = "KEINEZUSAETZEZUMVORBERIQT"

    # Create the graph
    graph = EnigmaGraph(crib, crypt_text)

    assert len(graph.edges["L"]) == 1
    assert len(graph.edges["V"]) == 2
    assert len(graph.edges["A"]) == 4

    assert graph.edges["L"][0].node1 in ["L", "V"]
    assert graph.edges["L"][0].node2 in ["L", "V"]
    assert graph.edges["L"][0].value == 17
