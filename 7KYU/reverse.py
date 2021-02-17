def reverse(n: int) -> int:
    """ This function takes in input 'n' and returns 'n' with all digits reversed. Assume positive 'n'. """
    reversed_n = []
    while n != 0:
        i = n % 10
        reversed_n.append(i)
        n = (n - i) // 10
    return int(''.join(map(str, reversed_n)))