def remove(s: str) -> str:
    return ' '.join([i for i in s.split() if i.count('!') != 1])
