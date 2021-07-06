def flatten(*args):
    to_flatten = lambda *n: (e for a in n for e in (to_flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    return list(to_flatten(*args))
    