def ones_counter(inp: list) -> list:
    if inp:
        if all(i == 1 for i in inp):
            return [len(inp)]
        if all(i == 0 for i in inp):
            return []
        return [len(i) for i in ''.join(map(str, inp)).split('0') if len(i) > 0]
    return []
