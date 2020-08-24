import re
from enum import Enum, auto
from typing import List, Dict


class LanguageLevel(Enum):
    UNDEFINED = auto()
    BASIC = auto()
    PRE_INTERMEDIATE = auto()
    INTERMEDIATE = auto()
    UPPER_INTERMEDIATE = auto()
    ADVANCED = auto()
    PROFICIENT = auto()
    NATIVE = auto()

    def pretty_name(self) -> str:
        return self.name.lower().replace('_', ' ')


class Language(Enum):
    ARABIC = auto()
    ARMENIAN = auto()
    AZERBAIJANI = auto()
    BELORUSSIAN = auto()
    BULGARIAN = auto()
    CHINESE = auto()
    CZECH = auto()
    ENGLISH = auto()
    DUTCH = auto()
    FINNISH = auto()
    GEORGIAN = auto()
    GREEK = auto()
    HEBREW = auto()
    HINDI = auto()
    HUNGARIAN = auto()
    INDONESIAN = auto()
    JAPANESE = auto()
    FRENCH = auto()
    GERMAN = auto()
    ITALIAN = auto()
    LATVIAN = auto()
    KAZAKH = auto()
    KOREAN = auto()
    KYRGYZ = auto()
    LATIN = auto()
    POLISH = auto()
    PORTUGUESE = auto()
    ROMANIAN = auto()
    RUSSIAN = auto()
    SERBIAN = auto()
    SPANISH = auto()
    SWEDISH = auto()
    TAJIK = auto()
    TATAR = auto()
    THAI = auto()
    TURKISH = auto()
    UKRAINIAN = auto()
    UZBEK = auto()
    YAKUT = auto()
    PERSIAN = auto()
    UNKNOWN = auto()

    def pretty_name(self) -> object:
        return self.name.lower().capitalize()


def parse_language(language_str: str) -> Dict[Language, LanguageLevel]:
    result = {}
    if language_str:
        languages = language_str.split(', ')
        for language in languages:
            match = re.fullmatch("(\\S+)\\s+\\((\\S+)\\)", language)
            if match:
                result[_parse_language_name(match.group(1))] = _parse_language_level(match.group(2))
    return result


def _parse_language_name(language_name_str: str) -> Language:
    for language in list(Language):
        if language.name.lower() == language_name_str.lower():
            return language
    print(f"Unknown language: {language_name_str}")
    return Language.UNKNOWN


def _parse_language_level(level_str: str) -> LanguageLevel:
    if level_str == 'Basic':
        return LanguageLevel.BASIC
    elif level_str == 'Pre_Intermediate':
        return LanguageLevel.PRE_INTERMEDIATE
    elif level_str == 'Intermediate':
        return LanguageLevel.INTERMEDIATE
    elif level_str == 'Upper_Intermediate':
        return LanguageLevel.UPPER_INTERMEDIATE
    elif level_str == 'Advanced':
        return LanguageLevel.ADVANCED
    elif level_str == 'Proficient':
        return LanguageLevel.PROFICIENT
    elif level_str == 'Native':
        return LanguageLevel.NATIVE
    elif level_str == 'undefined':
        return LanguageLevel.UNDEFINED
    else:
        print(f'Unknown language level {level_str}')
        return LanguageLevel.UNDEFINED
