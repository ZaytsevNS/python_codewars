# Solution for task: https://www.codewars.com/kata/6523a71df7666800170a1954/

from numpy import base_repr


def esthetic(num: int) -> list:
    find_base: list = []
    for base in range(2, 11):
        convert_num: str = base_repr(num, base)
        pair: list = [i for i in zip(convert_num, convert_num[1::])]
        if all(i == 1 for i in [abs(int(i[0]) - int(i[1])) for i in pair]):
            find_base.append(base)
    return find_base
