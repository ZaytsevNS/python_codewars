def vaporcode(s: str) -> str:
    """ This function converts any sentence into a V A P O R W A V E sentence """
    return '  '.join(i.upper() for i in s if i != ' ')
