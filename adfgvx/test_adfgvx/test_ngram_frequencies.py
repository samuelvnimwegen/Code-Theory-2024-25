"""
This file contains the tests for the n-gram_frequencies module.
"""

from adfgvx.frequency_analysis import get_frequencies, get_frequencies_ngrams


def test_frequencies1():
    text = "Hello, World!"
    text = list(text)
    expected = {"He": round(100 * 1/12, 2), "el": round(100 * 1/12, 2), "ll": round(100 * 1/12, 2),
                "lo": round(100 * 1/12, 2), "o,": round(100 * 1/12, 2), ", ": round(100 * 1/12, 2),
                " W": round(100 * 1/12, 2), "Wo": round(100 * 1/12, 2), "or": round(100 * 1/12, 2),
                "rl": round(100 * 1/12, 2), "ld": round(100 * 1/12, 2), "d!": round(100 * 1/12, 2)}
    result = get_frequencies_ngrams(text, 2)
    assert result == expected, f"Expected {expected} but got {result}"

def test_frequencies2():
    text = "Hello, World!"
    text = list(text)
    expected = {"Hel": round(100 * 1/11, 2), "ell": round(100 * 1/11, 2), "llo": round(100 * 1/11, 2),
                "lo,": round(100 * 1/11, 2), "o, ": round(100 * 1/11, 2), ", W": round(100 * 1/11, 2),
                " Wo": round(100 * 1/11, 2), "Wor": round(100 * 1/11, 2), "orl": round(100 * 1/11, 2),
                "rld": round(100 * 1/11, 2), "ld!": round(100 * 1/11, 2)}
    result = get_frequencies_ngrams(text, 3)
    assert result == expected, f"Expected {expected} but got {result}"

def test_frequencies3():
    text = "Hello, World!"
    text = list(text)
    expected = {"Hell": round(100 * 1/10, 2), "ello": round(100 * 1/10, 2), "llo,": round(100 * 1/10, 2),
                "lo, ": round(100 * 1/10, 2), "o, W": round(100 * 1/10, 2), ", Wo": round(100 * 1/10, 2),
                " Wor": round(100 * 1/10, 2), "Worl": round(100 * 1/10, 2), "orld": round(100 * 1/10, 2),
                "rld!": round(100 * 1/10, 2)}
    result = get_frequencies_ngrams(text, 4)
    assert result == expected, f"Expected {expected} but got {result}"

def test_frequencies4():
    text = "ADADADFGVX"
    expected = {"AD": round(100 * 3/5, 2), "FG": round(100 * 1/5, 2), "VX": round(100 * 1/5, 2)}
    result = get_frequencies(text)
    assert result == expected, f"Expected {expected} but got {result}"

def test_frequencies5():
    text = "ADFGVXADFGVXADFGVXADFGVXADFGVXADFGVXADFGVXADFGVXADFGVXADFGVXADADADADADADADADADAD"
    # 10x AD FG VX + 10x AD = 40 = 20x AD, 10x FG, 10x VX
    expected = {"AD": round(100 * 20/40, 2), "FG": round(100 * 10/40, 2), "VX": round(100 * 10/40, 2)}
    result = get_frequencies(text)
    assert result == expected, f"Expected {expected} but got {result}"

def test_frequencies6():
    text = "XAVGGDGDGFXGGXVDDDGVGDDFDXDXAXAXVGFDXGGGGXGVAX"
    # XA VG GD GD GF XG GX VD DD GV GD DF DX DX AX AX VG FD XG GG GX GV AX
    # 1  1  1  2  1  1  1  1  1  1  3  1  1  2  1  2  2  1  2  1  2  2  3
    expected = {"XA": round(100 * 1/23, 2), "VG": round(100 * 2/23, 2), "GD": round(100 * 3/23, 2),
                "GF": round(100 * 1/23, 2), "XG": round(100 * 2/23, 2), "GX": round(100 * 2/23, 2),
                "VD": round(100 * 1/23, 2), "DD": round(100 * 1/23, 2), "GV": round(100 * 2/23, 2),
                "DF": round(100 * 1/23, 2), "DX": round(100 * 2/23, 2), "AX": round(100 * 3/23, 2),
                "FD": round(100 * 1/23, 2), "GG": round(100 * 1/23, 2)}
    result = get_frequencies(text)
    assert result == expected, f"Expected {expected} but got {result}"