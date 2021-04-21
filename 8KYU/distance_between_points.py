from math import sqrt


def distance_between_points(a, b):    
    return round(sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2), 6)
