# Solution for task: https://www.codewars.com/kata/563b1f55a5f2079dc100008a/

def get_larger_numbers(a: list, b: list) -> list:
    return [max(i, j) for i, j in zip(a, b)]
