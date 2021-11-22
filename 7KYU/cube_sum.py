def cube_sum(n: int, m: int) -> int:
    if n > m:
        n, m = m, n
    return sum(list(i ** 3 for i in range(n+1, m+1)))
