"""
This file contains the tests for the chi_squared function in the frequency_analysis module.
"""

from adfgvx.frequency_analysis import chi_squared

def test_chi_squared1():
    frequencies = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
    language = {'A': 10, 'B': 20, 'C': 30, 'D': 40}

    # Expected result is 0.0 because the frequencies are the same
    result = chi_squared(frequencies, language)
    expected = float(0)
    assert result == expected

def test_chi_squared2():
    frequencies = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
    language = {'A': 20, 'B': 30, 'C': 40, 'D': 10}

    # (10 - 20)² / 20 = 5
    # (20 - 30)² / 30 = 3.33 (repeating)
    # (30 - 40)² / 40 = 2.5
    # (40 - 10)² / 10 = 90
    # Total = 100.83 (with rounding)
    result = chi_squared(frequencies, language)
    expected = float(100.83)
    assert result == expected

def test_chi_squared3():
    # Test with all letters and 1 number in frequencies
    frequencies = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50, 'F': 60, 'G': 70, 'H': 80, 'I': 90, 'J': 100, 'K': 110, 'L': 120, 'M': 130, 'N': 140, 'O': 150, 'P': 160, 'Q': 170, 'R': 180, 'S': 190, 'T': 200, 'U': 210, 'V': 220, 'W': 230, 'X': 240, 'Y': 250, 'Z': 260, '1': 270}
    language = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50, 'F': 60, 'G': 70, 'H': 80, 'I': 90, 'J': 100, 'K': 110, 'L': 120, 'M': 130, 'N': 140, 'O': 150, 'P': 160, 'Q': 170, 'R': 180, 'S': 190, 'T': 200, 'U': 210, 'V': 220, 'W': 230, 'X': 240, 'Y': 250, 'Z': 260}

    # Expected result is infinite because more than 26 letters are in frequencies
    result = chi_squared(frequencies, language)
    expected = float('inf')
    assert result == expected