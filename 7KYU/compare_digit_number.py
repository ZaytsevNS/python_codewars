# Solution for task: https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de/

def compare(a: int, b: int) -> str:
    len_intersection: int = len(set(str(a)) & set(str(b)))
    if (len_intersection == 2) or (a == b):
        return '100%'
    elif len_intersection == 1:
        return '50%'
    else:
        return '0%'