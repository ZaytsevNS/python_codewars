def multiple_of_index(arr: list) -> list:
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]