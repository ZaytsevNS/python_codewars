from numpy import median as np_median
from typing import Union

def median(array: list) -> Union[int, float]:
#      With numpy
    return np_median(array)

#     Without numpy
#     sorted_array = sorted(array)
#     len_array = len(array)
#     if not len_array % 2:
#         return (sorted_array[len_array//2]+sorted_array[len_array//2 - 1]) / 2
#     else:
#         return sorted_array[len_array//2]