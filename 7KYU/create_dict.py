# Solution for task: https://www.codewars.com/kata/5533c2a50c4fea6832000101/

from itertools import zip_longest


def create_dict(keys: list, values: list) -> dict:
    """ This function makes dictionary from two lists """
    return dict(zip_longest(keys, values)) if len(keys) >= len(values) else dict(zip(keys, values))
