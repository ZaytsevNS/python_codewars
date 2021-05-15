from typing import Union


def multiply_and_filter(seq: list, multiplier: Union[int, float]) -> list: 
    return [i * multiplier for i in seq if type(i) == int or type(i) == float]
