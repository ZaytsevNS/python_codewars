# Solution for task: https://www.codewars.com/kata/56b0bc0826814364a800005a/

def cyclops(n: int) -> bool:
    """ A cyclops number is a number in binary that is made up of all 1's, with one 0 in the exact middle. """
    split_bin: list = bin(n)[2:].split('0')
    return len(split_bin[0]) == len(split_bin[1]) if len(split_bin) == 2 else False
    