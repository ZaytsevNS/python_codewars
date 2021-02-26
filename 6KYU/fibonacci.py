def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    D = {0: 0}
    result = [0, 1]
    for i in range(1, n):
        result.append(result[-1] + result[-2])
        D[i] = result[i]
    return list(D.values())

fibonacci(6)
