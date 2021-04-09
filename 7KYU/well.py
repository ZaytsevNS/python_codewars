from itertools import chain
from typing import List


def well(arr: List[str]) -> str:
    arr_chain: list = list(chain(*arr))
    count_good: int = 0
    for item in arr_chain:
        if type(item) == str and item.lower() == 'good':
            count_good += 1
    if 1 <= count_good <= 2:
        return 'Publish!'
    return 'I smell a series!' if count_good > 2 else 'Fail!'
    