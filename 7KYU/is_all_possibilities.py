def is_all_possibilities(arr: list) -> bool:
    if arr:
        return sorted(arr) == [i for i in range(0, len(arr))]
    return False