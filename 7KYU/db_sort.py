from itertools import chain


def db_sort(arr: list) -> list:
    if all(type(i) == int for i in arr) or all(type(i) == str for i in arr):
        return sorted(arr)
    list_for_num: list = []
    list_for_symb: list = []
    list_for_str_num: list = []
    list_for_exclamation: list = []
    for i in arr:
        if type(i) == int:
            list_for_num.append(i)
        elif i.isdigit():
            list_for_str_num.append(int(i))
        elif i == '!':
            list_for_exclamation.append(i)
        else:
            list_for_symb.append(i)
    result_sorted_list: list = []
    result_sorted_list.append(sorted(list_for_num))
    result_sorted_list.append(list_for_exclamation)
    result_sorted_list.append([str(i) for i in sorted(list_for_str_num)])
    result_sorted_list.append(sorted(list_for_symb))
    return list(chain(*result_sorted_list))
