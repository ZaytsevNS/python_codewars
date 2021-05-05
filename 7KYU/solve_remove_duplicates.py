from typing import List


def solve(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    list_without_duplicates = []
    for item in arr[::-1]:
        if item not in list_without_duplicates:
            list_without_duplicates.append(item)
    return list_without_duplicates[::-1]
    