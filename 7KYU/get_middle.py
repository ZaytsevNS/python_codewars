def get_middle(s: str) -> str:
    if len(s) < 3:
        return s
    for i, k in enumerate(range(len(s)-1)):
        needed_idx = len(s) // 2
        if len(s) % 2 == 0:
            return s[needed_idx - 1] + s[needed_idx]
        else:
            return s[needed_idx]
            