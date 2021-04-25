def filter_long_words(sentence: str, n: int) -> list:
    return [i for i in sentence.split() if len(i) > n]
