from math import sqrt


def square_or_square_root(arr: list) -> list:
    result = []
    for i in arr:
        if int(sqrt(i)) != i ** 0.5:
            result.append(i ** 2)
        else:
            result.append(int(sqrt(i)))
    return result
    