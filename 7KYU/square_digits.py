def square_digits(num: int) -> int:
    return int(''.join(map(str, [int(i) ** 2 for i in str(num)])))