def wrap(height, width, length):
    min_val = min(height, width, length)
    if min_val == height:
        return (height * 4 + length * 2 + width * 2) + 20
    elif min_val == width:
        return (width * 4 + height * 2 + length * 2) + 20
    return (length * 4 + height * 2 + width * 2) + 20
    