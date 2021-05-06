def sum_triangular_numbers(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return n
    sum_numbers = 0
    for i in range(1, n + 2):
        sum_numbers += (i * (i - 1)) // 2
    return sum_numbers
