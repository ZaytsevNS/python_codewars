def shorter_reverse_longer(a: str, b: str) -> str:
    if len(a) < len(b): 
        return f'{a}{b[::-1]}{a}'
    return f'{b}{a[::-1]}{b}'
    