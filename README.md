# Slavic Translator

Simple CLI tool for comparing translations across Slavic languages.

## Features

- Translate words into multiple Slavic languages
- Cyrillic -> Latin transliteration
- Language groups:
  - East Slavic
  - West Slavic
  - South Slavic
- Simple command-line interface

## Supported languages

- Polish
- Czech
- Slovak
- Slovenian
- Croatian
- Bosnian
- Serbian
- Bulgarian
- Macedonian
- Ukrainian
- Belarusian
- Russian

## Usage

Translate into all languages:

```bash
python main.py słowo
```

Translate only East Slavic languages:

```bash
python main.py słowo --group east
```

Show original Cyrillic text:

```bash
python main.py słowo --show-original
```

You can also run it as a module:

```bash
python -m src słowo
```

## Example output

```text
      Polish : słowo
       Czech : slovo
      Slovak : slovo
   Slovenian : beseda
    Croatian : riječ
     Bosnian : riječ
     Serbian : rech [реч]
   Bulgarian : duma [дума]
  Macedonian : zbor [збор]
   Ukrainian : slovo [слово]
  Belarusian : slova [слова]
     Russian : slovo [слово]
```
