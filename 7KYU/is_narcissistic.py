# https://www.codewars.com/kata/56b22765e1007b79f2000079/


def is_narcissistic(n: int) -> bool:
    """ A Narcissistic Number is a number of length s in which the sum of its digits
    to the power of s is equal to the original number """
    return sum([pow(int(i), len(str(n))) for i in str(n)]) == n