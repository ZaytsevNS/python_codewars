def parse_float(string: str) -> float:
    if type(string) == list:
        return None
    try:
        return float(string)
    except ValueError:
        return None