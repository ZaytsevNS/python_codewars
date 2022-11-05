# Solution for task: https://www.codewars.com/kata/524f5125ad9c12894e00003f/

def remainder(a, b):
    """
    This function returns the remainder of dividing the larger value by the smaller value.
    """
    try:
        larger, smaller = max(a, b), min(a, b)
        return larger % smaller
    except ZeroDivisionError:
        return None
