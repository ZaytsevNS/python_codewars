def fake_bin(x:str):
    my_str = []
    for num in x:
        if int(num) >= 5:
            num = 1
            my_str.append(num)
        else:
            num = 0
            my_str.append(num)
    return (''.join(map(str, my_str)))