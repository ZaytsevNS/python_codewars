# Solution for task: https://www.codewars.com/kata/5a023c426975981341000014/

from typing import Union


def other_angle(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return 180 - (a + b)
