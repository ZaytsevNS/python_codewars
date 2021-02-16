def is_digit(n) -> bool:
    if len(n) > 1:
        return False
    return n.isdigit()