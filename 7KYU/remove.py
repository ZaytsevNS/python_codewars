def remove(s: str) -> str:
    new_s: str = ''
    for i in s.split():
        while i[-1] == '!':
            i = i[:-1]
            new_s += f'{i} '
    return new_s[:-1]
