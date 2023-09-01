# Solution for task: https://www.codewars.com/kata/5168b125faced29f66000005/

from re import findall


def solution(full_text: str, search_text: str) -> int:
    return len(findall(search_text, full_text))
