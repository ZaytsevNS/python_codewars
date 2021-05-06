def move_vowels(string: str) -> str:
    if len(string) <= 1:
        return string
    vowels_from_string = ''
    consonants_from_string = ''
    for i in string:
        if i in 'aeiou':
            vowels_from_string += i
        else: consonants_from_string += i
    return f'{consonants_from_string}{vowels_from_string}'