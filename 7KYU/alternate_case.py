def alternate_case(s: str) -> str:
    alternate_s = ''
    for i in s:
        if i.islower():
            alternate_s += i.upper()
        else:
            alternate_s += i.lower()
    return alternate_s
    