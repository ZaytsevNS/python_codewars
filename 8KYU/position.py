from string import ascii_lowercase

def position(alphabet: str):
    dict_letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
    if alphabet in dict_letters:
        return f'Position of alphabet: {dict_letters[alphabet]}'