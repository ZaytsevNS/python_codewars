def divisible_by(numbers: list, divisor: int) -> list:
    """This function returns all numbers which are divisible by the given divisor."""
    if numbers is None:
        return []
    res = []
    for item in numbers:
        if item % divisor == 0:
            res.append(item)
    return res