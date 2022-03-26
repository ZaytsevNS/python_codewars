def remove(s: str) -> str:
    last_letter_idx: int = s.rindex([i for i in s if i.isalpha()][-1])
    count_mark: int = s[last_letter_idx+1:].count('!')
    return s.replace('!', '') + '!' * count_mark