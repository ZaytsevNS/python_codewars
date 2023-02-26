# Solution for task: https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/

def capitalize(s: str, ind: list) -> str:
    return ''.join(k.upper() if i in ind else k for i, k in enumerate(s))
