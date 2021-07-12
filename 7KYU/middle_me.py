def middle_me(N: int, X: str, Y: str) -> str:
    """ This function takes a key of X and place it in the middle of Y repeated N times. """
    string = N * Y
    if len(string) % 2:
        return X
    else:
        id_x = len(string) // 2
        return f'{string[:id_x]}{X}{string[id_x:]}'