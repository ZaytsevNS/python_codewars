# https://www.codewars.com/kata/55c5b03f8c28da9a51000045/

def find_sum(*args) -> int:
    return sum(args) if all(i>=0 for i in args) else -1