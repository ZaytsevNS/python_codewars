def capitals(word: str) -> list:
    return [i for i, k in enumerate(word) if k.isupper()]
