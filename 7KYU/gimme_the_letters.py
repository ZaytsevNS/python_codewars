# Solution for task: https://www.codewars.com/kata/6512b3775bf8500baea77663/

from string import ascii_lowercase, ascii_uppercase


def gimme_the_letters(sp: str) -> str:
    first_letter, last_letter = sp.split('-')
    if first_letter.isupper():
        return ascii_uppercase[ascii_uppercase.index(first_letter):ascii_uppercase.index(last_letter) + 1]
    else:
        return ascii_lowercase[ascii_lowercase.index(first_letter):ascii_lowercase.index(last_letter) + 1]
    