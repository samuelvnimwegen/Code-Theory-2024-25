"""
This module contains a function to decode a morse code string
"""


def decode(code: str) -> str:
    """
    Decodes a morse code string

    :param code: the morse code string
    :return: the decoded string
    """
    # Remove slash at end
    if code[-1] == '/':
        code = code[:-1]
    # Morse code dictionary
    morse_dict = {'.-': 'A', '-..': 'D', '..-.': 'F', '--.': 'G', '...-': 'V', '-..-': 'X'}
    # Check if all morse code characters are valid (split by '/', check if every string is in the dictionary, ignore empty strings)
    assert all([i in morse_dict if len(i) != 0 else True for i in code.split('/')]), 'Invalid morse code'
    # Return the decoded string
    return ''.join([morse_dict.get(i, ' ') for i in code.split('/')])

def encode(plain: str) -> str:
    """
    Encodes a string to morse code

    :param plain: the string to encode
    :return: the encoded string
    """
    # Morse code dictionary
    morse_dict = {'A': '.-', 'D': '-..', 'F': '..-.', 'G': '--.', 'V': '...-', 'X': '-..-'}
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plain = plain.upper()
    # Check if all characters are valid (ignore spaces)
    assert all([i in alphabet if i != ' ' else True for i in plain]), 'Invalid character'
    # Return the encoded string
    return '/'.join([morse_dict.get(i, ' ') for i in plain]) + '/'