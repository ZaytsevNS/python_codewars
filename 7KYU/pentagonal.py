# Solution for task: https://www.codewars.com/kata/5fb856190d5230001d48d721/

def pentagonal(n: int) -> int:
    return (5 * n * (n - 1) + 2) // 2 if n > 0 else -1
