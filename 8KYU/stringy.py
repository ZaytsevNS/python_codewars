def stringy(size: int) -> str:
    if size % 2 == 0:
        return '10' * (size // 2)
    return '10' * (size // 2) + '1'