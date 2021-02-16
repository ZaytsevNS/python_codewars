def averages(arr: list) -> list:
    if arr is None:
        return []
    my_avg = []
    for i in range(len(arr) - 1):
        my_avg.append((arr[i] + arr[i + 1]) / 2)
    return my_avg