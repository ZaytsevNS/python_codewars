import re


def solve(s: str) -> str:
    return ''.join(reversed([i[::-1] if not i.isdigit() else i for i in re.split('(\d+)', s)]))