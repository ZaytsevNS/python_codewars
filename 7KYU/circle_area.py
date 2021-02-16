from math import pi

def circle_area(r):
    try:
        if r < 0:
            return False
        return round(pi * pow(r, 2), 2)
    except TypeError:
        return False