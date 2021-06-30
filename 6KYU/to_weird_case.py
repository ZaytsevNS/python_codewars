def swapcase_letter(string: str) -> str:
    return ''.join([l.lower() if i % 2 else l.upper() for i, l in enumerate(string)])

def to_weird_case(string: str) -> str:
    return ' '.join(swapcase_letter(word) for word in string.split())
