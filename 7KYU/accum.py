def accum(s: str) -> str:
    list_letter: list = []
    for i, k in enumerate(range(len(s)), start=1):
        list_letter.append(s[i-1]*i)
    my_str = ' '.join(list_letter)
    return '-'.join(w.capitalize() for w in my_str.split())
