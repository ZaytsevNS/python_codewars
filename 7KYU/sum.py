def sum(*args):
    res = 0
    for x in args:
        if type(x) == int:
            res += x
    return res