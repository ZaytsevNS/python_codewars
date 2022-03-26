def comes_after(st: str, l: str) -> str:
    s: str = ''
    for i in range(len(st)-1):
        if st[i].lower() == l.lower() and st[i+1].isalpha():
            s += st[i+1]
    return s