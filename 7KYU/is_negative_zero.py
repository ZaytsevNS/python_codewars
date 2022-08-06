# Solution for task: https://www.codewars.com/kata/5c5086287bc6600001c7589a/


from re import match


def is_negative_zero(n: float) -> bool:
    """ This function returns true if the input number is -0 and false otherwise. """
    return bool(match(r'-0.0', str(n)))
