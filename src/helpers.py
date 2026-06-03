# Standard Library
import re

# Local
from .languages import GROUPS
from .languages import LANGUAGES


def has_cyrillic(text: str) -> bool:
    return bool(re.search(r'[а-яА-Я]', text))


def filter_languages(group: str) -> dict[str, str]:
    return {code: LANGUAGES[code] for code in GROUPS[group]}
