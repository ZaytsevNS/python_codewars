# https://www.codewars.com/kata/56e9ac87c3e7d512bc001363/

def ascii_encrypt(plaintext: str) -> str:
    plaintext_encrypt: str = ''.join(chr(ord(k)+i) for i, k in enumerate(plaintext))
    return plaintext_encrypt

def ascii_decrypt(plaintext: str) -> str:
    plaintext_decrypt: str = ''.join(chr(ord(k)-i) for i, k in enumerate(plaintext))
    return plaintext_decrypt