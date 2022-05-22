# https://www.codewars.com/kata/590e03aef55cab099a0002e8/


def incrementer(nums: list) -> list:
    return [int(str(i+k)[-1]) for i, k in enumerate(nums, 1)]
