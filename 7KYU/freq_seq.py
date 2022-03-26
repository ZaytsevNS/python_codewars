def freq_seq(s: str, sep: str) -> str:
    return sep.join(str(s.count(i)) for i in s)