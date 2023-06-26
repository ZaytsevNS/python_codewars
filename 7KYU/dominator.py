# Solution for task: https://www.codewars.com/kata/559e10e2e162b69f750000b4/

from collections import Counter


def dominator(arr: list) -> int:
    if arr:
        num, count = Counter(arr).most_common(1)[0]
        if count > len(arr) // 2:
            return num
        else: return -1
    else: return -1
