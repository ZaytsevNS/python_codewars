from math import factorial


def pascals_triangle(n: int) -> list:
    triangle = []
    for i in range(n):
        for j in range(i + 1):
            triangle.append(factorial(i)//(factorial(j)*factorial(i - j)))
    return triangle
    