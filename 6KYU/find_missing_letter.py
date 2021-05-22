from string import ascii_letters
from operator import itemgetter
from typing import List


def find_missing_letter(chars: List[str]) -> str:
    eng_letters: dict = {idx: letter for idx, letter in enumerate(ascii_letters, start=1)}
    if chars[0].islower():
        first_letter: int, last_letter: int = ord(chars[0]) - 96, ord(chars[-1]) - 96
    else:
        first_letter: int, last_letter: int = ord(chars[0]) - 38, ord(chars[-1]) - 38
    letters_from_first_to_last_letter = itemgetter(*range(first_letter, last_letter + 1))(eng_letters)
    return ''.join(set(letters_from_first_to_last_letter) - set(chars)) 
    