VOWEL: dict = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
def encode(st: str) -> str:
    encode_str: str = ''
    for i in st:
        if i in VOWEL.keys():
            encode_str += str(VOWEL[i])
        else:
            encode_str += i
    return encode_str
    
def decode(st: str) -> str:
    decode_str: str = ''
    for i in st:
        if i.isnumeric():
            if int(i) in VOWEL.values():
                decode_str += ''.join([k for k, v in VOWEL.items() if v == int(i)])
        else:
            decode_str += i
    return decode_str
