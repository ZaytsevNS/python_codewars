# Solution for task: https://www.codewars.com/kata/563fb342f47611dae800003c/

def trim(phrase: str, size: int) -> str:
    len_phrase: int = len(phrase)
    if size >= len_phrase:
        return phrase
    elif size < 3:
        return f'{phrase[:size]}...'
    else:
        return f'{phrase[:size-3]}...'
