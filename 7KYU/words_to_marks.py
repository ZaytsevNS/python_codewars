from string import ascii_lowercase


def words_to_marks(s: str) -> int:
    letter: dict = {v:k for k, v in enumerate(ascii_lowercase, 1)}
    return sum(letter.get(i) for i in s)
    