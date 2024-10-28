"""
This file contains the tests for the vigenere.py file
"""
from util.letter_frequency_table import ENGLISH
from vigenere.vigenere import (get_indices, get_index_spacing, check_dividers, get_key, most_used_letter,
                               alphabet_difference, decrypt_vigenere, get_letter_frequencies, get_xi_squared_value)


def test_get_indices():
    """
    Test the get indices method
    """
    # Test with a simple example
    assert get_indices("abcabcabc", "abc") == [0, 3, 6]
    assert get_indices("abcabcabc", "bca") == [1, 4]
    assert get_indices("abcabcabc", "cab") == [2, 5]

    # Test with a more complex example
    assert get_indices("abcabcabcabc", "abc") == [0, 3, 6, 9]
    assert get_indices("abcabcabcabc", "bca") == [1, 4, 7]
    assert get_indices("abcabcabcabc", "cab") == [2, 5, 8]


def test_get_index_spacing():
    """
    Test the get index spacing method
    """
    assert get_index_spacing("abcabcabc", ["abc"]) == [3, 3, 6]
    assert get_index_spacing("abcabcabc", ["bca"]) == [3]
    assert get_index_spacing("abcabcabc", ["cab"]) == [3]
    assert get_index_spacing("abcabcabc", ["abc", "bca"]) == [3, 3, 3, 6]


def test_check_dividers():
    """
    Test the check dividers method
    """
    spacings = [3, 3, 3, 6]
    assert check_dividers(spacings, 10) == {
        2: 1,
        3: 4,
        4: 0,
        5: 0,
        6: 1,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }


def test_get_key():
    """
    Test the get key value method
    """
    cipher = """
        LIAKYQOXFOFJKGILSYBHYXHQSWYZPYDJMBQQRETOFCORGXYQOWGXGCWELICCKVQKRBRETOWRKVROHRYEEOXFOYLSZCBWGDCMPELDACBTFK
        WBOGGNIBDSYMUSSVCKRCGSLVMLOPCKVLSREZPYDJMBQGXSPNIPDSQETNYVRDLCVSAKPCMSLYQWKRBWEIOYQOSDQSTOVLWILDWSLWGNMC
        CXFOYLSZCBWGDCFKWBOGGNIBDSYCORRIYXWWWSPOWCKVARKPYYNDSBOZCVSNDLCZPYDJMBQRYKCDLCBAGDLRRIDVIKSWFCXYBXZOGYEWC
        DLCLPYMOZYEPNELNWGCENVERPSPWWFKZCLICXMLEWCCMLMIKKRWIIYBWYXHFKZCCXYBXCNXMKKCDLCERGFIPCMRISDKRRGIPZLYCHCMMBOH
        RYEAAYGBIYXIUYRJSRCVIYBRGXKNVERPSPWMLYVBOVRYWSZTMBXRRIJYGYVIAYRMWCYXHKKOCEWCYJEYZCBRKORRCYZCMBSIQDLCERGFIPC
        MRILYCHCMMBOHRYEQUXFOELCCKYVCCIYBGFQVMETRYHCFIJYTRRINVERPSPWXMQIRRIPGMRRXFOJJOQGCLQDEPD
    """.replace("\n", "").replace(" ", "").upper()

    key = get_key(cipher, 3, ENGLISH)
    assert key == "KEY"


def test_most_used_letter():
    """
    Test the most used letter method
    """
    assert most_used_letter("aaabc") == ("a", 3)


def test_alphabet_difference():
    """
    Test the alphabet difference method
    """
    assert alphabet_difference("A", "B") == "B"
    assert alphabet_difference("A", "C") == "C"
    assert alphabet_difference("A", "D") == "D"
    assert alphabet_difference("Z", "A") == "B"


def test_decrypt_vigenere():
    """
    Test the decrypt vigenere method
    """
    cipher = """
            LIAKYQOXFOFJKGILSYBHYXHQSWYZPYDJMBQQRETOFCORGXYQOWGXGCWELICCKVQKRBRETOWRKVROHRYEEOXFOYLSZCBWGDCMPELDA
            CBTFKWBOGGNIBDSYMUSSVCKRCGSLVMLOPCKVLSREZPYDJMBQGXSPNIPDSQETNYVRDLCVSAKPCMSLYQWKRBWEIOYQOSDQSTOVLWILDWS
            LWGNMCCXFOYLSZCBWGDCFKWBOGGNIBDSYCORRIYXWWWSPOWCKVARKPYYNDSBOZCVSNDLCZPYDJMBQRYKCDLCBAGDLRRIDVIKSWFCXYBXZ
            OGYEWCDLCLPYMOZYEPNELNWGCENVERPSPWWFKZCLICXMLEWCCMLMIKKRWIIYBWYXHFKZCCXYBXCNXMKKCDLCERGFIPCMRISDKRRGIPZL
            YCHCMMBOHRYEAAYGBIYXIUYRJSRCVIYBRGXKNVERPSPWMLYVBOVRYWSZTMBXRRIJYGYVIAYRMWCYXHKKOCEWCYJEYZCBRKORRCYZCMBS
            IQDLCERGFIPCMRILYCHCMMBOHRYEQUXFOELCCKYVCCIYBGFQVMETRYHCFIJYTRRINVERPSPWXMQIRRIPGMRRXFOJJOQGCLQDEPD
        """.replace("\n", "").replace(" ", "").upper()

    key = "KEY"

    solution = """
    BECAUSETHEBLACKBOARDANDSISAPLATFORMSHAVEBEENINUSESINCEMANYYEARSANDHAVESTARTEDTOAGETHEUNIVERSITYOFANTWERPHASDECIDE
    DTOACQUIREANEWONLINELEARNINGPLATFORMINORDERTOSUPPORTTHELOCALECONOMYANDMAKEUSEOFGOVERNMENTSUBSIDIESTHEUNIVERSITYHA
    SDECIDEDTOASKTHEANSYMORESEARCHGROUPTODEVELOPTHEPLATFORMTOGETHERWITHTHEFLEMISHSTARTBECAUSETHEBLACKBOARDANDSISAPL
    ATFORMSHAVEBEENINUSESINCEMANYYEARSANDHAVESTARTEDTOAGETHEUNIVERSITYOFANTWERPHASDECIDEDTOACQUIREANEWONLINELEARNINGPLAT
    FORMINORDERTOSUPPORTTHELOCALECONOMYANDMAKEUSEOFGOVERNMENTSUBSIDIESTHEUNIVERSITYHASDECIDEDTOASKTHEANSYMORESEARCHGROUP
    TODEVELOPTHEPLATFORMTOGETHERWITHTHEFLEMISHSTART
    """.replace("\n", "").replace(" ", "").upper()

    assert decrypt_vigenere(cipher, key) == solution


def test_get_letter_frequencies():
    """
    Test the get letter frequencies method
    """
    assert get_letter_frequencies("AAABBBCCCB") == {
        "A": 30,
        "B": 40,
        "C": 30
    }


def test_get_xi_squared_value():
    """
    Test the get xi squared value method
    """
    expected = {"A": 1.0, "B": 2.0}
    actual = {"A": 2.0, "B": 1.0}
    assert get_xi_squared_value(actual, expected) == 1.5
