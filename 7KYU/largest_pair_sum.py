from typing import List


def largest_pair_sum(numbers: List[int]) -> int:
    return sum(sorted(numbers, reverse=True)[:2])
    