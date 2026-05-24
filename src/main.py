import argparse

from languages import LANGUAGES, GROUPS
from translator import translate_word


def filter_languages(group=None):
    if not group:
        return LANGUAGES

    allowed_codes = GROUPS[group]

    return {
        lang: code
        for lang, code in LANGUAGES.items()
        if code in allowed_codes
    }


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("word", help="Word to translate")
    parser.add_argument(
        "--group",
        choices=["east", "west", "south"],
        help="Language group",
    )

    parser.add_argument(
        "--show-original",
        action="store_true",
        help="Show original Cyrillic text",
    )

    args = parser.parse_args()

    languages = filter_languages(args.group)

    results = translate_word(
        args.word,
        languages,
        args.show_original,
    )

    print()

    for language, translation in results:
        print(f"{language:>12} : {translation}")

    print()


if __name__ == "__main__":
    main()
