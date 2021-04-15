from collections import Counter
from typing import List


def stray(arr: List[int]) -> int:
    counter_list = Counter(arr)
    for k, v in counter_list.items():
        if v == 1:
            return k
