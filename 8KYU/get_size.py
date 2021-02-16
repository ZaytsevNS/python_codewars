def get_size(w: int, h: int, d: int) -> list:
    return [2 * (w * h + h * d + w * d), w * h * d]