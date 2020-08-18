from typing import List
import re

class Language:
    def __init__(self, language, level):
        self.language = language
        self.level = level


def parse_language (language_str: str) -> List[Language]:
    if not language_str:
        return []
    languages = language_str.split(', ')
    result = []
    for language in languages:
        match = re.fullmatch("(\\S+)\\s+\\((\\S+)\\)")
        if match:
            result.append(Language(match.group(1), match.group(2)))
    return result

