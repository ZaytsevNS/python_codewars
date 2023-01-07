# Solution for task: https://www.codewars.com/kata/5d41e16d8bad42002208fe1a/

def more_zeros(s: str) -> list:
    bin_value: list = []
    for i in s:
        binary_ord = bin(ord(i))[2:]
        if binary_ord not in bin_value and binary_ord.count('0') > binary_ord.count('1'):
            bin_value.append(binary_ord)
    return [chr(int(i, 2)) for i in bin_value]
