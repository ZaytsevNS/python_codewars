from numpy import average


def better_than_average(class_points: list, your_points: int) -> bool:
    return your_points > average(class_points)