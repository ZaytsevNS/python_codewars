def add_length(s: str) -> list:
    words_with_len = []
    for i in s.split():
        words_with_len.append(i + ' ' + str(len(i)))
    return words_with_len