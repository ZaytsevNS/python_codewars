def even_and_odd(n: int) -> tuple:
    """ This function return two numbers NE and NO such as NE is formed by even digits of N 
    and NO is formed by odd digits of N """
    NE = ''.join(i for i in str(n) if not int(i) % 2)
    NO = ''.join(i for i in str(n) if int(i) % 2)
    if not NE:
        return (0, int(NO))
    if not NO:
        return (int(NE), 0)
    return (int(NE), int(NO))
