# 3rd-Party
from helpers import has_cyrillic
from mtranslate import translate
from transliteration import transliterate


def translate_word(word: str, languages: dict, show_original=False):
    results = []

    for language_name, code in languages.items():
        try:
            translation = translate(word, code)

            if has_cyrillic(translation):
                latin = transliterate(translation)

                if show_original:
                    formatted = f'{latin} [{translation}]'
                else:
                    formatted = latin
            else:
                formatted = translation

            results.append((language_name, formatted))

        except Exception as e:
            results.append((language_name, f'ERROR: {e}'))

    return results
