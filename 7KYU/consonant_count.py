# Solution for task: https://www.codewars.com/kata/564e7fc20f0b53eb02000106/

from re import findall


def consonant_count(s: str) -> int:
    return len(findall(r'[^(\W)(0-9)(aeiou)(_)]', s.lower()))
