import re


def sum_of_integers_in_string(s: str) -> int:
    """ This function calculates the sum of the integers inside a string """
    return sum([int(i) for i in re.findall(r'\d+', s)])