import re


def sp_eng(sentence: str) -> bool:
    result = re.search(r'english', sentence, re.IGNORECASE)
    return True if result else False
