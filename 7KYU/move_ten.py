def move_ten(st: str) -> str:
    new_str: str = ''
    for i in range(len(st)):
        val = ord(st[i]) + 10
        if val > 122:
            new_str += chr(val - 26)
        else:
            new_str += chr(val)
    return new_str
    