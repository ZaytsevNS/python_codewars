# Solution for task: https://www.codewars.com/kata/58acfe4ae0201e1708000075/

def invite_more_women(arr: list) -> bool:
    return arr.count(-1) < arr.count(1)
