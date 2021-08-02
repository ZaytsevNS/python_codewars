def is_vow(inp: list) -> list:
    result: list = []
    for i in inp:
        if chr(i) in 'aeiou':
            result.append(chr(i))
        else:
            result.append(i)
    return result
