def vowel_change(txt: str, vow: str) -> str:
    return ''.join(i.replace(i, vow) if i in 'aeiou' else i for i in txt)
