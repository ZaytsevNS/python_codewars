def cat_mouse(x: str) -> str:
    return 'Escaped!' if x.count('.') >= 4 else 'Caught!'
