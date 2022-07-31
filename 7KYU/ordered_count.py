# Solution for task: https://www.codewars.com/kata/57a6633153ba33189e000074/

from collections import Counter


def ordered_count(inp: str) -> list:
    return [(k, v) for k, v in Counter(inp).items()]
