def first(seq: list, n: int = 1) -> list: 
    if n == 0:
        return []
    return seq[:n]
