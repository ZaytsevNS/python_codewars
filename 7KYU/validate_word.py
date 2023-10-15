from collections import Counter


def validate_word(s: str) -> bool:
    count = Counter(s.lower())
    return True if len(set(count.values())) < 2 else False
