def has_unique_chars(string: str) -> bool:
    if len(string) == 1:
        return True
    unique = []
    for item in string:
        if item not in unique:
            unique.append(item)
        else:
            return False
    return True