# Solution for task: https://www.codewars.com/kata/5519e930cd82ff8a9a000216/

def hamming_weight(x: int) -> int:
    return x.bit_count()
