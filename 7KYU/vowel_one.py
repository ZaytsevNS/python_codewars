# Solution for task: https://www.codewars.com/kata/580751a40b5a777a200000a1/

def vowel_one(s: str) -> str:
    return ''.join(['1' if i in 'aeiou' else '0' for i in s.lower()])
