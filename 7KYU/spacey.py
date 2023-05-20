# Solution for task: https://www.codewars.com/kata/56576f82ab83ee8268000059/

def spacey(array: list) -> list:
    return list(''.join(array[:i + 1]) for i in range(len(array)))
