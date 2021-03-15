def merge_arrays(arr1: list, arr2: list) -> list:
    return sorted(list(set(arr1) | set(arr2)))