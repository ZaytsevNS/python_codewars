from numpy import prod


def smallest_product(a: list) -> int:
    return min([prod(i) for i in a])
