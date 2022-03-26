def make_password(phrase: str) -> str:
    return ''.join(i[0] for i in phrase.split()).translate(str.maketrans({'O': '0', 'o': '0', 'I': '1', 'i': '1', 'S': '5', 's': '5'}))