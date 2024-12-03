import os
from math import sqrt


def get_file_content(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()


def create_file_name(file_name: str, directory_path: str, extension: str = "txt") -> str:
    # Count amount of files in directory
    # Then increase name with counter
    list_files = [name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))]
    amount_of_files = len(list_files)
    return f"{directory_path}{file_name}_{amount_of_files}.{extension}"


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

