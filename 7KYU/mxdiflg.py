def mxdiflg(a1: list, a2: list) -> int:
    if not a1 or not a2:
        return -1
    return max(abs(len(min(a1, key=len)) - len(max(a2, key=len))), abs(len(max(a1, key=len))) - len(min(a2, key=len)))
    