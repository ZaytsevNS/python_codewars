def spin_words(sentence: str) -> str:
    list_of_words = []
    for i in sentence.split():
        if len(i) >= 5:
            list_of_words.append(i[::-1])
        else:
            list_of_words.append(i)
    return ' '.join(list_of_words)
    