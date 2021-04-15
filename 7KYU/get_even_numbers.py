from typing import List


def get_even_numbers(arr: List[int]) -> List[int]:
    if len(arr) < 1:
        return []
    return list(filter(lambda i: not(i % 2), arr))
