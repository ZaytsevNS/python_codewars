import re


def textin(s: str) -> str:
    return re.sub('two|too|to', '2', s, flags=re.IGNORECASE)