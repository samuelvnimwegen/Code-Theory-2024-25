import math

bigram_frequencies_en = dict()
bigram_frequencies_fr = dict()
bigram_frequencies_de = dict()
bigram_frequencies_es = dict()
bigram_frequencies_nl = dict()
bigram_frequencies_it = dict()


def get_frequencies(path: str, frequencies: dict[str, float]):
    """
    Get the bigram frequencies from a file.

    :param path: the path to the file
    :param frequencies: the dictionary to store the frequencies in
    :return:
    """
    with open(path, 'r') as f:
        total = 0
        text = f.read().splitlines()
        # Fix incorrect encoding
        text = fix_encoding(text)
        for line in text:
            # Skip empty line or comment
            if line.startswith("#") or len(line) == 0:
                continue
            # Split line
            try:
                bigram, frequency = line.split()
            except ValueError:
                ...
            for i in range(len(bigram)):
                # if not ever char alphabetic
                if not bigram[i].isalpha():
                    raise Exception("Bigram contains non-alphabetic character: " + bigram + " with frequency: " + frequency)
            try:
                total += int(frequency)
            except ValueError:
                raise Exception("Frequency is not a number: " + frequency)
            if bigram in frequencies:
                frequencies[bigram] += int(frequency)
            else:
                frequencies[bigram] = int(frequency)
        for bigram in frequencies:
            frequencies[bigram] = round(100 * frequencies[bigram] / total, 2)
        # Sort by frequency
        sorted_dict = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        frequencies.clear()
        frequencies.update(sorted_dict)


def fix_encoding(text: list[str]) -> list[str]:
    i = 0
    while i < len(text):
        # Skip empty line or comment
        if text[i].startswith("#") or len(text[i]) == 0:
            i += 1
            continue
        bigram, frequency = text[i].split()
        # OE
        if "Å’" in bigram:
            if bigram.index("Å") == 0:
                # OEX where X any char --> OX and EX
                text[i] = "O" + bigram[2] + " " + frequency
                text.insert(i, "E" + bigram[2] + " " + frequency)
            elif bigram.index("Å") == 1:
                # XOE where X any char --> XO and XE
                text[i] = bigram[0] + "O " + frequency
                text.insert(i, bigram[0] + "E " + frequency)
            else:
                # XXOE where X any double char --> XXO and XXE
                text[i] = bigram[0] + bigram[1] + "O " + frequency
                text.insert(i, bigram[0] + bigram[1] + "E " + frequency)
            # Update bigram
            bigram = text[i].split()[0]
        # AE
        if "Ã†" in bigram:
            if bigram.index("Ã") == 0:
                # AEX where X any char --> AX and EX
                text[i] = "A" + bigram[2] + " " + frequency
                text.insert(i, "E" + bigram[2] + " " + frequency)
            elif bigram.index("Ã") == 1:
                # XAE where X any char --> XA and XE
                text[i] = bigram[0] + "A " + frequency
                text.insert(i, bigram[0] + "E " + frequency)
            else:
                # XXAE where X any double char --> XXA and XXE
                text[i] = bigram[0] + bigram[1] + "A " + frequency
                text.insert(i, bigram[0] + bigram[1] + "E " + frequency)
            # Update bigram
            bigram = text[i].split()[0]
        # à
        bigram = bigram.replace("Ã€", "A")
        # â
        bigram = bigram.replace("Ã‚", "A")
        # ä
        bigram = bigram.replace("Ã„", "A")
        # ç
        bigram = bigram.replace("Ã‡", "C")
        # é
        bigram = bigram.replace("Ã‰", "E")
        # ë
        bigram = bigram.replace("Ã‹", "E")
        # ï
        bigram = bigram.replace("Ã", "I")
        # ñ
        bigram = bigram.replace("Ã‘", "N")
        # ö
        bigram = bigram.replace("Ã–", "O")
        # ô
        bigram = bigram.replace("Ã”", "O")
        # ù
        bigram = bigram.replace("Ã™", "U")
        # û
        bigram = bigram.replace("Ã›", "U")
        # ÿ
        bigram = bigram.replace("Å¸", "Y")

        # Update text
        text[i] = bigram + " " + frequency

        i += 1
    return text

# Get frequencies for all languages
get_frequencies("util/bigram_frequencies/english.txt", bigram_frequencies_en)
get_frequencies("util/bigram_frequencies/french.txt", bigram_frequencies_fr)
get_frequencies("util/bigram_frequencies/german.txt", bigram_frequencies_de)
get_frequencies("util/bigram_frequencies/spanish.txt", bigram_frequencies_es)