def invert(a:list):
    if len(a) is None:
        return []
    my_invert = []
    for item in a:
        if item > 0:
            item *= -1
            my_invert.append(item)
        else:
            item *= -1
            my_invert.append(item)
    return my_invert