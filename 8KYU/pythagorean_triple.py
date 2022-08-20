# Solution for task: https://www.codewars.com/kata/5951d30ce99cf2467e000013/


def pythagorean_triple(integers: list) -> bool:
    integers = sorted(integers)
    return pow(integers[0], 2) + pow(integers[1], 2) == pow(integers[2], 2)