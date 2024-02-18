# Solution for task: https://www.codewars.com/kata/520d9c27e9940532eb00018e/

from collections import Counter


def solution(*args) -> bool:
    if not args:
        return False
    counter = Counter(args)
    return max(list(counter.values())) > 1
