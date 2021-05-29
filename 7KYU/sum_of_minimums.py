def sum_of_minimums(numbers: list) -> int:
    """
    This function returns the sum of minimum value in each row.
    """
    return sum([min(i) for i in numbers])
    