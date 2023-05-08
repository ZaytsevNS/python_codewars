# Solution for task: https://www.codewars.com/kata/62cecd4e5487c10028996e04/

from math import ceil


def race_podium(blocks: int) -> tuple:
    first = ceil(blocks / 3) + 1
    second = first - 1
    third = blocks - (first + second)
    if not third:
        second -= 1
        third += 1
    return second, first, third
