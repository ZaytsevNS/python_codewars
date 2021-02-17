def even_chars(st: str) -> list:
    """ This function returns a sequence (index begins with 1) of all the even characters from a string. """
    if len(st) < 2 or len(st) > 100:
        return 'invalid string'
    even = []
    for i, k in enumerate(range(len(st))):
        if i % 2 != 0:
            even.append(st[i])
    return even