# https://www.codewars.com/kata/58daa7617332e59593000006/

def find_longest(arr: list) -> int:
    return sorted(arr, key=lambda x: len(str(x)), reverse=True)[0]