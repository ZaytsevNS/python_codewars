# Solution for task: https://www.codewars.com/kata/5f9f43328a6bff002fa29eb8/

def approx_equals(a: float, b: float) -> bool:
    diff: float = 0.001
    return abs(a - b) < diff
