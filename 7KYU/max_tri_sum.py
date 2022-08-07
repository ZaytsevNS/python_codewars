# Solution for task: https://www.codewars.com/kata/5aa1bcda373c2eb596000112/


def max_tri_sum(numbers: list) -> int:
    return sum(sorted(set(numbers), reverse=True)[:3])
