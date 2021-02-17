def find_it(x: list) -> int:
    dict_num = {}
    for item in x:
        if item in dict_num:
            dict_num[item] += 1
        else:
            dict_num[item] = 1
    for el in dict_num:
        if dict_num[el] % 2 != 0:
            return el