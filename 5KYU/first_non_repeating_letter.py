def first_non_repeating_letter(s: str) -> str:
    if s:
        non_repeating = [i for i in s if s.lower().count(i.lower()) == 1]
        return non_repeating[0] if len(non_repeating) >= 1 else ''
    return ''
