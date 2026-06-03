# Standard Library
import argparse
from typing import Literal

# 3rd-Party
from pydantic import BaseModel
from pydantic import field_validator

# Local
from .languages import LANGUAGES


class Args(BaseModel):
    word: str
    target: list[str] | None = None
    group: Literal['east', 'west', 'south'] | None = None
    show_original: bool = False

    @field_validator('target')
    @classmethod
    def validate_target(cls, value):
        if value is not None and value not in LANGUAGES:
            raise ValueError(f'target must be one of: {", ".join(LANGUAGES.keys())}')
        return value


def parse_args() -> Args:
    parser = argparse.ArgumentParser()

    parser.add_argument('word', help='Word to translate')
    parser.add_argument(
        '--target',
        nargs='+',
        choices=LANGUAGES.keys(),
        help='Target language code',
    )
    parser.add_argument(
        '--group',
        choices=['east', 'west', 'south'],
        help='Language group',
    )
    parser.add_argument(
        '--show-original',
        action='store_true',
        help='Show original Cyrillic text',
    )

    namespace = parser.parse_args()

    return Args.model_validate(vars(namespace))
