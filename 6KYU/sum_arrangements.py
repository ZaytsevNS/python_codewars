from math import factorial


def sum_arrangements(n: int) -> int:
    """
    This function finds the sum of all numbers with the same digits (permutations) as the input number, including duplicates.
    """
    return sum([int(i) for i in str(n)]) * factorial(len(str(n))-1) * int(''.join(map(str, [1] * len(str(n)))))
    
#     list_of_int_permutations = []
#     for i in list(permutations([int(i) for i in str(n)])):
#         list_of_int_permutations.append(int(''.join(map(str, i))))
#     return sum(list_of_int_permutations)