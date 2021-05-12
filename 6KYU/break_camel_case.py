def solution(s: str) -> str:
    if all(i.islower() for i in s):
        return s
    return ''.join(' ' + i if i.isupper() else i for i in s)
   