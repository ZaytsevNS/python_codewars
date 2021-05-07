def get_real_floor(n: int) -> int:
    if n < 0:
        return n
    elif abs(n) < 2:
        return 0
    elif n > 13:
        return n - 2
    return n - 1
    