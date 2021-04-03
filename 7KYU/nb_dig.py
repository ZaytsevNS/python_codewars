def nb_dig(n: int, d: int) -> int:
    square = [i ** 2 for i in range(n + 1)]
    count_digit = ' '.join(map(str, square)).count(str(d))
    return count_digit