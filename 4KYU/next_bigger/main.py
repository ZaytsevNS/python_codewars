#from itertools import permutations


def next_bigger(num: int) -> int:
    digit_of_num: list = list(str(num))
    max_num = int(''.join(map(str, sorted(digit_of_num, reverse=True))))
    min_num = int(''.join(map(str, sorted(digit_of_num))))
    my_num = num
    while my_num <= max_num:
        my_num += 1
        if int(''.join(map(str, sorted(list(str(my_num)))))) == min_num:
            return my_num
    else:
        return -1
    
#     list_of_num = sorted(set([int(''.join(i)) for i in permutations(str(n))]))
#     try:
#         if len(list_of_num) < 2:
#             return -1
#         else:
#             return list_of_num[list_of_num.index(n) + 1]
#     except IndexError as error:
#         return -1
