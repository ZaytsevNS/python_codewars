import math


def double_integer(i: int) -> int:
    if i >= 0:
        return round(2 * math.sqrt(i) * math.sqrt(i))
    return 2 * i