# Solution for task: https://www.codewars.com/kata/57d448c6ba30875437000138/

def roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0: return None
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    
    return round(x1 + x2, 2)
