from collections import Counter


def count_languages(lst: list) -> dict:
    return Counter([i['language'] for i in lst])
