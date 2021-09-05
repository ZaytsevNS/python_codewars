def determine_sequence(series_array: list) -> int:
    arithmetic = all([series_array[i] - series_array[i+1] == series_array[0] - series_array[1] for i in range(len(series_array)-1)])
    geometric = False if not all(series_array) else all([series_array[i] / series_array[i+1] == series_array[0] / series_array[1] for i in range(len(series_array)-1)])
    if arithmetic and geometric:
        return 2
    elif geometric:
        return 1
    elif arithmetic:
        return 0
    else:
        return -1
    