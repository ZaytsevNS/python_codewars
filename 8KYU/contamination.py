# Solution for task: https://www.codewars.com/kata/596fba44963025c878000039/

from re import sub


def contamination(text: str, char: str) -> str:
    return sub(r'\S', char, text)
