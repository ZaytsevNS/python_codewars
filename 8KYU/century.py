def century(year: int) -> int:
    """This function returns the century by year."""
    if year % 100 == 0:
        year //= 100
        return year
    else:
        year //= 100
        return year + 1