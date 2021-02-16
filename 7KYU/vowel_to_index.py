def vowel_2_index(s: str) -> str:
    vowel = ['a', 'e', 'i', 'o', 'u']
    my_string = ''
    for i, k in enumerate(s, start = 1):
        if k.lower() not in vowel:
            my_string += k
        elif k.lower() in vowel:
            my_string += str(i)
    return my_string