def swap(st: str) -> str:
    return st.translate(str.maketrans('aeiou', 'AEIOU'))