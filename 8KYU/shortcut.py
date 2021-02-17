def shortcut(s: str) -> str:
    """ This function removes all the lowercase vowels in a given string. """
    vowel = ['a', 'e', 'i', 'o', 'u']
    str_without_vowel = ''
    for letter in s:
        if letter not in vowel:
            str_without_vowel += letter
    return str_without_vowel