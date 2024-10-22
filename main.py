import os.path
from logging import raiseExceptions


def ask_for_path() -> str | None:
    # Ask the user for a path to the code.
    print("Enter the path to the file or 'exit' to return to the main menu.")
    path = input("")

    # Exit
    if path == "exit":
        return "exit"

    # Return the path if it exists
    if os.path.exists(path):
        return path
    return None


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()


def vigenere_plus_decrypt(input: str):
    raise NotImplementedError("Not implemented yet")


def playfair_decrypt(input: str):
    raise NotImplementedError("Not implemented yet")


def adfgvx_decrypt(input: str):
    from decrypt.adfgvx import ADFGVX
    adfgvx_instance = ADFGVX(input)
    adfgvx_instance.decrypt()


def enigma_decrypt(input: str):
    raise NotImplementedError("Not implemented yet")


def decrypt():
    # Menu
    choices = {1: "Vigenere Plus", 2: "Playfair", 3: "ADFGVX", 4: "Enigma", 5: "Exit"}
    methods = {1: vigenere_plus_decrypt, 2: playfair_decrypt, 3: adfgvx_decrypt, 4: enigma_decrypt}
    while True:
        # Print menu.
        print("Options:")
        for key, value in choices.items():
            print(f"{key}. {value}")

        # Get user choice.
        choice = input("")

        # Check if choice is a digit.
        if not choice.isdigit():
            print("Invalid choice.")
            continue
        choice = int(choice)

        # Check if choice is valid.
        if choice not in choices.keys():
            print("Invalid choice.")
            continue

        # Exit.
        if choice == 5:
            break

        # Print selected choice.
        print(f"Selected {choices[int(choice)]}")

        # Decrypt.
        while True:
            # Ask for path.
            path = ask_for_path()

            # Check if path exists.
            if path is None:
                continue

            # Exit to main menu.
            if path == "exit":
                break

            # Decrypt
            code = read_file(path)
            methods[int(choice)](code)
            break


# Call decrypt function.
if __name__ == '__main__':
    decrypt()
