from typing import List


def small_enough(array: List[int], limit: int) -> bool:
    return all(i <= limit for i in array)
    