# Standard Library
import re

# Project
from src.languages import GROUPS
from src.languages import LANGUAGES


def has_cyrillic(text: str) -> bool:
    return bool(re.search(r'[а-яА-Я]', text))


def filter_languages(group: str) -> dict[str, str]:
    return {code: LANGUAGES[code] for code in GROUPS[group]}
