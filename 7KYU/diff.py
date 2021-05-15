# return a sorted set with the difference
def diff(a: list, b: list) -> list:
    if a is b:
        return []
    return sorted(list(set(a) ^ set(b)))
    