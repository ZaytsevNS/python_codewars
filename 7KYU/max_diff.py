def max_diff(lst: list) -> int:
    """ Function returns the difference between the largest and the smallest value. """
    return max(lst) - min(lst) if lst else 0
