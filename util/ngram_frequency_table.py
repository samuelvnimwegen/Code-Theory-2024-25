import os.path


def get_frequencies(language: str, n: int, frequencies: dict[str, float]):
    """
    Get the ngram frequencies from a file.

    :param language: the language of the ngrams
    :param n: the n
    :param frequencies: the dictionary to store the frequencies in
    :return:
    """
    path = "util/ngram_frequencies/" + language + "_" + str(n) + "grams.txt"
    if not os.path.exists(path):
        return
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
                ngram, frequency = line.split()
            except ValueError:
                ...
            for i in range(len(ngram)):
                # if not ever char alphabetic
                if not ngram[i].isalpha():
                    raise Exception("N-gram contains non-alphabetic character: " + ngram + " with frequency: " + frequency)
            try:
                total += int(frequency)
            except ValueError:
                raise Exception("Frequency is not a number: " + frequency)
            if ngram in frequencies:
                frequencies[ngram] += int(frequency)
            else:
                frequencies[ngram] = int(frequency)
        for ngram in frequencies:
            frequencies[ngram] = round(100 * frequencies[ngram] / total, 2)
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
        ngram, frequency = text[i].split()
        # OE
        if "Å’" in ngram:
            if ngram.index("Å") == 0:
                # OEX where X any char --> OX and EX
                text[i] = "O" + ngram[2] + " " + frequency
                text.insert(i, "E" + ngram[2] + " " + frequency)
            elif ngram.index("Å") == 1:
                # XOE where X any char --> XO and XE
                text[i] = ngram[0] + "O " + frequency
                text.insert(i, ngram[0] + "E " + frequency)
            else:
                # XXOE where X any double char --> XXO and XXE
                text[i] = ngram[0] + ngram[1] + "O " + frequency
                text.insert(i, ngram[0] + ngram[1] + "E " + frequency)
            # Update ngram
            ngram = text[i].split()[0]
        # AE
        if "Ã†" in ngram:
            if ngram.index("Ã") == 0:
                # AEX where X any char --> AX and EX
                text[i] = "A" + ngram[2] + " " + frequency
                text.insert(i, "E" + ngram[2] + " " + frequency)
            elif ngram.index("Ã") == 1:
                # XAE where X any char --> XA and XE
                text[i] = ngram[0] + "A " + frequency
                text.insert(i, ngram[0] + "E " + frequency)
            else:
                # XXAE where X any double char --> XXA and XXE
                text[i] = ngram[0] + ngram[1] + "A " + frequency
                text.insert(i, ngram[0] + ngram[1] + "E " + frequency)
            # Update ngram
            ngram = text[i].split()[0]
        # à
        ngram = ngram.replace("Ã€", "A")
        # â
        ngram = ngram.replace("Ã‚", "A")
        # ä
        ngram = ngram.replace("Ã„", "A")
        # ç
        ngram = ngram.replace("Ã‡", "C")
        # é
        ngram = ngram.replace("Ã‰", "E")
        # ë
        ngram = ngram.replace("Ã‹", "E")
        # ï
        ngram = ngram.replace("Ã", "I")
        # ñ
        ngram = ngram.replace("Ã‘", "N")
        # ö
        ngram = ngram.replace("Ã–", "O")
        # ô
        ngram = ngram.replace("Ã”", "O")
        # ù
        ngram = ngram.replace("Ã™", "U")
        # û
        ngram = ngram.replace("Ã›", "U")
        # ÿ
        ngram = ngram.replace("Å¸", "Y")

        # Update text
        text[i] = ngram + " " + frequency

        i += 1
    return text

