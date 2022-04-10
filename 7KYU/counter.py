# https://www.codewars.com/kata/60edafd71dad1800563cf933/

def counter():
    count: int = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc