from typing import List


def presents(arr: List[int]) -> List[int]:
    return list(map(lambda x: x + 1, [arr.index(i) for i, k in enumerate(arr, start=1)]))
