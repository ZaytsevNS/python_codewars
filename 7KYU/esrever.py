def esrever(s: str) -> str:
    if len(s) < 2:
        return s
    return s[:-1][::-1] + s[-1]
    