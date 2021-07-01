def duplicate_encode(s: str) -> str:
    return f'{"".join("(" if s.lower().count(i.lower()) == 1 else ")" for i in s)}'
    