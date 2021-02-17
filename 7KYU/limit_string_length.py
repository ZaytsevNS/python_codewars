def solution(st: str, limit: int) -> str:
    if len(st) <= limit:
        return st
    for i in range(len(st)):
        return st[i:limit]+'...'