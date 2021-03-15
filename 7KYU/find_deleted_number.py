def find_deleted_number(arr: list, mixed_arr: list) -> int:
    if arr == sorted(mixed_arr):
        return 0
    return int(''.join(map(str, (set(arr) - set(mixed_arr)))))