def sum_digits(num: int) -> int:
    return sum([int(i) for i in str(abs(num))])
    