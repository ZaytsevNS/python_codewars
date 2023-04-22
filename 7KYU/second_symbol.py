# Solution for task: https://www.codewars.com/kata/63f96036b15a210058300ca9/

def second_symbol(s: str, symbol: str) -> int:
    
    idx = list()
    
    for i, k in enumerate(s):
        if k == symbol and len(idx) != 2:
            idx.append(i)
    if len(idx) == 2:
        return idx[-1]
    else:
        return -1
