# Solution for task: https://www.codewars.com/kata/592915cc1fad49252f000006/

def no_ifs_no_buts(a: int, b: int) -> str:
    """
    Function accepts two numbers a and b and returns whether a is smaller than, bigger than, or equal to b, as a string.
    """
    
    possible_options: dict = {a == b: f'{a} is equal to {b}',
                              a > b: f'{a} is greater than {b}',
                              a < b: f'{a} is smaller than {b}',
                             }
    
    return possible_options[True]
    