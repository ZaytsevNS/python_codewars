# Solution for task: https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/

from re import findall, sub


def remove_parentheses(s: str) -> str:
    while findall(r"\([^()]*\)", s):
        s = sub(r"\([^()]*\)", "", s)
    return s
