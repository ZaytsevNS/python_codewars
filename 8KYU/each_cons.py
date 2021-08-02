def each_cons(arr: list, n: int) -> list:
    # First way
    result: list = []
    i: int = 0
    while i < len(arr) - n + 1:
        result.append(arr[i:i+n])
        i += 1
    return result

    # Second way
    # return [arr[i:i+n] for i in range(len(arr) - n + 1)]
    