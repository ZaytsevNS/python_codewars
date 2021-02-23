def div_con(x):
    sum_for_int, sum_for_str = sum([i for i in x if type(i) == int]), sum([int(i) for i in x if type(i) == str])
    return sum_for_int - sum_for_str

div_con([9, 3, '7', '3'])
