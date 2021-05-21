import string


def alphabet_position(s: str) -> str:
    """
    This function return string with replace every letter with its position in the alphabet.
    """
    dict_of_letters: dict = {letter: str(idx) for idx, letter in enumerate(string.ascii_lowercase, start=1)}
    return ' '.join([dict_of_letters[i] for i in s.lower() if i in dict_of_letters])
    