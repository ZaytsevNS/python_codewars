def sort_array(source_array: list) -> list:
    """ This function sort the odd numbers in ascending order 
    while leaving the even numbers at their original positions """
    sorted_odd_num: list = sorted(filter(lambda x: x % 2, source_array))
    result_sorted_array: list = []
    idx: int = 0
    for i in source_array:
        if not i % 2:
            result_sorted_array.append(i)
        else:
            result_sorted_array.append(sorted_odd_num[idx])
            idx += 1
    return result_sorted_array
    