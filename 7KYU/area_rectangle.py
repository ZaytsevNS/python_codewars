from typing import Union


def area(diagonal: int, side_a: int) -> Union[int, float]:
    if diagonal <= side_a:
        return "Not a rectangle"
    side_b = (diagonal ** 2 - side_a ** 2) ** 0.5
    area_rectangle = side_a * side_b
    return round(area_rectangle, 2)
