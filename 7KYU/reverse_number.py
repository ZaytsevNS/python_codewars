def reverse_number(n: int) -> int:
    """ This function takes in input 'n' and returns 'n' with all digits reversed. """
    if len(str(n)) == 1:
        return n
    k = abs(n)
    reversed_n = []
    while k != 0:
        i = k % 10
        reversed_n.append(i)
        k = (k - i) // 10
    return int(''.join(map(str, reversed_n))) if n > 0 else -int(''.join(map(str, reversed_n)))
    