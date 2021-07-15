def round_color(color: int) -> int:
    """ Rounded to the closest valid value. """
    if color > 255:
        return 255
    elif color < 0:
        return 0
    return color

def rgb(r: int, g: int, b: int) -> str:
    """ RGB in a hexadecimal representation. """
    try:
        r, g, b = round_color(r), round_color(g), round_color(b)
        return f'{r:02x}{g:02x}{b:02x}'.upper()
    except:
        return 'error'