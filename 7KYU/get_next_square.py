def is_perfect_square(n: int) -> bool:
    if n ** 0.5 != int(n ** 0.5):
        return False
    return True


def find_next_square(n: int) -> int:
    if is_perfect_square(n) is False:
        return -1
    n += 1
    while not is_perfect_square(n):
        n += 1
    return n
    