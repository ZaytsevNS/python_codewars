def hex_hash(code: str) -> int:
    my_string_with_hex_ord = ''
    list_of_num = []
    for letter in code:
        my_string_with_hex_ord += hex(ord(letter))[2:]
    for symbol in my_string_with_hex_ord:
        if symbol.isdigit():
            list_of_num.append(int(symbol))
    return sum(list_of_num)