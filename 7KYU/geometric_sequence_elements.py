# Solution for task: https://www.codewars.com/kata/55caef80d691f65cb6000040/

def geometric_sequence_elements(a: int, r: int, n: int) -> str:
    """ This function print first 'n' elements of the sequence with the given constant 'r' and first element 'a'. """
    return ', '.join(map(str, [a * pow(r, i) for i in range(n)]))
