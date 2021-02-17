# from math import factorial as fact

def factorial(n: int) -> int:
    # Using recursion
    if 0 <= n <= 1:
        return 1
    elif n < 0:
        return None
    return n * factorial(n - 1)
#     Using math-library
#     return fact(n) if n > 0 else None