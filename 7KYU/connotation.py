from string import ascii_lowercase


def connotation(strng: str) -> bool:
    FIRST_HALF = len([i for i in strng.split() if i[0].lower() in ascii_lowercase[:13]])
    SECOND_HALF = len([i for i in strng.split() if i[0].lower() in ascii_lowercase[13:]])
    return True if FIRST_HALF >= SECOND_HALF else False
    