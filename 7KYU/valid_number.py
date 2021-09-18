import re


def valid_number(n: str) -> bool:
    result = re.match(r'^(\+|\-)?(\d+)?\.(\d\d)$', n)
    return True if result else False
