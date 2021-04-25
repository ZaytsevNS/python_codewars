def gordon(a: str) -> str:
    list_of_vowel: list = ['a', 'e', 'i', 'o', 'u']
    str_of_word_with_replace_symbols: str = ''
    for i in a:
        if i.lower() in list_of_vowel and i.lower() == 'a':
            str_of_word_with_replace_symbols += '@'
        elif i.lower() in list_of_vowel:
            str_of_word_with_replace_symbols += '*'
        else:
            str_of_word_with_replace_symbols += i.upper()
    return str_of_word_with_replace_symbols.replace(' ', '!!!! ') + '!!!!'
    