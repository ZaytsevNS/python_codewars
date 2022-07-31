# Solution for task: https://www.codewars.com/kata/56d6b7e43e8186c228000637/


def colour_association(arr: list) -> list:
    return [{i[0]: i[1]} for i in arr]
