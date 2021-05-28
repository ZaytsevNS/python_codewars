# write the function is_anagram
def is_anagram(test: str, original: str) -> bool:
    letters_from_test: list = sorted([i.lower() for i in test])
    letters_from_original: list = sorted([i.lower() for i in original])
    return letters_from_test == letters_from_original