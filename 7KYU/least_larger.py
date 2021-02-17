def least_larger(arr: list, idx: int) -> int:
    """ This function returns the index of the least number larger than the element at the given index, or -1 if there is no such index. """
    if len(arr) < 0:
        return -1
    my_element = [i for i in arr if i > arr[idx]]
    if len(my_element) > 0:
        return arr.index(min(my_element))
    return -1