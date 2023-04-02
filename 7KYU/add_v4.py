# Solution for task: https://www.codewars.com/kata/555de49a04b7d1c13c00000e/

def add(*args) -> int:
    return round(sum(k / i for i, k in enumerate(args, 1)))
