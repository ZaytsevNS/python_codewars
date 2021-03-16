from math import sqrt
from typing import List, Union


def sum_square_even_root_odd(nums: List[(Union[int, float])]) -> float:
    sum_nums = 0
    for i in nums:
        if i % 2 == 0:
            sum_nums += pow(i, 2)
        else:
            sum_nums += sqrt(i)
    return round(sum_nums, 2)