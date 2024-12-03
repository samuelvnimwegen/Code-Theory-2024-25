def load_quad_grams(file_path="playfair/src/language_info/4grams.txt") -> dict[str, int]:
    """
    Load a dictionary file into a dict for quick lookups.
    Each line is expected to be in the format: 'word value'.
    """
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split each line into word and value
            word, value = line.strip().split()
            dictionary[word] = int(value)
    return dictionary


EN_QUAD_GRAM_DICT: dict[str, int] = load_quad_grams()
EN_TOTAL_QUADGRAMS: int = sum(EN_QUAD_GRAM_DICT.values())
