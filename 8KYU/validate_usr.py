import re


def validate_usr(username: str) -> bool:
    try:
        return re.match(r'[a-z0-9_]{4,16}', username).group(0) == username
    except AttributeError:
        return False
