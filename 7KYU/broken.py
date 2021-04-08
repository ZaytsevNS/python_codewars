def broken(inp: str) -> str:
    my_str = ''
    for i in inp:
        if i == '0':
            my_str += '1'
        elif i == '1':
            my_str += '0'
    return my_str
    