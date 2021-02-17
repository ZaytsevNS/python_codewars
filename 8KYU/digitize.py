def digitize(n: int) -> list:
    num = []
    for el in str(n):
        num.append((int(el)))
    return list(reversed(num))