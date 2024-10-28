import copy


def equal_letters(letter_1, letter_2) -> bool:
    if letter_1 == letter_2:
        return True

    if (letter_1 == 'J' and letter_2 == 'I') or (letter_1 == 'I' and letter_2 == 'J'):
        return True

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


