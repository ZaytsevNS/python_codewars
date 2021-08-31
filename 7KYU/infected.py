def infected(s: str):
    try:
        map: list = []
        for i in s.split('X'):
            if '1' in i:
                map.append(len(i) * '1')
            else:
                map.append(i)
        final_map = ''.join(map)
        return 100 * final_map.count('1') / len(final_map)
    except ZeroDivisionError:
        return 0
