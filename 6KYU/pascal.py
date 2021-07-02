from math import factorial


def pascal(n: int) -> list:
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i)//(factorial(j)*factorial(i - j)))
        triangle.append(row)
    return triangle
    