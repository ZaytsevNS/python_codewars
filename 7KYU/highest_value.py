def highest_value(a: str, b: str) -> str:
    return a if sum(ord(i) for i in a) >= sum(ord(i) for i in b) else b
    