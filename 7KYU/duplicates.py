# Solution for task: https://www.codewars.com/kata/5558cc216a7a231ac9000022/

from collections import Counter


def duplicates(arr: list) -> list:
    result = []
    counter = Counter()
    for i in arr:
        counter[i] += 1
        if counter[i] == 2:
            result.append(i)
    return result
