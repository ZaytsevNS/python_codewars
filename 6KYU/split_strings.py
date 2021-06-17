def solution(s: str) -> list:
    if len(s) % 2:
        s += "_"
    every_two_characters: list = []
    while s:
        every_two_characters.append(s[:2])
        s = s[2:]
    return every_two_characters
    