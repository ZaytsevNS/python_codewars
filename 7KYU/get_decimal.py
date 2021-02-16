from math import modf


def get_decimal(n):
    fractional, whole = modf(n)
    return round(abs(fractional), 50)