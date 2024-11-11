"""
This file contains the tests for the bigram_frequencies module.
"""

from adfgvx.frequency_analysis import get_letter_frequencies as get_letter_frequencies


def test_frequencies1():
    text = "Hello, World!!"
    expected = {"He": round(100 * 1/7, 2), "ll": round(100 * 1/7, 2), "o,": round(100 * 1/7, 2),
                " W": round(100 * 1/7, 2), "or": round(100 * 1/7, 2), "ld": round(100 * 1/7, 2),
                "!!": round(100 * 1/7, 2)}
    result = get_letter_frequencies(text)
    assert result == expected, f"Expected {expected} but got {result}"


def test_frequencies2():
    text = "XAVGGDGDGFXGGXVDDDGVGDDFDXDXAXAXVGFDXGGGGXGVAX"
    # XA VG GD GD GF XG GX VD DD GV GD DF DX DX AX AX VG FD XG GG GX GV AX
    # 1  1  1  2  1  1  1  1  1  1  3  1  1  2  1  2  2  1  2  1  2  2  3
    expected = {"XA": round(100 * 1/23, 2), "VG": round(100 * 2/23, 2), "GD": round(100 * 3/23, 2),
                "GF": round(100 * 1/23, 2), "XG": round(100 * 2/23, 2), "GX": round(100 * 2/23, 2),
                "VD": round(100 * 1/23, 2), "DD": round(100 * 1/23, 2), "GV": round(100 * 2/23, 2),
                "DF": round(100 * 1/23, 2), "DX": round(100 * 2/23, 2), "AX": round(100 * 3/23, 2),
                "FD": round(100 * 1/23, 2), "GG": round(100 * 1/23, 2)}
    result = get_letter_frequencies(text)
    assert result == expected, f"Expected {expected} but got {result}"