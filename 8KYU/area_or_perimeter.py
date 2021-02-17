def area_or_perimeter(length: int, width: int) -> int:
    """ This function returns area for a square or perimeter for a rectangle. """
    if length == width:
        return length * width
    return (2 * length) + (2 * width)