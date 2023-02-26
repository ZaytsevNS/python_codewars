# Solution for task: https://www.codewars.com/kata/556025c8710009fc2d000011/

def gr33k_l33t(string: str) -> str:
    
    greek_letter: dict = {'a': 'α', 'b': 'β', 'd': 'δ', 'e': 'ε',
                          'i': 'ι', 'k': 'κ', 'n': 'η', 'o': 'θ',
                          'p': 'ρ', 'r': 'π', 't': 'τ', 'u': 'μ',
                          'v': 'υ', 'w': 'ω', 'x': 'χ', 'y': 'γ',
                         }
    
    return ''.join(greek_letter.get(i.lower(), i.lower()) for i in string)
