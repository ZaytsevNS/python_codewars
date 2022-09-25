# Solution for task: https://www.codewars.com/kata/58845748bd5733f1b300001f/

def range_bit_count(a: int, b: int) -> int:
    return sum([sum(map(int, format(i, 'b'))) for i in range(a, b + 1)])
    