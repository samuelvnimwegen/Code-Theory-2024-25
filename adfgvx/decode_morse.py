"""
This module contains a function to decode a morse code string
"""


def decode(code: str) -> str:
    """
    Decodes a morse code string

    :param code: the morse code string
    :return: the decoded string
    """
    # Morse code dictionary
    morse_dict = {'.-': 'A', '-..': 'D', '..-.': 'F', '--.': 'G', '...-': 'V', '-..-': 'X'}
    # Check if all morse code characters are valid (split by '/', check if every string is in the dictionary, ignore empty strings)
    assert all([i in morse_dict if len(i) != 0 else True for i in code.split('/')]), 'Invalid morse code'
    # Return the decoded string
    return ''.join([morse_dict.get(i, ' ') for i in code.split('/')])