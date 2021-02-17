def sum_array(arr:list):
    if arr is None or len(arr) <= 2:
        return 0
    sorted_arr = sorted(arr)
    return sum(sorted_arr[1:-1])