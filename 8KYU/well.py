def well(x: list) -> str:
    good = x.count('good')
    if 1 <= good <= 2:
        return 'Publish!'
    elif good > 2:
        return 'I smell a series!'
    return 'Fail!'