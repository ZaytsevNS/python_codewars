from math import sqrt


def heron(a, b, c):
    s = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)