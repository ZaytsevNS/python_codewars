from math import pi


def square_area(A):
    radius = 2 * A / pi
    return round(radius ** 2, 2)