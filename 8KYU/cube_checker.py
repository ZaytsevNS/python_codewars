# Solution for task: https://www.codewars.com/kata/58d248c7012397a81800005c/

def cube_checker(volume: int, side: int) -> bool:
    return pow(side, 3) == volume if volume > 0 and side > 0 else False