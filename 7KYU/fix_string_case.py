def solve(s: str) -> str:
    count_lower: int = 0
    count_upper: int = 0
    for i in s:
        if i.islower():
            count_lower += 1
        else:
            count_upper += 1
    if count_lower >= count_upper:
        return s.lower()
    return s.upper()
