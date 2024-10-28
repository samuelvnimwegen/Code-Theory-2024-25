
def text_only_alphabet(text: str) -> bool:
    """
    Check only the use of alphabetical characters
    :return: true/false
    """
    return text.isalpha()


def text_no_j(text: str) -> bool:
    """
    Check that character J is not used, as I=J
    :return: true/false
    """
    return 'J' not in text


def keyword_no_double_letter(keyword: str) -> bool:
    """
    Check that the keyword does not contain repeated letters
    :return: true/false
    """
    keyword_upper = keyword.upper()
    seen = set()
    for letter in keyword_upper:
        if letter in seen:
            return False
        seen.add(letter)
    return True


def no_spaces_in_text(text: str) -> bool:
    """
    Check that there are no spaces in the text
    :return: true/false
    """
    return ' ' not in text



