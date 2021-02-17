def is_triangle(a:float, b:float, c:float):   
    if (a < c + b) and (b < a + c) and (c < a + b): #длина каждого отрезка меньше суммы длин двух остальных отрезков
        return True
    else:
        return False