def series_sum(n: int) -> str:
    """ 
    This function returns the sum of following series upto nth term(parameter).
    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...
    """
    s = 0
    for i in range(n):
        s += 1 / (1 + (i * 3))
    return "{:.2f}".format(s)