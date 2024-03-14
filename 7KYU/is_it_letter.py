# Solution for task: https://www.codewars.com/kata/57a06b07cf1fa58b2b000252/

from string import ascii_letters


def is_it_letter(s: str) -> bool:
    return s in ascii_letters
