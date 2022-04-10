# https://www.codewars.com/kata/55da6c52a94744b379000036/

from re import findall


def sum_from_string(strng: str) -> int:
    return sum(map(int, findall(r'[0-9]+', strng)))