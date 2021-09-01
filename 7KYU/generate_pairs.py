from itertools import combinations_with_replacement


def generate_pairs(n: int) -> list:
    return [list(i) for i in combinations_with_replacement(range(n+1), 2)]
