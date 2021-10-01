from collections import Counter


def majority(arr: list):
    if arr:
        count: dict = Counter(arr)
        max_values: int = max(count.values())
        key_for_max_values: list = [k for k, v in count.items() if v == max_values]
        return key_for_max_values[0] if len(key_for_max_values) == 1 else None
    return None
    