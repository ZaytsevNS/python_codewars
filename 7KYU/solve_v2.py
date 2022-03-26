def solve(s: str) -> int:
    new_s: str = ''
    for i in s:
        if i not in 'aeiou':
            new_s += f'-{i}-'
        else:
            new_s += i
    return len(max(new_s.split('-'), key=len))