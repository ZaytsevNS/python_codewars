from string import ascii_lowercase


def alphanumeric(password: str) -> bool:
    if not password:
        return False
    for i in password:
        if (i.lower() in ascii_lowercase) or (i in '0123456789'):
            continue
        else:
            return False
    return True
