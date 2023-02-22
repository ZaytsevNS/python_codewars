# Solution for task: https://www.codewars.com/kata/562926c855ca9fdc4800005b/

def number_to_pwr(number: int, p: int) -> int: 
    result = 1
    for _ in range(1, p + 1):
        result *= number
    return result