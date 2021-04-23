from typing import Optional


def even_last(numbers: Optional[int]) -> int:
    if len(numbers) == 0:
        return 0
    sum_even = sum([numbers[i] for i, k in enumerate(range(len(numbers))) if not k % 2])
    return sum_even * numbers[-1]
