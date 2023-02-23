# Solution for task: https://www.codewars.com/kata/570f6436b29c708a32000826

def first_non_repeated(s: str) -> str or None:
    try: return [i for i in s if s.count(i) == 1][0]
    except IndexError: return None
    