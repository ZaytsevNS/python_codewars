# Solution for task: https://www.codewars.com/kata/559cc2d2b802a5c94700000c/


from typing import List


def consecutive(arr: List[int]) -> int:
    if arr:
        return len(set(range(min(arr), max(arr) + 1)) - set(arr))
    return 0
