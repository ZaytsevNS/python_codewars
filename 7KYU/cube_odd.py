from typing import Optional


def cube_odd(arr: list) -> Optional[int]:
    try:
        if all(type(i) == int for i in arr):
            return(sum([i ** 3 for i in arr if i % 2]))
    except TypeError:
        return None
