def digital_root(n: int) -> int:
    """ This function returns recursive sum of all the digits in a number. """
    if n < 10:
        return n
    return (digital_root(sum(map(int, str(n)))))