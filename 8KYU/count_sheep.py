# Solution for task: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/

def count_sheep(n: int) -> str:
    return ''.join(f'{i} sheep...' for i in range(1, n + 1))
