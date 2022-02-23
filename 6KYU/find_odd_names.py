def is_odd(name: str) -> bool:
    return True if sum(ord(i) for i in name) % 2 else False

def find_odd_names(lst: list) -> list:
    return [i for i in lst if is_odd(i['firstName'])]
    