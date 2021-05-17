from math import gcd


def calculate_ratio(width: int, height: int) -> str:
    """
    To reduce a ratio, find the greatest common factor of both the number of width and the number of height. 
    Then divide the number of width and the number of height by the greatest common factor.
    """
    if width != 0 and height != 0:
        greatest_common_factor = gcd(width, height)
        return f'{width // greatest_common_factor}:{height // greatest_common_factor}'
    else:
        return 'You threw an error'
        