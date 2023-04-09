# Solution for task: https://www.codewars.com/kata/55e9529cbdc3b29d8c000016/

from string import ascii_letters
from typing import Optional


def char_to_ascii(s: str) -> Optional[dict]:
    
    char_and_ascii_values: dict = {}
    
    if s:
        for i in s:
            if i in ascii_letters and i not in char_and_ascii_values.keys():
                char_and_ascii_values[i] = ord(i)
        return char_and_ascii_values
    else:
        return None
