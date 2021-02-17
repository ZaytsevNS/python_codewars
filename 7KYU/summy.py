def summy(string_of_ints: str) -> int:
    return sum([int(i) for i in string_of_ints.split(' ')])