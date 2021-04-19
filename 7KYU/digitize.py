def digitize(num: int) -> list:
    if num == 0:
        return [0]
    my_digitize = []
    while num != 0:
        l = num % 10
        my_digitize.append(l)
        num = (num - l) // 10
    return list(reversed(my_digitize))
    