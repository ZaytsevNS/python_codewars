# Solution for task: https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/

def sum_no_duplicates(l: list) -> int:
    return sum(i for i in l if l.count(i) == 1)
