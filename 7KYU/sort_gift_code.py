def sort_gift_code(code: str) -> str:
    my_letter = []
    for letter in code:
        my_letter.append(letter)
    return ''.join(sorted(my_letter))