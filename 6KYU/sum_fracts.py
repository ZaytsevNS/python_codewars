from math import gcd
import numpy as np


def sum_fracts(arr: list):
    if len(arr) == 0:
        return None
    denominator = [i[1] for i in arr]
    LCM = np.lcm.reduce(denominator)
    numerator = sum([LCM // i[1] * i[0] for i in arr])
    com_div = gcd(numerator, LCM)
    if com_div != 1:
        n = numerator / LCM
        if n == int(n):
            return int(n)
        return [numerator // com_div, LCM // com_div]
    return [numerator, LCM]
    