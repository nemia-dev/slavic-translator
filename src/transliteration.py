CYR_TO_LAT = {
    "а": "a", "б": "b", "в": "v", "г": "g",
    "д": "d", "е": "e", "ё": "yo", "ж": "zh",
    "з": "z", "и": "i", "й": "y", "к": "k",
    "л": "l", "м": "m", "н": "n", "о": "o",
    "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "kh", "ц": "ts",
    "ч": "ch", "ш": "sh", "щ": "shch",
    "ъ": "", "ы": "y", "ь": "",
    "э": "e", "ю": "yu", "я": "ya",
}


def transliterate(text: str) -> str:
    result = []

    for char in text:
        lower = char.lower()

        if lower in CYR_TO_LAT:
            translated = CYR_TO_LAT[lower]

            if char.isupper():
                translated = translated.capitalize()

            result.append(translated)
        else:
            result.append(char)

    return "".join(result)
