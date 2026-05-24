symbols = (
    u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"
)

tr = {ord(a): ord(b) for a, b in zip(*symbols)}

slavic_languages = {
    'Polski': 'pl',
    'Czeski': 'cs',
    'Białoruski': 'be',
    'Rosyjski': 'ru',
    'Ukraiński': 'uk',
    'Bośniacki': 'bs',
    'Bułgarski': 'bg',
    'Chorwacki': 'hr',
    'Macedoński': 'mk',
    'Serbski': 'sr',
    'Słoweński': 'sl',
    'Słowacki': 'sk',
}
