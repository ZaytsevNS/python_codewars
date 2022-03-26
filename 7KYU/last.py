def last(s: str) -> list:
    return sorted(list(s.split()), key=lambda i: i[-1])