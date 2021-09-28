def compress(sentence: str) -> str:
    word: list = []
    for i in sentence.lower().split():
        if i not in word:
            word.append(i)
    return ''.join([str(word.index(i)) for i in sentence.lower().split()])
    