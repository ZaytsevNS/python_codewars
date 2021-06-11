def find_squares(n: int) -> str:
    k = (n - 1) // 2 # because n = 2k + 1
    return f'{(k + 1) ** 2}-{k ** 2}'
    