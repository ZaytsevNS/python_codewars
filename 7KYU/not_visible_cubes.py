def not_visible_cubes(n: int) -> int:
    if n < 3:
        return 0
    return (n - 2) ** 3
    