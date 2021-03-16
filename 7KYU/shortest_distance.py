from math import sqrt
from typing import Union

def shortest_distance(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    A = [sqrt(pow(a, 2) + pow((b + c), 2))]
    B = [sqrt(pow(b, 2) + pow((a + c), 2))]
    C = [sqrt(pow(c, 2) + pow((a + b), 2))]
    return min(list(A + B + C))