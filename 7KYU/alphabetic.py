# Solution for task: https://www.codewars.com/kata/5a8059b1fd577709860000f6/


def alphabetic(s: str) -> bool:
    """ This function takes an input string of lowercase letters and returns true/false depending on whether the string is in alphabetical order or not. """
    return s == ''.join(sorted([i for i in s], key=str.lower))
