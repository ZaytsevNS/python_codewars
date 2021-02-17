def find_longest(string: str) -> int:
    return max([len(i) for i in string.split()])