def string_hash(s: str) -> int:
    ascii_values_from_s = [ord(i) for i in s]
    a, b = sum(ascii_values_from_s), sum([ascii_values_from_s[i + 1] - ascii_values_from_s[i] for i in range(len(ascii_values_from_s)-1)])
    c = (a | b) & (~a << 2) 
    d = c ^ (32 * (s.count(' ') + 1))
    return d
    