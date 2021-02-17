def next_id(arr: list) -> int:
    """ This function returns the smallest unused ID. """
    reversed_arr = list(sorted(arr.copy()))
    if len(reversed_arr) == 0:
        return 0
    for i in range(len(reversed_arr) - 1):
        if reversed_arr[0] != 0:
            return 0
        if reversed_arr[i] - reversed_arr[i+1] == 0:
            continue
        if reversed_arr[i] - reversed_arr[i+1] != -1 and reversed_arr[i] - reversed_arr[i+1] != 0:
            return reversed_arr[i] + 1
    return max(reversed_arr) + 1