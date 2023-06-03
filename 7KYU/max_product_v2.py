# Solution for task: https://www.codewars.com/kata/5784c89be5553370e000061b/

import heapq


def max_product(a: list) -> int:
    first, second = heapq.nlargest(2, a)
    return first * second
