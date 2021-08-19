def split_in_parts(s: str, part_length: int) -> str: 
    words: list = []
    for i in range(0, len(s), part_length):
        words.append(s[i:i+part_length])
    return ' '.join(words)
    