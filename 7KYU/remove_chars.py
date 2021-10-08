from string import ascii_letters


def remove_chars(s: str) -> str:
    return ''.join([i for i in s if i in ascii_letters or i == ' '])