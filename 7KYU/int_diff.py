from itertools import combinations


def int_diff(lst: list, n: int) -> int:
    return sum([1 for i in list(combinations(lst, 2)) if abs(i[0]-i[1]) == n])
