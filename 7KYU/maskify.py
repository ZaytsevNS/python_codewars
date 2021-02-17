def maskify(cc):
    if len(cc) <= 4:
        return cc
    my_str = ""
    for i in cc:
        my_str += str(i)
        str_maskify = "#"*len(my_str[:-4])+my_str[-4:]
    return str_maskify