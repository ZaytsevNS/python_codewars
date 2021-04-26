# from math import factorial as fact


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)
#     return fact(n)