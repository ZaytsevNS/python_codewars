from math import log2


def power_of_two(x: int) -> bool:
    if x == 0:
        return False
    n = log2(x)
    if pow(2, int(n)) == x:
        return True
    return False
