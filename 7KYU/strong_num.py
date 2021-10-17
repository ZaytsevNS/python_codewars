from math import factorial


def strong_num(number: int) -> str:
    if sum(factorial(int(i)) for i in str(number)) == number:
        return "STRONG!!!!"
    return "Not Strong !!"
