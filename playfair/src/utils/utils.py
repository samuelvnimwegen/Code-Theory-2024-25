import os
from math import sqrt


def get_file_content(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()


def create_file_names(file_name: str, directory_path: str, extension: str = "txt") -> (str, str, int):
    """
    Create filename from path and extension.
    Also use amount of files already exist in directory and use as index.
    Create also filename for progress file
    :return: filename and index (amount of files)
    """
    # Count amount of files in directory
    # Then increase name with counter
    list_files = [name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))]
    amount_of_files = len(list_files) // 2
    result_file_name = f"{directory_path}{file_name}_{amount_of_files}.{extension}"
    progress_file_name = f"{directory_path}{file_name}_PROGRESS_{amount_of_files}.{extension}"
    return result_file_name, progress_file_name, amount_of_files


def write_result(file_name: str, result_key: str, result_plaintext: str, elapsed_time: float = 0, best_score: float = 0) -> None:
    text = "[ \n \t { \n \t\t"
    text += f"\"key\": {result_key}, \n \t\t \"text\": \"{result_plaintext}\" \n \t"
    text += "} \n ]"

    if elapsed_time > 0:
        text += "\n"
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        text += f"Duration: {hours}:{minutes}:{seconds} - score: {best_score * 100} %"

    with open(file_name, 'a') as file:
        file.write(text)

    file.close()


def norm_2(vector: list[int|float]) -> float:
    """
    Calculate second norm
    """
    squares = 0
    for value in vector:
        squares += value * value

    return sqrt(squares)


def remove_letters_x(text: str) -> str:
    """
    Remove all the letters X of the text and return back in upper case
    :param text: text with(out) X's
    :return: text without X's in uppercase
    """
    return text.upper().replace('X', '')

