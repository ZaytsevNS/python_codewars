def collision(x1, y1, radius1, x2, y2, radius2) -> bool: 
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) <= (radius1 + radius2) ** 2:
        return True
    return False
    