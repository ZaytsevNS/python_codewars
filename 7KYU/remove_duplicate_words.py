def remove_duplicate_words(s: str) -> str:
    return ' '.join(dict.fromkeys([i for i in s.split()]))
    