from math import sqrt


def is_simple(n: int) -> bool:
    if n % 2 == 0 and n != 2:
        return False
    for i in range (3, int(sqrt(n)) + 2, 2):
        if n % i == 0 and n != i:
            return False
    return True

def next_prime(n: int) -> int:
    n += 1
    if n <= 2:
        return 2
    else:
        if n % 2 == 0:
            n += 1
        while not is_simple(n):
            n += 2
        return n