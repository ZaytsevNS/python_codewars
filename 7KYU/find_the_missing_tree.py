# Solution for task: https://www.codewars.com/kata/58aa8698ae929e1c830001c7/

from collections import Counter


def find_the_missing_tree(trees: list) -> int:
    counter = Counter(trees)
    return min(counter, key=counter.get)
