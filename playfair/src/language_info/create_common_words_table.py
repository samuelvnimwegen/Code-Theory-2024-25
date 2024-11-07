"""
This file was a one time use to create the lists of common words
"""

from playfair.src.scoring_algorithms import languages

if __name__ == '__main__':
    text = "\n\n"
    for language in languages.keys():
        text += f"{language} = ["
        with open(f"{language}_most_common_words.txt", 'r') as file:
            for line in file:
                text += f"\"{line.strip()}\", "
        file.close()

        text = text[:-1]
        text += "] \n\n"

    with open("most_common_words.py", 'a') as file:
        file.write(text)

    file.close()


