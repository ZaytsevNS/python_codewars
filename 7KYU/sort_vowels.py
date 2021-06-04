def sort_vowels(s: str) -> str:
    if type(s) != str:
        return ''
    VOWEL = 'AaEeIiOoUu'
    BACKSLASH = '\n'
    str_in_special_format = ''
    for i in s:
        if i in VOWEL:
            str_in_special_format += f'{"|" + i + BACKSLASH}'
        else:
            str_in_special_format += f'{i + "|" + BACKSLASH}'
    return str_in_special_format[:-1]
    