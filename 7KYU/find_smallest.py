def find_smallest(numbers: list, to_return: str) -> int:
    if to_return == "value":
        return min(numbers)
    return numbers.index(min(numbers))
    