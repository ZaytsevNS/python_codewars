def type_of_triangle(a, b, c) -> str: 
    try:
        if (type(a) == type(b) == type(c) == int) and (c < (a + b) and b < (a + c) and a < (b + c)):
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Not a valid triangle"
    except TypeError:
        return "Not a valid triangle"
    