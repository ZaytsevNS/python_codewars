from numpy import average


def get_average(lst: list) -> int:
    return round(average([i['age'] for i in lst]))