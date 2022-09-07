# Solution for task: https://www.codewars.com/kata/59a1cdde9f922b83ee00003b/


def stanton_measure(arr: list) -> int:
    return sum(1 for i in arr if i == arr.count(1))
    