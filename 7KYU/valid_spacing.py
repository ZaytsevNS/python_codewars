def valid_spacing(s: str) -> bool:
    if s != ' '.join([i for i in s.split()]):
        return False
    return True
