def is_vowel(s: str) -> bool:
    if len(s) == 0 or len(s) > 1:
        return False
    vowel = ["a", "e", "i", "o", "u"]
    for item in s:
        if item.lower() in vowel:
            return True
        return False