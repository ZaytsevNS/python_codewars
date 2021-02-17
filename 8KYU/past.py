def past(h: int, m: int, s: int) -> int:
    """ This function returns time converted to milliseconds. """
    return (h * 3600 + m * 60 + s) * 1000