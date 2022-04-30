# https://www.codewars.com/kata/597bb84522bc93b71e00007e/


def string_merge(string1: str, string2: str, letter: str) -> str:
    first_index: int = string1.index(letter)
    second_index: int = string2.index(letter)
    return string1[:first_index]+string2[second_index:]