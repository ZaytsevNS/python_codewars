def first_non_consecutive(arr: list) -> int:
    ''' This function returns the first element of an array that is not consecutive. '''
    if len(arr) < 2:
        return None
    non_consecutive = []
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] != 1:
            non_consecutive.append(arr[i+1])
    if len(non_consecutive) == 0:
        return None
    return int(''.join(map(str, non_consecutive[:1])))