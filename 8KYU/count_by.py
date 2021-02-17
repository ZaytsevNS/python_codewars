def count_by(x: int, n: int) -> list:
    """ This function returns a sequence of numbers counting by `x` `n` times. """
    # first way
    seq = []
    for i in range(1, n + 1):
        seq.append(i * x)
    return seq
    # second way
    # return [i * x for i in range(1, n+1)]