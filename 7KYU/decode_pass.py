def decode_pass(pass_list: list, bits: str):
    bits_to_str: str = ''.join(chr(int(i, 2)) for i in bits.split())
    return bits_to_str if bits_to_str in pass_list else False
    