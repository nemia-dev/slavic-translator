if __package__ in (None, ''):
    # Standard Library
    import sys
    from pathlib import Path

    project_root = Path(__file__).resolve().parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    # Project
    from src.cli import parse_args
    from src.helpers import filter_languages
    from src.languages import LANGUAGES
    from src.translator import translate_word
else:
    # Local
    from .cli import parse_args
    from .helpers import filter_languages
    from .languages import LANGUAGES
    from .translator import translate_word


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
