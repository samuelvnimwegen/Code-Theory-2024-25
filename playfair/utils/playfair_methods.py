import copy
from ..playfair_matrix import PlayfairMatrix

def replace_J_with_I(text: str) -> str:
    replace_string = ""
    for i in range(len(text)):
        if text[i] == 'J':
            replace_string += 'I'
            continue
        replace_string += text[i]

    return replace_string


def equal_letters(letter_1, letter_2) -> bool:
    if letter_1 == letter_2:
        return True

    #  ot necessary to check I and J as every J is replaced with I
    # if (letter_1 == 'J' and letter_2 == 'I') or (letter_1 == 'I' and letter_2 == 'J'):
    #     return True
    return False


def split_text_in_correct_pairs(text: str) -> str:
    """
    Split the text in pairs where each pair with same letter adds X between the letters and at the end add X if text is uneven length
    :return: the new string with added X's
    """
    splitted_text = copy.deepcopy(text)
    x_process_not_done = True
    while x_process_not_done:
        x_process_not_done = False
        for i in range(len(splitted_text) // 2):
            letter_1 = splitted_text[i * 2]
            letter_2 = splitted_text[i * 2 + 1]
            if not equal_letters(letter_1, letter_2):
                continue
            temp_plaintext = splitted_text[:i * 2 + 1] + 'X' + splitted_text[i * 2 + 1:]
            splitted_text = temp_plaintext
            x_process_not_done = True
            break

    if len(splitted_text) % 2 != 0:
        splitted_text += 'X'

    return splitted_text


def replace_pairs(letter_1: str, letter_2: str, matrix: PlayfairMatrix, encryption=True) -> str:
    dx = +1
    if not encryption:
        dx = -1

    if equal_letters(letter_1, letter_2):
        raise ValueError(f"Pairs can't be same letter: {letter_1} and {letter_2}")

    row_l1, col_l1 = matrix.get_letter_coordinates(letter_1)
    row_l2, col_l2 = matrix.get_letter_coordinates(letter_2)

    if row_l1 == row_l2 and col_l1 == col_l2:
        raise ValueError(f"Different letters cant have same coordinates: {letter_1} ({row_l1}, {col_l1}) and {letter_2} ({row_l2}, {col_l2})")

    if row_l1 == row_l2:
        # Both letters in same row
        # Go both one step right
        new_col_l1 = (col_l1 + dx) % 5
        new_col_l2 = (col_l2 + dx) % 5

        new_letter1 = matrix.get_letter(row_l1, new_col_l1)
        new_letter2 = matrix.get_letter(row_l2, new_col_l2)
        return new_letter1 + new_letter2

    if col_l1 == col_l2:
        # Both letters in same column
        # Go both one step down
        new_row_l1 = (row_l1 + dx) % 5
        new_row_l2 = (row_l2 + dx) % 5

        new_letter1 = matrix.get_letter(new_row_l1, col_l1)
        new_letter2 = matrix.get_letter(new_row_l2, col_l2)
        return new_letter1 + new_letter2

    # Letters not in same row or column
    # Switch each other column index == go to other corner of created rectangle
    new_letter1 = matrix.get_letter(row_l1, col_l2)
    new_letter2 = matrix.get_letter(row_l2, col_l1)
    return new_letter1 + new_letter2



