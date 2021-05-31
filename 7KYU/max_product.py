from functools import reduce
from operator import mul


def max_product(lst: list, n_largest_elements: int) -> int:
    largest_elements = sorted(lst)[-n_largest_elements:]        
    return reduce(mul, largest_elements)
    