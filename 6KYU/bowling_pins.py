def bowling_pins(arr: list) -> str:
    row1 = '7 8 9 x'
    row2 = ' 4 5 6 '
    row3 = '  2 3  '
    row4 = '   1   '
    pins = '\n'.join([row1,row2,row3,row4])
    for i in range(len(arr)):
        if arr[i] == 10:
            arr[i] = 'x'
    new_pins = []
    for i in pins:
        if i in map(str, arr):
            new_pins.append(' ')
        else:
            if i.isdigit():
                new_pins.append('I')
            else:
                new_pins.append(i)
    return ''.join(new_pins).replace('x', 'I')
