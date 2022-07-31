# Solution for task: https://www.codewars.com/kata/563d59dd8e47a5ed220000ba


def get_sum_of_digits(num: int) -> int:
    return sum([int(i) for i in str(num)])
