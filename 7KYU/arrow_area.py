# Solution for task: https://www.codewars.com/kata/589478160c0f8a40870000bc/

from math import sqrt


def arrow_area(a: int, b: int):
    triangle_side = sqrt(pow(a, 2) + pow(b, 2)) / 2
    return round(b / 4 * sqrt(4 * pow(triangle_side, 2) - pow(b, 2)), 2)
