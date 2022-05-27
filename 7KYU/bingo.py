# https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145/


def bingo(array: list) -> str: 
    return 'WIN' if {2,7,9,14,15}.issubset(set(array)) else 'LOSE'
