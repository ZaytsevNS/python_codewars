def unique(integers: list) -> list:
    if len(integers) == 0:
        return []
    return list(dict.fromkeys(integers))
    