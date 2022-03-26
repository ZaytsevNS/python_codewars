def nth_char(words: list) -> str:
    return ''.join(words[i][k] for i, k in enumerate(range(len(words))))