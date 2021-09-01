from itertools import combinations_with_replacement


def generate_pairs(m: int, n: int) -> list:
#     First way
#     pairs: list = []
#     for i in range(m, n+1):
#         for j in range(i, n+1):
#             pairs.append((i,j))
#     return pairs
#
#     Second way
    return [i for i in combinations_with_replacement(range(m, n+1), 2)]
