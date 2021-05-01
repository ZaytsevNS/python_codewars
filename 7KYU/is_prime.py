def is_prime(n: int) -> bool:
    '''
    This function returns True if n is a prime number otherwise return False.
    '''
    if n <= 1:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
