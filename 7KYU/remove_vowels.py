import re


def remove_vowels(strng: str) -> str:
    strng = re.sub('[aeiou]', '', strng)
    return strng
