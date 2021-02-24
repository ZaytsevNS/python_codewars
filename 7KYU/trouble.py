def trouble(arr: list, target: int) -> list:
    result = [arr[0]]
    for i in range(1, len(arr)):
        if result[-1] + arr[i] == target:
            continue
        else:
            result.append(arr[i])
    return result


trouble([1, 2, 3, 4, 5], 3)
