def compare(s1: str, s2: str) -> bool:
    def get_sum(s):
        return sum(ord(c) for c in s.upper()) if s and s.isalpha() else None
    return get_sum(s1) == get_sum(s2)