def is_pangram(s: str) -> bool:
    letter_from_s: dict = {}
    for i in s.lower():
        if i not in letter_from_s:
            if i.isalpha():
                letter_from_s[i] = 1
        else:
            letter_from_s[i] += 1
    return len(letter_from_s) == 26
    