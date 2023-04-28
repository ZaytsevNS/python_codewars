# Solution for task: https://www.codewars.com/kata/6347f9715467f0001b434936/

from math import sqrt
from typing import Optional


def thin_or_fat(matrix: list) -> Optional[str]:
    try:
        sum_width = sum([sqrt(sum(i)) for i in matrix])
        sum_height = sum([sqrt(sum(i)) for i in zip(*matrix)])
        return 'thin' if sum_width < sum_height  else ('fat' if sum_width > sum_height else 'perfect')
    except ValueError:
        return None
