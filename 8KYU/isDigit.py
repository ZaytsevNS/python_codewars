def isDigit(s: str) -> bool:
    return s.lstrip('-').replace('.', '', 1).isdigit()
    