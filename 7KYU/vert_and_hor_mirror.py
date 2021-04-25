def vert_mirror(s: str) -> str:
    return '\n'.join([''.join(list(reversed(i))) for i in s.split('\n')])


def hor_mirror(s: str) -> str:
    return '\n'.join(reversed([i for i in s.split('\n')]))


def oper(fct, s):
    return fct(s)
    