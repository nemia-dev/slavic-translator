# 3rd-Party
from languages import LANGUAGES
from translator import translate_word

# Project
from src.cli import parse_args
from src.helpers import filter_languages


def main():

    args = parse_args()

    languages = LANGUAGES

    if args.target:
        languages = {code: LANGUAGES[code] for code in args.target}

    if args.group:
        languages = filter_languages(args.group)

    results = translate_word(
        args.word,
        languages,
        args.show_original,
    )

    print()
    for language, translation in results:
        print(f'{language:>12} : {translation}')
    print()


if __name__ == '__main__':
    main()
