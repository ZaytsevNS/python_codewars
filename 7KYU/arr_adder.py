# Solution for task: https://www.codewars.com/kata/59778cb1b061e877c50000cc/

def arr_adder(arr: list) -> str:
    return ' '.join(''.join(i) for i in zip(*arr))
