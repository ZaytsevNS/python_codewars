from math import gcd


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def smallest(n: int) -> int:
    smallest_num = 1
    for i in range (1, n + 1):
        smallest_num = lcm(smallest_num, i)
    return smallest_num