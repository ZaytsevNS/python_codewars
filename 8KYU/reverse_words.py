def reverse_words(s: str) -> str:
    words_from_s = []
    for i in s.split(' '):
        words_from_s.append(i)
    return ' '.join(reversed(words_from_s))