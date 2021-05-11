def longest(a1: str, a2: str) -> str:
    if a1 is a2:
        return ''.join(sorted(set(a1)))
    return ''.join(sorted(set(a1 + a2)))
    