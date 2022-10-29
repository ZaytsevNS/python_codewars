# Solution for task: https://www.codewars.com/kata/5546180ca783b6d2d5000062/

def squares(x: int, n: int) -> list:
    """
    This function returns an array of length n, 
    starting with the given number x and the squares of the previous number.
    """
    squares: list = list()
    i: int = 1
    while i <= n:
        squares.append(x)
        x = x ** 2
        i += 1
    return squares if n > 0 else []
