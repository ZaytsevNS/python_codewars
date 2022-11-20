# Solution for task: https://www.codewars.com/kata/55ea5650fe9247a2ea0000a7/

from re import sub


def unscramble_eggs(word: str) -> str:
    return sub('egg', '', word)
