from math import sqrt


def is_square(arr: list):
    if arr:
        return all(sqrt(i) == int(i ** 0.5) for i in arr)
    return None
    