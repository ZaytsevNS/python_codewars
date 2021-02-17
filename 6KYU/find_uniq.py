def find_uniq(arr: list) -> int:
    """ This function returns the unique number from 'arr'. """
    count_min = arr.count(min(arr))
    count_max = arr.count(max(arr))
    if count_min == 1:
        return min(arr)
    return max(arr)