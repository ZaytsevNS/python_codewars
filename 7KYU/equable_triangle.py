def equable_triangle(a: int, b: int, c: int) -> bool:
    perimeter = a + b + c
    semi_perimeter = perimeter // 2
    area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
    return True if perimeter == area else False
