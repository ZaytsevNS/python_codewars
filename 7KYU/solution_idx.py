def solution(items: list, index: int, default_value: str):
    try:
        return items[index]
    except IndexError:
        return default_value
