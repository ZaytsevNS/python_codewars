def ensure_question(s: str) -> str:
    return s if s.endswith('?') else s + '?'