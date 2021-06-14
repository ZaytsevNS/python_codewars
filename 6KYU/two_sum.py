from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)) :
        for j in range(i + 1, len(numbers)):
            if numbers[j] + numbers[i] == target :
                return [i, j]

# from typing import List
# from itertools import combinations


# def two_sum(numbers: List[int], target: int) -> List[int]:
#     list_of_combinations = list(combinations(numbers, 2))
#     for el in list_of_combinations:
#         if sum(el) == target:
#             first_el, second_el = numbers.index(el[0]), numbers.index(el[1])
#             if first_el == second_el:
#                 return [i for i, x in enumerate(numbers) if x == el[0]]
#             else:
#                 return [numbers.index(el[0]), numbers.index(el[1])]
    