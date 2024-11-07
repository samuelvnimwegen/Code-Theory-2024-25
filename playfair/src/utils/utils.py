import os


def get_file_content(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()


def create_file_name(file_name: str, directory_path: str, extension: str = "txt") -> str:
    # Count amount of files in directory
    # Then increase name with counter
    list_files = [name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))]
    amount_of_files = len(list_files)
    return f"{directory_path}{file_name}_{amount_of_files}.{extension}"


def write_result(file_name: str, result_key: str, result_plaintext: str) -> None:
    text = "[ \n \t { \n \t\t"
    text += f"\"key\": {result_key}, \n \t\t \"text\": \"{result_plaintext}\" \n \t"
    text += "} \n ]"

    with open(file_name, 'a') as file:
        file.write(text)

    file.close()
