from string import ascii_lowercase


def get_sum_value_letter(word: str) -> int:
    eng_lowercase: dict = {v:k for k, v in enumerate(ascii_lowercase, start=1)}
    return sum(eng_lowercase[letter] for letter in word)


def high(string: str) -> str:
    """ This function returns highest scoring word. """
    return max(string.split(), key=get_sum_value_letter)
