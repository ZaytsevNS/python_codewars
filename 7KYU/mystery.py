def mystery(s: str, n: int) -> str:
    if n == 0:
        return ''
    return ''.join(i for i, k in zip(s, bin(n)[2:]) if k == '1')
    