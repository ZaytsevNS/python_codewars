# Solution for task: https://www.codewars.com/kata/56d19b2ac05aed1a20000430/

def between_extremes(numbers: list) -> int:
    """
    This function returns the difference between the largest and smallest values.
    """
    return max(numbers) - min(numbers)
