def explode(s: str) -> str:
    return ''.join(int(i)*i for i in s)