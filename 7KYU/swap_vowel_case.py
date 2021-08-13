def swap_vowel_case(st: str) -> str: 
    return ''.join(i.swapcase() if i in 'aeouiAEOUI' else i for i in st)
