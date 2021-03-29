from math import sqrt


def is_simple(n: int) -> bool:
    if n % 2 == 0 and n != 2:
        return False
    for i in range (3, int(sqrt(n)) + 2, 2):
        if n % i == 0 and n != i:
            return False
    return True

def divisors(n: int) -> int:
    if n == 1:
        return 1
    elif is_simple(n):
        return 2
    return len([x for x in range(1, n + 1) if n % x == 0])
    