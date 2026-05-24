# Standard Library
import re


def has_cyrillic(text: str) -> bool:
    return bool(re.search(r'[а-яА-Я]', text))
