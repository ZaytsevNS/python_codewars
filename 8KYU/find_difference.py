from numpy import prod


def find_difference(a: list, b: list) -> int:
    return abs(prod(a) - prod(b))