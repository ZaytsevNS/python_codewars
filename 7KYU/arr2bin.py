# Solution for task: https://www.codewars.com/kata/559576d984d6962f8c00003c/

def arr2bin(arr: list) -> str or bool:
    if not arr:
        return '0'
    if any(type(i) != int for i in arr):
        return False
    else:
        return bin(sum(arr))[2:]
