# https://www.codewars.com/kata/577b9960df78c19bca00007e/

def find_digit(num: int, nth: int) -> int:
    if nth <= 0:
        return -1
    else:
        num: str = str(abs(num)).zfill(nth)[::-1]
        return [int(k) for i, k in enumerate(num, 1) if i == nth][0]