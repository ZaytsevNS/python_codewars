def grow(arr: list) -> int:
    """This function returns the result of multiplying the values."""
    if len(arr) is None:
        return 0
    res = 1
    for item in arr:
        res *= item
    return res