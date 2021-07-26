from string import ascii_uppercase


def battle(x: str, y: str) -> str:
    dict_eng_letter: dict = {k:v for k, v in enumerate(ascii_uppercase, start=1)}
    count1: int = sum([key for _ in x for key, value in dict_eng_letter.items() if _ == value])
    count2: int = sum([key for _ in y for key, value in dict_eng_letter.items() if _ == value])
    return x if count1 > count2 else y if count1 < count2 else "Tie!"
