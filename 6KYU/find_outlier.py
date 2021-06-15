from typing import List


def find_outlier(integers: List[int]) -> int:
    odd, even = [i for i in integers if not i % 2], [i for i in integers if i % 2]
    if len(odd) > len(even):
        return int(''.join(map(str, even)))
    else:
        return int(''.join(map(str, odd)))
        