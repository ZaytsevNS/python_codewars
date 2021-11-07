from string import ascii_lowercase


def solve(st: str) -> bool:
    return ''.join(sorted(st)) in ascii_lowercase
